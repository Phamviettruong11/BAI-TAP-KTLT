print ("sinh vien:PHAM VIET TRUONG MSV:235752021610101")
Chuỗi = input("Nhập chuỗi: ")
Chuỗi_mới = ''.join([ch for ch in Chuỗi if not ch.isdigit()])
print("Chuỗi mới sau khi loại bỏ chữ số:",Chuỗi_mới)
