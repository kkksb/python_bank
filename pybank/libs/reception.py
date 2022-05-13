import os
import operation_common as opc


class Reception:
    def distribute_process(self):
        last_menu_number = opc.OperationManual.operation_numbers[-1]
        
        while True:
            print(f"以下のメニューから操作を選択してください[1~{last_menu_number}]")
            print("1: 残高確認 2: 預入れ 3: 引き出し 4: プログラムを終了")
            user_choice = int(input())

            if user_choice in opc.OperationManual.operation_numbers:
                if user_choice == last_menu_number:
                    print("プログラムを終了します")
                    exit()
                break
            else:
                print("メニューから選択してください")
        return opc.OperationManual.operation_map.get(user_choice)

    def confirm_passbook(self, passbook):
        # カレントディレクトリはpybank
        dir = "./resouces"
        file = dir + passbook
        if os.path.exists(file):
            print("通帳を読み込みました。")
        else:
            print("通帳ファイルが存在しません。新規作成します")
            with open(file, "w", encoding="utf-8"):
                print("ファイルを作成しました。")
