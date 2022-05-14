class OperationManual:
    operation_numbers = tuple(range(1, 5))
    operation = ("show", "deposit", "withdraw", "exit")
    operation_map = dict(zip(operation_numbers, operation))
