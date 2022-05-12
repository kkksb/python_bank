import operation_common as opc


class Account:
    def __init__(self, deposit=10000):
        self.deposit = deposit


class BankOperate:
    def __init__(self, decided_operation):
        self.decided_operation = decided_operation

    def operate(self):
        if self.decided_operation in opc.OperationManual.operation:
            print("取引を行います")
        else:
            print("不正値が入力されました")
        
    def withdraw(self):
        pass

    def deposit(self):
        pass

    def show():
        pass