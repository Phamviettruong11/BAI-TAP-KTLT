print("PHAM VIET TRUONG MSV:235752021610101")
import tkinter as tk

def create_personal_info_form():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Thông Tin Cá Nhân")
    root.geometry("400x300")  # Đặt kích thước cửa sổ

    # Hiển thị tiêu đề
    title_label = tk.Label(root, text="Thông Tin Cá Nhân", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    # Thông tin cá nhân
    info = {
        "Họ và Tên": "Phạm Viết Trường",
        "Ngày Sinh": "19/02/2005",
        "MSSV": "235752021610101",
        "Ngành Học": "KTĐK&TĐH"
    }

    # Hiển thị thông tin trên form
    for key, value in info.items():
        label = tk.Label(root, text=f"{key}: {value}", font=("Helvetica", 12))
        label.pack(anchor="w", padx=20, pady=5)

    # Nút đóng cửa sổ
    close_button = tk.Button(root, text="Đóng", command=root.destroy, font=("Helvetica", 12))
    close_button.pack(pady=20)

    # Bắt đầu giao diện
    root.mainloop()

# Chạy form thông tin cá nhân
create_personal_info_form()
