class OperationManual:
    operation_numbers = tuple(range(1, 5))
    operation = ("show", "deposit", "withdrow", "exit")
    operation_map = dict(zip(operation_numbers, operation))
