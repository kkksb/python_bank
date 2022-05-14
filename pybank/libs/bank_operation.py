import sys
import os
from traceback import print_tb

# pythonのモジュール探索の起点となるディレクトリに、.../libsを入れる
# すると、pybankからプログラムを実行してもlibs内のモジュール同士で読み込みができる
sys.path.append(os.path.join(os.path.dirname(__file__)))

import operation_common as opc


class Account:
    deposit = 10000


class BankOperate:
    def __init__(self, passbook):
        self.passbook_operator = PassbookOperator(passbook)

    def operate(self, deal):
        if deal in opc.OperationManual.operation:
            if deal == "withdraw":
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

        if Account.deposit >= deal_money:
            try:
                Account.deposit -= deal_money
            except Exception:
                print("取引金額は整数で入力してください")
        else:
            print("預金以上の金額を引き出すことはできません")

        print(f"残高は{Account.deposit}円になりました")

        self.passbook_operator.write_deal_on_passbook(Account.deposit)

    def deposit_func(self):
        print("預ける金額を入力してください")

        try:
            deal_money = int(input())
            Account.deposit += deal_money
        except Exception:
            print("整数を入力してください")

        print(f"残高は{Account.deposit}円になりました")

        self.passbook_operator.write_deal_on_passbook(Account.deposit)

    def show(self):
        print(f"現在の残高は{Account.deposit}円です")

    def init_account(self):
        Account.deposit = int((self.passbook_operator.read_last_deal()))
        Account.deposit = Account.deposit
        print("通帳から読み取った値で残高を更新しました。(現状、口座のデータを保存する先がテキストファイルだけ)")


class PassbookOperator:
    def __init__(self, passbook):
        self.passbook = passbook
        # 手帳をDB代わりに利用する

    def read_last_deal(self):
        with open(self.passbook, "r") as f:
            try:
                last_line = f.readlines()[-1]
            except Exception:
                print("空のファイルは読み込めません")
        return last_line

    def write_deal_on_passbook(self, deal_result):
        if deal_result > 0:
            with open(self.passbook, "a") as f:
                f.write("\n" + str(deal_result))
                print("通帳に取引履歴を記帳しました。")
        else:
            pass
