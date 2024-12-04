print("PHAM VIET TRUONG MSV:235752021610101")
from itertools import islice

def file_read_from_head(fname, nlines):
    with open(fname, 'r', encoding='utf-8') as f:
        for line in islice(f, nlines):
            print(line, end='')

file_read_from_head('D:/a.txt', 2)
