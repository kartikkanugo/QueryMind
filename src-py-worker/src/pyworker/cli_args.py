"""
module for functions of cli related
"""

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CliArgs:
    """
    CLI arguments for the Python worker server.
    Extend this dataclass as new CLI parameters are introduced.
    """

    config_fp: Path

    @classmethod
    def parse(cls) -> "CliArgs":
        """parses the cli args"""
        parser = argparse.ArgumentParser(
            prog="pyworker",
            description="Python Worker Server",
        )

        parser.add_argument(
            "-c",
            "--config",
            dest="config_fp",
            type=Path,
            required=True,
            help="Path to env.toml configuration file",
        )

        args = parser.parse_args()

        return cls(
            config_fp=args.config_fp,
        )
