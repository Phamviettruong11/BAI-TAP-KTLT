print ("sinh vien:PHAM VIET TRUONG MSV:235752021610101")
Dãy = input("Nhập dãy các từ: ")
các_từ = Dãy.split()
max_length = max(len(từ) for từ in các_từ)
longest_các_từ = [từ for từ in các_từ if len(từ) == max_length]
print("Từ dài nhất là:", ', '.join(longest_các_từ))
