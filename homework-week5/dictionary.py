def check_isomorphic(word1: str, word2: str) -> bool:
    """
    Kiểm tra xem hai từ có đẳng cấu (isomorphic) với nhau hay không.

    :param word1: Chuỗi ký tự thứ nhất (a).
    :param word2: Chuỗi ký tự thứ hai (b).
    :return: True nếu hai từ đẳng cấu, False nếu ngược lại.
    """
    # Điều kiện bắt buộc: Hai từ phải có cùng độ dài.
    if len(word1) != len(word2):
        return False

    # 1. Khởi tạo hai bản đồ (dictionaries) để lưu ánh xạ hai chiều:
    # map_a_to_b: Ánh xạ từ ký tự của word1 sang ký tự của word2.
    # map_b_to_a: Ánh xạ từ ký tự của word2 sang ký tự của word1.
    map_a_to_b = {}
    map_b_to_a = {}
    # 2. Duyệt qua từng cặp ký tự tương ứng (a_char, b_char) trong hai từ.
    for a_char, b_char in zip(word1, word2):
        
        # Xử lý ánh xạ từ word1 sang word2 (map_a_to_b):
        if a_char in map_a_to_b:
            # Nếu a_char đã được ánh xạ, kiểm tra xem nó có ánh xạ
            # đúng đến b_char theo ánh xạ đã thiết lập trước đó không.
            if map_a_to_b[a_char] != b_char:
                # Nếu a_char trước đó ánh xạ sang ký tự khác, thì vi phạm
                # quy tắc: một ký tự chỉ có thể ánh xạ đến duy nhất một ký tự.
                return False
        else:
            # Nếu a_char chưa được ánh xạ, thiết lập ánh xạ:
            map_a_to_b[a_char] = b_char

        # Xử lý ánh xạ từ word2 sang word1 (map_b_to_a):
        # Đây là điều kiện đảm bảo ánh xạ là MỘT-MỘT (One-to-One).
        if b_char in map_b_to_a:
            # Nếu b_char đã được ánh xạ ngược, kiểm tra xem nó có ánh xạ 
            # đúng từ a_char theo ánh xạ đã thiết lập trước đó không.
            if map_b_to_a[b_char] != a_char:
                # Nếu b_char trước đó ánh xạ từ ký tự khác, thì vi phạm
                # quy tắc: Hai ký tự khác nhau của word1 không thể ánh xạ 
                # đến cùng một ký tự b_char của word2.
                return False
        else:
            # Nếu b_char chưa được ánh xạ ngược, thiết lập ánh xạ ngược:
            map_b_to_a[b_char] = a_char

    # 3. Nếu vòng lặp hoàn thành mà không có vi phạm nào, hai từ là đẳng cấu.
    return True

# --- Ví dụ kiểm tra theo đề bài ---
# Ví dụ 1: "abca" và "zbxz" -> True ('a'->'z', 'b'->'b', 'c'->'x')
print(f"'abca', 'zbxz': {check_isomorphic('abca', 'zbxz')}") # Kết quả: True

# Ví dụ 2: "egg" và "add" -> True ('e'->'a', 'g'->'d')
print(f"'egg', 'add': {check_isomorphic('egg', 'add')}") # Kết quả: True

# Ví dụ 3: "paper" và "title" -> True ('p'->'t', 'a'->'i', 'e'->'l', 'r'->'e')
print(f"'paper', 'title': {check_isomorphic('paper', 'title')}") # Kết quả: True

# Ví dụ 4: "foo" và "bar" -> False ('f'->'b', 'o'->'a', nhưng 'o' phải ánh xạ đến 'r')
print(f"'foo', 'bar': {check_isomorphic('foo', 'bar')}") # Kết quả: False

# Ví dụ 5: "show" và "same" -> False ('s'->'s', 'h'->'a', 'o'->'m', nhưng 'w' phải ánh xạ đến 'e')
# Ở đây 's' -> 's', 'h' -> 'a', 'o' -> 'm'. Khi đến 'w' và 'e', 
# 'w' chưa có ánh xạ, đặt 'w' -> 'e'. 
# Tuy nhiên, nếu xét ví dụ 'ab' và 'aa' -> False ('a'->'a', 'b'->'a'. Ký tự 'a' và 'b' khác nhau
# trong word1 ánh xạ đến cùng ký tự 'a' trong word2 -> vi phạm điều kiện ánh xạ ngược/một-một)
# Ví dụ 6: "show" và "seem" (đúng theo đề bài ở cột phải)
print(f"'show', 'seem': {check_isomorphic('show', 'seem')}") # Kết quả: False ('s'->'s', 'h'->'e'. Lần 2: 'o'->'e'. Ký tự 'h' và 'o' khác nhau
                                                                 # của word1 cùng ánh xạ đến 'e' của word2 -> False)
                                                                 
# Ví dụ 7: "aab" và "ced" -> False (Độ dài bằng nhau, nhưng không đủ ký tự)
# Ví dụ 8: "aab" và "ccd" -> True ('a'->'c', 'b'->'d')
print(f"'aab', 'ccd': {check_isomorphic('aab', 'ccd')}") # Kết quả: True
# Ví dụ 9: "abc" và "defg" -> False (Độ dài khác nhau)
print(f"'abc', 'defg': {check_isomorphic('abc', 'defg')}") # Kết quả: False