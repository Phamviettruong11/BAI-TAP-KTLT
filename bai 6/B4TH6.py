print("PHAM VIET TRUONG MSV:235752021610101")
class RomanConverter:
    def __init__(self):
        # Tạo một dictionary để lưu trữ các ký tự La Mã và giá trị tương ứng
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, roman):
        total = 0
        prev_value = 0

        # Duyệt qua từng ký tự trong chuỗi La Mã từ phải sang trái
        for symbol in reversed(roman):
            value = self.roman_numerals[symbol]

            # Nếu ký tự hiện tại có giá trị lớn hơn hoặc bằng ký tự trước đó, cộng vào tổng
            if value >= prev_value:
                total += value
            else:
                # Nếu ký tự hiện tại có giá trị nhỏ hơn ký tự trước đó, trừ khỏi tổng
                total -= value

            # Cập nhật giá trị trước đó
            prev_value = value

        return total


# Sử dụng class RomanConverter để chuyển đổi số La Mã thành số nguyên
converter = RomanConverter()
roman_number = "XV"  # Thí dụ: số La Mã là "XV"
integer_value = converter.roman_to_int(roman_number)
print(f"Số La Mã {roman_number} chuyển thành số nguyên là: {integer_value}")
