import asyncio
import json
from typing import Optional


class TCPServer:
    """
    Async TCP server used to communicate with a Rust client.

    Responsibilities:
    - Accept TCP connections
    - Receive JSON messages from the client
    - Process the message
    - Allow sending responses later via `send_response`
    """

    def __init__(self, host: str, port: int):
        # Address where the TCP server will listen
        self.host = host
        self.port = port

        # asyncio server instance
        self.server: Optional[asyncio.AbstractServer] = None

        # StreamWriter used to send responses back to the connected client
        self.writer: Optional[asyncio.StreamWriter] = None

    async def handle_client(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        """
        Handles a connected TCP client.

        This coroutine runs for the lifetime of a client connection.
        It continuously reads data from the socket until the client disconnects.
        """

        # Save writer so we can respond later using send_response()
        self.writer = writer

        addr = writer.get_extra_info("peername")
        print(f"Client connected: {addr}")

        try:
            while True:
                # Read up to 4096 bytes from the socket
                data = await reader.read(4096)

                # If empty bytes are returned, the client closed the connection
                if not data:
                    break

                # Decode incoming bytes to string
                message = data.decode()
                print(f"Received: {message}")

                # Process incoming message
                await self.process_message(message)

        except Exception as e:
            print(f"Connection error: {e}")

        finally:
            # Clean up connection
            print(f"Client disconnected: {addr}")

            writer.close()
            await writer.wait_closed()

            # Reset stored writer
            self.writer = None

    async def process_message(self, message: str):
        """
        Process a message received from the Rust client.

        Currently this only parses JSON and prints it.
        You can extend this method to trigger tasks such as:
        - CSV processing
        - database queries
        - job execution
        """

        try:
            data = json.loads(message)

            print("Parsed JSON:", data)

            # Example placeholder processing
            result = {"status": "ok", "received": data}

            # Optionally send response immediately
            # await self.send_response(json.dumps(result))

        except json.JSONDecodeError:
            print("Invalid JSON received")

    async def send_response(self, response: str):
        """
        Send a response back to the connected Rust client.

        This can be called from anywhere in your application once a client
        connection exists.
        """

        if self.writer is None:
            print("No client connected. Cannot send response.")
            return

        # Encode string to bytes before sending
        self.writer.write(response.encode())

        # Ensure buffer is flushed to the socket
        await self.writer.drain()

    async def start(self):
        """
        Start the TCP server and begin accepting connections.
        """

        self.server = await asyncio.start_server(
            self.handle_client,
            self.host,
            self.port,
        )

        addr = self.server.sockets[0].getsockname()
        print(f"Server listening on {addr}")

        # Keep the server running forever
        async with self.server:
            await self.server.serve_forever()
