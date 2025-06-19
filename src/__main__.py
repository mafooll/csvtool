from argparse import ArgumentParser
from csv import DictReader
from tabulate import tabulate

from src.core.build import CommandBuilder


def main():
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to csv file")
    parser.add_argument(
        "--filter",
        help="'column op[>, <, =] logic[AND, OR] (column op value)'",
    )
    parser.add_argument("--sort", help="'column:sort_type[asc,desc]'")
    parser.add_argument("--aggregate", help="'column:agg_type[min,max,avg]'")
    args = parser.parse_args()

    with open(args.filepath, newline="") as f:
        data = list(DictReader(f))

    filter_cmd, sort_cmd, agg_cmd = CommandBuilder(args).build(data)

    if filter_cmd:
        data = filter_cmd.execute(data)

    if sort_cmd:
        data = sort_cmd.execute(data)

    if agg_cmd:
        print(
            tabulate(
                [[agg_cmd.execute(data)]],
                headers=[f"{args.aggregate.upper()}"],
                tablefmt="pretty",
            )
        )
    else:
        print(tabulate(data, headers="keys", tablefmt="pretty"))


if __name__ == "__main__":
    main()
