"""
module run server main loop initialiser
"""

from pathlib import Path
from pyworker.cli_args import CliArgs
from pyworker.config_models import EnvConfig
from pyworker.server import TCPServer
import asyncio


def main():
    """main function that holds the entire server"""
    args = CliArgs.parse()

    cfg = EnvConfig.load(Path(args.config_fp))

    print(cfg)

    server = TCPServer(cfg.address, cfg.port)
    asyncio.run(server.start())


if __name__ == "__main__":
    main()
