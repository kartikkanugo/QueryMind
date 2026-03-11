"""
Configuration model and loader for the application's env.toml file.

Defines the validated configuration schema and provides a helper
method to load and validate the configuration from disk.
"""

from pathlib import Path
import tomllib

from pydantic import BaseModel, ValidationError
from pyworker.errors import ConfigError


class EnvConfig(BaseModel):
    """
    Root configuration model for the Python worker server.
    """

    address: str
    port: int
    log_lvl: str

    @classmethod
    def load(cls, path: Path) -> "EnvConfig":
        """
        Load and validate configuration from an env.toml file.

        Parameters
        ----------
        path : Path
            Path to the env.toml configuration file.

        Returns
        -------
        EnvConfig
            Validated configuration object.

        Raises
        ------
        ConfigError
            If the file cannot be found, parsed, or validated.
        """

        if not path.exists():
            raise ConfigError(f"Configuration file not found: {path}")

        try:
            with open(path, "rb") as f:
                data = tomllib.load(f)
        except Exception as e:
            raise ConfigError(f"Failed to parse TOML configuration: {e}") from e

        try:
            toml_data = data["py_server"]
        except KeyError as e:
            raise ConfigError("Missing [py_server] section in configuration") from e

        try:
            return cls(**toml_data)
        except ValidationError as e:
            raise ConfigError(f"Invalid configuration: {e}") from e
