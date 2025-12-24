def count_smaller_mergesort(nums):
    # Dòng 1: Gắn thẻ từng số với vị trí ban đầu của nó
    arr = list(enumerate(nums)) 
    # Dòng 2: Tạo xô chứa kết quả đếm
    counts = [0] * len(nums)

    def merge_sort(nums):
        # Dòng 3: Chia đôi
        mid = len(nums) // 2
        if mid:
            # Dòng 4: Đệ quy chia nhỏ tiếp
            left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
            
            # --- KHÚC QUAN TRỌNG NHẤT: TRỘN (MERGE) ---
            # Dòng 5: Duyệt ngược từ cuối về đầu để điền vào danh sách
            for i in range(len(nums) - 1, -1, -1):
                # Dòng 6: So sánh phần tử lớn nhất của Left và Right
                if not right or (left and left[-1][1] > right[-1][1]):
                    # Dòng 7: Cộng dồn kết quả đếm  a
                    counts[left[-1][0]] += len(right)
                    # Dòng 8: Lấy phần tử từ Left bỏ vào vị trí i
                    nums[i] = left.pop()
                else:
                    # Dòng 9: Lấy phần tử từ Right bỏ vào vị trí i
                    nums[i] = right.pop()
                    
        return nums

    merge_sort(arr)
    return counts