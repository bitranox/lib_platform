# EXT
from click.testing import CliRunner

# OWN
import lib_platform.lib_platform_cli as lib_platform_cli

runner = CliRunner()
runner.invoke(lib_platform_cli.cli_main, ['--version'])
runner.invoke(lib_platform_cli.cli_main, ['-h'])
runner.invoke(lib_platform_cli.cli_main, ['info'])
