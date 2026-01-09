class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        # Quan trọng: Lệnh trừ tiền phải nằm THỤT VÀO trong if
        if amount <= self.balance:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.owner} : {self.balance}"

def menu_display():
    # Đọc dòng đầu tiên: Tên và số dư
    try:
        user_inf = input().strip().split()
        if len(user_inf) < 2: return # Kiểm tra input rỗng
        
        name = user_inf[0]
        balance = float(user_inf[1])
        
        # SỬA LỖI 1: Truyền biến 'name' chứ không phải 'user_inf'
        my_acc = BankAccount(name, balance)

        # Đọc số lượng lệnh
        command_count = int(input())

        i = 0
        while i < command_count:
            command_line = input().strip().split()
            if len(command_line) >= 2:
                cmd_type = command_line[0]
                amount = float(command_line[1])

                if cmd_type == "DEPOSIT":
                    my_acc.deposit(amount)
                elif cmd_type == "WITHDRAW":
                    my_acc.withdraw(amount)
            
            i += 1

        # In kết quả
        print(f"{my_acc.balance:.2f}")
        
    except Exception:
        # Bắt lỗi nếu input nhập vào bị sai định dạng
        pass

if __name__ == "__main__":
    menu_display()