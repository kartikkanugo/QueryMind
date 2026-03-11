"""
module errors
"""


class PyWorkerError(Exception):
    """
    Base exception for all pyworker errors.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ConfigError(PyWorkerError):
    """
    Raised when configuration loading or validation fails.
    """


class CliArgumentError(PyWorkerError):
    """
    Raised when CLI arguments are invalid.
    """


class ServerStartupError(PyWorkerError):
    """
    Raised when the TCP server fails to start.
    """


class WorkerRuntimeError(PyWorkerError):
    """
    Raised during runtime processing errors.
    """
