import bisect

def min_interval_binary_search(intervals, queries):
    # 1. Sắp xếp Intervals theo ĐỘ DÀI (ngắn trước, dài sau)
    # x[1] - x[0] + 1 là công thức tính độ dài
    intervals.sort(key=lambda x: x[1] - x[0] + 1)
    
    # 2. Sắp xếp Queries (nhưng phải giữ lại vị trí gốc để trả kết quả)
    # sorted_qs = [(giá_trị, index_gốc), ...]
    sorted_qs = sorted([(q, i) for i, q in enumerate(queries)])
    
    # Tách riêng list chỉ chứa giá trị để tí nữa dùng Binary Search
    q_values = [x[0] for x in sorted_qs]
    
    # Mảng kết quả ban đầu toàn -1
    res = [-1] * len(queries)
    
    # Mảng đánh dấu xem query tại vị trí i (trong sorted_qs) đã có đáp án chưa
    # False = chưa có, True = đã có
    answered = [False] * len(queries)
    
    # 3. Duyệt từng Interval (từ ngắn đến dài)
    for l, r in intervals:
        length = r - l + 1
        
        # --- ĐÂY LÀ PHẦN DÙNG HINT BINARY SEARCH ---
        
        # Tìm vị trí query đầu tiên >= l
        start_idx = bisect.bisect_left(q_values, l)
        
        # Tìm vị trí query cuối cùng <= r
        # (bisect_right tìm vị trí > r, nên ta giới hạn đến đó)
        end_idx = bisect.bisect_right(q_values, r)
        
        # Duyệt qua các query nằm trong phạm vi [l, r]
        for k in range(start_idx, end_idx):
            # Nếu query này chưa có đáp án
            if not answered[k]:
                # Lấy index gốc của nó  
                original_idx = sorted_qs[k][1]
                # Gán độ dài (đây chắc chắn là độ dài nhỏ nhất vì ta duyệt từ ngắn->dài)
                res[original_idx] = length
                # Đánh dấu đã xong
                answered[k] = True

                # *Lưu ý tối ưu: Trong thực tế (Hard problems), việc duyệt vòng for này 
                # có thể vẫn chậm nếu dữ liệu quá lớn. Các cao thủ sẽ dùng thêm 
                # kỹ thuật DSU (Disjoint Set Union) để "nhảy cóc" qua các query đã xong.
                # Nhưng logic Binary Search cơ bản là như thế này.
                
    return res

# --- Test lại ---
intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]

print("Output:", min_interval_binary_search(intervals, queries))