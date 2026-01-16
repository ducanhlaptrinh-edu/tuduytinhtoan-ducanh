import sys

# Tăng giới hạn đệ quy cho trường hợp chuỗi dài (tối đa 1000 ký tự)
sys.setrecursionlimit(2000)

def solve():
    # Đọc toàn bộ dữ liệu đầu vào
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data	)
    
    try:
        # Đọc số lượng câu hỏi Q
        q_str = next(iterator, None)
        if not q_str: return
        Q = int(q_str)
    except StopIteration:
        return

    # Hàm đệ quy có nhớ (Memoization)
    def check(i, j, A, B, memo):
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Trường hợp cơ sở: Hết xâu A
        if i == len(A):
            # Nếu B cũng hết thì OK, ngược lại là False
            return j == len(B)
        
        # Ký tự hiện tại của A
        char_a = A[i]
        
        res = False
        
        if char_a.isupper():
            # Nếu là in hoa, bắt buộc phải khớp với B[j]
            if j < len(B) and char_a == B[j]:
                res = check(i + 1, j + 1, A, B, memo)
            else:
                res = False
        else:
            # Nếu là in thường, có 2 cách:
            
            # Cách 1: Xóa ký tự này (nhảy qua i, giữ nguyên j)
            res = check(i + 1, j, A, B, memo)
            
            # Cách 2: Biến thành in hoa để khớp (nếu khớp được)
            if not res and j < len(B) and char_a.upper() == B[j]:
                res = check(i + 1, j + 1, A, B, memo)
                
        memo[state] = res
        return res

    # Xử lý từng truy vấn
    for _ in range(Q):
        try:
            a = next(iterator)
            b = next(iterator)
            
            # Reset bảng nhớ cho mỗi test case
            memo = {}
            if check(0, 0, a, b, memo):
                print("YES")
            else:
                print("NO")
        except StopIteration:
            break

if __name__ == '__main__':
    solve()