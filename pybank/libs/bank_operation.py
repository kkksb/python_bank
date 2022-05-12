import operation_common as opc


class Account:
    def __init__(self, deposit=10000):
        self.deposit = deposit


class BankOperate:
    def __init__(self, decided_operation):
        self.decided_operation = decided_operation
        account = Account
        self.deposit = account.deposit

    def operate(self):
        if self.decided_operation in opc.OperationManual.operation:
            print("取引を行います")

            eval(self.decided_operation)()
        else:
            print("不正値が入力されました")
        
    def withdraw(self):
        print("引き出す金額を入力してください")
        deal_money = int(input())

        if self.deposit >= deal_money:
            try:
                self.deposit -= deal_money
            except Exception:
                print("取引金額は整数で入力してください")
        else:
            print("預金以上の金額を引き出すことはできません")

    def deposit(self):
        print("引き出す金額を入力してください")
        deal_money = int(input())

        try:
            self.deposit += deal_money
        except Exception:
            print("整数を入力してください")

    def show(self):
        print("現在の残高は" + self.deposit + "円です")