
N = 500

for n in range(2, N):
    kq = True
    for i in range(2, n-1):
        if n%i == 0:
            kq = False
            break # dung vong lap for

    if kq==True:
        print(n, " la so nguyen to")
