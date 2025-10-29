
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
P = tuple(i for i in range(2, 1_000_000) if la_so_nguyen_to(i))
print("So luong so nguyen to nho hon 1 trieu:", len(P))
print("Mot vai so dau tien:", P[:20])
