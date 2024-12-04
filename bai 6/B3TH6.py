print("PHAM VIET TRUONG MSV:235752021610101")
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng của lớp Nam và Nu
aNam = Nam()
aNu = Nu()

# In kết quả trả về từ phương thức getGender
print(aNam.getGender())  # In "Nam"
print(aNu.getGender())   # In "Nữ"
