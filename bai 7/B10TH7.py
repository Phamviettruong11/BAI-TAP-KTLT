print("PHAM VIET TRUONG MSV:235752021610101")
def find_longest_words(text):
    # Chuyển đổi văn bản thành danh sách các từ
    words = text.split()

    # Tìm độ dài của từ dài nhất
    max_length = max(len(word) for word in words)

    # Lọc ra các từ có độ dài bằng với từ dài nhất
    longest_words = [word for word in words if len(word) == max_length]

    return longest_words

# Ví dụ văn bản
text = "Nguyen Xuan Vu sinh vien ĐHV K64 KTĐK&TĐH."

# Gọi hàm để tìm các từ dài nhất trong văn bản
longest_words = find_longest_words(text)

print("Các từ dài nhất trong văn bản là:", longest_words)
