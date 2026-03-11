"""
module run server main loop initialiser
"""

from pathlib import Path
from pyworker.cli_args import CliArgs
from pyworker.config_models import EnvConfig


def main():
    """main function that holds the entire server"""
    args = CliArgs.parse()

    cfg = EnvConfig.load(Path(args.config_fp))

    print(cfg)


if __name__ == "__main__":
    main()
