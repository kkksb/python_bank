from libs.bank_operation import BankOperate
from libs.reception import Reception 


class PyBank:
    def __init__(self, filename):
        self.reception = Reception()
        self.filename = filename

        passbook = self.reception.confirm_passbook(self.filename)
        self.bank_operate = BankOperate(passbook)

    def operate(self):
        self.bank_operate.init_account()

        deal = self.reception.distribute_process()
        self.bank_operate.operate(deal)
