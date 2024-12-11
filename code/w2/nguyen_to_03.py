
def kiem_tra_so_nguyen_to(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

M1 = 2
M2 = 20
for k in range(M1, M2):
    kq = kiem_tra_so_nguyen_to(k)
    if kq == True:
        print(k, ": ", kq)
