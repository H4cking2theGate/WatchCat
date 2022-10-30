from core.log import logger
from core.watchcat import WatchCat
import click


@click.command(name="WatchCat")
@click.option(
    "-t",
    help="目标文件/目录",
)
@click.option(
    "-r",
    help="规则文件目录",
)
def cli(t, r):
    v = WatchCat(rule_path=r)
    v.run(1)


if __name__ == "__main__":
    cli()
