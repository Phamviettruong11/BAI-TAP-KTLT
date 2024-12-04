print ("sinh vien:PHAM VIET TRUONG MSV:235752021610101")
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  
        triangle.append(row)
    return triangle
n = int(input("Nhập số dòng n: "))
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)
