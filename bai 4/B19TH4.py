print ("sinh vien:PHAM VIET TRUONG MSV:235752021610101")
def sieve(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return tuple(i for i in range(limit) if is_prime[i])
P = sieve(1_000_000)
print(P)
