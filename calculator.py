from enum import Enum

class Operation(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

class Calculator:
    def __init__(self, title: str):
        self.title = title
        self.history = []  # List of dicts: {Operation: [a, b, result]}

    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined")
        return a / b

    def calculate(self, a: float, b: float, op: Operation) -> float:
        if op == Operation.ADD:
            result = self.add(a, b)
        elif op == Operation.SUB:
            result = self.sub(a, b)
        elif op == Operation.MUL:
            result = self.mul(a, b)
        elif op == Operation.DIV:
            result = self.div(a, b)
        else:
            raise ValueError("Unsupported Operation")
        
        self.update_history(a, b, result, op)
        return result

    def update_history(self, a: float, b: float, res: float, op: Operation):
        self.history.append({op: [a, b, res]})

    def get_operator_as_character(self, op: Operation) -> str:
        return {
            Operation.ADD: "+",
            Operation.SUB: "-",
            Operation.MUL: "*",
            Operation.DIV: "/"
        }.get(op, "?")

    def print_history(self):
        print(f"{self.title} History:")
        for entry in self.history:
            for op, operands in entry.items():
                print(f"{operands[0]} {self.get_operator_as_character(op)} {operands[1]} = {operands[2]}")

