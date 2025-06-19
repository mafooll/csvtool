class CommandBuilder:
    def __init__(self, args):
        self.args = args

    def build(self, data):
        from src.commands.filter.command import FilterCommand
        from src.commands.sort.command import (
            SortCommand,
            parse_sort_arg,
            is_numeric_column,
        )
        from src.commands.aggregate.command import (
            AggregateCommand,
            parse_aggregate_arg,
        )

        def build_filter():
            if self.args.filter:
                return FilterCommand(self.args.filter)
            return None

        def build_sort():
            if self.args.sort:
                column, sort_type = parse_sort_arg(self.args.sort)
                numeric = is_numeric_column(data, column)
                return SortCommand(column, sort_type, numeric)
            return None

        def build_aggregate():
            if self.args.aggregate:
                column, agg_type = parse_aggregate_arg(self.args.aggregate)
                return AggregateCommand(column, agg_type)
            return None

        return build_filter(), build_sort(), build_aggregate()
