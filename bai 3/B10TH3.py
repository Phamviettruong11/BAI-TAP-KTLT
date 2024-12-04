print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
import math
def Tinh(R):
    """
    Hàm Tinh tính chu vi và diện tích hình tròn với bán kính R.
    Tham số:
    R (float): Bán kính của hình tròn.
    Trả về:
    tuple: (chu_vi, dien_tich) nếu R hợp lệ.
    In thông báo lỗi nếu R không hợp lệ.
    """
    if not isinstance(R, (int, float)):
        print("Giá trị bán kính phải là số.")
        return
    if R <= 0:
        print("Giá trị bán kính phải lớn hơn 0.")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * (R ** 2)
    return chu_vi, dien_tich
def main():
    try:
        R_input = input("Nhập bán kính hình tròn: ")
        R = float(R_input)
        result = Tinh(R)
        if result:
            chu_vi, dien_tich = result
        print(f"Chu vi hình tròn: {chu_vi:.2f}")
        print(f"Diện tích hình tròn: {dien_tich:.2f}")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số thực.")
if __name__ == "__main__":
    main()
