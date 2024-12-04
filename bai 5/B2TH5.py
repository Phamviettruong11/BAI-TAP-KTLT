print("PHAM VIET TRUONG MSV:235752021610101")
import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('Ngày ' + str(t1.day))
print('Tháng ' + str(t1.month))
print('Phút ' + str(t1.minute))
print('Giây ' + str(t1.second))
t2 = dt.datetime.now()
diff = t2 - t1
print('Chênh lệch bao nhiêu ngày? ' + str(diff.days))
