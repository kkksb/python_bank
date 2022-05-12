from libs.bank_operation import BankOperate
from libs.reception import Reception 


class PyBank:
    def __init__(self):
        self.reception = Reception()
        self.operation = BankOperate()

    def operate(self):
        deal = self.reception.distribute_process()
        self.operation.operate(deal)