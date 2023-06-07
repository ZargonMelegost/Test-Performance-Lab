def circle_generator(n,m):
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield v
def corle():
    x =  list(circle_generator(n, m))
    stroka_chisel = int("".join(map(str, x)))
    print(stroka_chisel)

if __name__ == '__main__':
    n = int(input("Задайте число массива n:"))
    m = int(input("Задайте интервал длины m:"))
    corle()
