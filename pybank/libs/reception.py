import operation_common as opc


class Reception:
    def distribute_process():
        last_menu_number = opc.OperationManual.operation_numbers[-1]
        
        while True:
            print("以下のメニューから操作を選択してください[1~" + last_menu_number + "]")
            user_choice = input()

            if user_choice in opc.OperationManual.operation_numbers:
                if user_choice == last_menu_number:
                    print("取引を終了します")
                    break
            else:
                print("1から" + last_menu_number + "の間の数値で指定してください")
            
        return opc.OperationManual.operation_map.get(user_choice)
