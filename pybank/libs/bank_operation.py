from itertools import accumulate
import sys
import os

# pythonのモジュール探索の起点となるディレクトリに、.../libsを入れる
# すると、pybankからプログラムを実行してもlibs内のモジュール同士で読み込みができる
sys.path.append(os.path.join(os.path.dirname(__file__)))

import operation_common as opc


class Account:
    deposit = 10000


class BankOperate:
    def __init__(self):
        self.deposit = Account.deposit

    def operate(self, deal):
        if deal in opc.OperationManual.operation:
            if deal == "withdrow":
                self.withdraw()
            if deal == "deposit":
                # depositはインスタンス変数にもあるので使えない
                self.deposit_func()
            if deal == "show":
                self.show()
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

        print(f"残高は{self.deposit}になりました")

    def deposit_func(self):
        print("預ける金額を入力してください")
        deal_money = int(input())

        try:
            self.deposit += deal_money
        except Exception:
            print("整数を入力してください")

        print(f"残高は{self.deposit}になりました")

    def show(self):
        print(f"現在の残高は{self.deposit}円です")


class PassbookOperator:
    def __init__(self, passbook_file):
        self.deposit = (self.read_last_deal()).get("deposit")
        Account.deposit = self.deposit
        self.passbook_file = passbook_file

    def update_passbook(self):
        pass

    def show(self):
        pass
        
    def read_last_deal(self):
        pass