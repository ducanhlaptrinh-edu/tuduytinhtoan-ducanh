import bisect

# def max_subarray_mod(nums, m):
#     max_mod = 0
#     current_prefix_sum = 0
    
#     # Danh sách lưu các tổng tiền tố đã gặp, luôn được sắp xếp tăng dần
#     # Khởi tạo [0] để xử lý trường hợp mảng con bắt đầu từ phần tử đầu tiên
#     sorted_prefixes = [0] 
    
#     for num in nums:
#         # 1. Tính tổng tiền tố hiện tại theo modulo m
#         current_prefix_sum = (current_prefix_sum + num) % m
        
#         # 2. Trường hợp cơ bản: Tính hiệu với tiền tố 0 (chính là current_prefix_sum)
#         max_mod = max(max_mod, current_prefix_sum)
        
#         # 3. Mẹo "Gợi ý": Tìm trong danh sách sorted_prefixes một số nhỏ nhất
#         # mà LỚN HƠN current_prefix_sum hiện tại.
#         # bisect_right trả về vị trí index mà tại đó phần tử > current_prefix_sum
#         idx = bisect.bisect_right(sorted_prefixes, current_prefix_sum)
        
#         # Nếu tìm thấy (idx chưa vượt quá độ dài danh sách) , nếu vượt quá thì chắc chắn current_pre lớn nhất và nó đã được lưu thành max_mod
#         if idx < len(sorted_prefixes):
#             # Công thức: (current - prefix_lớn_hơn + m) % m
#             # Hiểu đơn giản: mượn 1 vòng m để trừ ra số dư lớn
#             temp_mod = (current_prefix_sum - sorted_prefixes[idx] + m) % m
#             max_mod = max(max_mod, temp_mod)
            
#         # 4. Thêm tổng tiền tố hiện tại vào danh sách (giữ nguyên thứ tự sắp xếp)
#         bisect.insort(sorted_prefixes, current_prefix_sum)
        
#     return max_mod

# --- Chạy thử với các ví dụ trong ảnh ---


def find_max_mod(arr , mod) :   
    max_mod = 0
    current_prefix_sum = 0
    sorted_prefixes = [0]
    for num in arr : 
        current_prefix_sum = ( current_prefix_sum + num ) % mod # công thức đóng gói kẹo
        max_mod = max(max_mod  , current_prefix_sum)
        # hàm bs_right trả về vị trí đầu tiên trong ds sorted mà lớn hơn current-pre
        idx = bisect.bisect_right(sorted_prefixes , current_prefix_sum)
        # nếu idx >= len(sort) chứng tỏ current_pre là lớn nhất trong các pre_sorted và nó đã được lưu vô max-mod để chờ return
        if idx < len(sorted_prefixes): 
            # tìm ra số lớn hơn một chút để cái trong ngoặc tiến dần tới m-1
            temp_mod = (current_prefix_sum - sorted_prefixes[idx] + mod) % mod
            max_mod = max(temp_mod , max_mod) 
        bisect.insort(sorted_prefixes , current_prefix_sum ) 
    return max_mod
print(find_max_mod([3, 3, 9, 9, 5], 7))      