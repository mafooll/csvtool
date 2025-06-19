from re import findall, match, IGNORECASE
from src.commands.filter.strategy import (
    BaseStrategy,
    ComparisonStrategy,
    LogicStrategy,
)


def splitter(expr: str) -> list[str]:
    return [
        t.upper() if t.upper() in {"AND", "OR"} else t
        for t in findall(r"\(|\)|AND|OR|[^()\s]+", expr, IGNORECASE)
    ]


def precedence(op: str) -> int:
    if op == "AND":
        return 2
    if op == "OR":
        return 1
    return 0


def build_logic(op_stack, node_stack):
    op = op_stack.pop()
    right = node_stack.pop()
    left = node_stack.pop()
    node_stack.append(LogicStrategy(op.lower(), [left, right]))


def parse_expression(tokens: list[str]) -> BaseStrategy:
    op_stack: list[str] = []
    node_stack: list[BaseStrategy] = []
    for token in tokens:
        if token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack and op_stack[-1] != "(":
                build_logic(op_stack, node_stack)
            if not op_stack or op_stack.pop() != "(":
                raise ValueError("Missing opening parenthesis")
        elif token in {"AND", "OR"}:
            while (
                op_stack
                and op_stack[-1] in {"AND", "OR"}
                and precedence(op_stack[-1]) >= precedence(token)
            ):
                build_logic(op_stack, node_stack)
            op_stack.append(token)
        else:
            m = match(r"(\w+)(=|<|>)(.+)", token)
            if not m:
                raise ValueError(f"Invalid token: {token}")
            node_stack.append(ComparisonStrategy(*m.groups()))

    while op_stack:
        if op_stack[-1] == "(":
            raise ValueError("Missing closing parenthesis")

        build_logic(op_stack, node_stack)

    if len(node_stack) != 1:
        raise ValueError("Invalid expression")
    return node_stack[0]


class FilterCommand:
    def __init__(self, expr: str):
        self.strategy = parse_expression(splitter(expr))

    def execute(self, data: list[dict[str, str]]) -> list[dict[str, str]]:
        return self.strategy.apply(data)
