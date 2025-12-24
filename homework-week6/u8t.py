import heapq

def min_interval_length(intervals, queries):
    # 1. Chuẩn bị dữ liệu
    # Lưu truy vấn kèm index ban đầu để sau này trả kết quả đúng vị trí
    # sorted_queries = [(giá trị, index_gốc), ...]
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    
    # Sắp xếp intervals theo điểm bắt đầu (left)
    intervals.sort()
    
    # Mảng chứa kết quả, mặc định là -1
    res = [-1] * len(queries)
    
    # Min-Heap lưu trữ: (độ dài, điểm kết thúc)
    # Tại sao lưu điểm kết thúc? Để biết khi nào nó hết hiệu lực.
    min_heap = []
    
    i = 0 # Con trỏ duyệt qua intervals
    
    # 2. Duyệt qua từng truy vấn đã sắp xếp
    for q_val, q_idx in sorted_queries:
        
        # Bước A: Thêm các interval hợp lệ vào Heap
        # Nếu interval bắt đầu <= truy vấn hiện tại, ném vào Heap
        while i < len(intervals) and intervals[i][0] <= q_val:
            l, r = intervals[i]
            length = r - l + 1
            # Push vào heap: (độ dài, right)
            heapq.heappush(min_heap, (length, r))
            i += 1
            
        # Bước B: Loại bỏ các interval hết hạn
        # Nếu điểm kết thúc (right) < truy vấn hiện tại, nó không bao trùm q được nữa
        while min_heap and min_heap[0][1] < q_val:
            heapq.heappop(min_heap)
            
        # Bước C: Lấy kết quả
        # Phần tử trên đỉnh Heap là interval ngắn nhất còn hiệu lực
        if min_heap:
            res[q_idx] = min_heap[0][0]
            
    return res

# --- Chạy thử với ví dụ đầu tiên trong ảnh ---
intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]

print("Input Intervals:", intervals)
print("Input Queries:  ", queries)
result = min_interval_length(intervals, queries)
print("Output:         ", result)