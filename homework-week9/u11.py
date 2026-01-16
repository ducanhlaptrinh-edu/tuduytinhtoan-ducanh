import re

def check_regex(test_cases):
    for s in test_cases:
        try:
            # Thử biên dịch chuỗi s xem có phải regex chuẩn không
            re.compile(s)
            print("True")
        except re.error:
            # Nếu thư viện re báo lỗi -> Chuỗi không hợp lệ
            print("False")


data_input = [".*\+", ".*+"] 
check_regex(data_input)