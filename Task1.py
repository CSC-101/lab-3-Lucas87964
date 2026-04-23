more = [x + 1 for x in [1, 2, 3, 4]]  # 1+1, 2+1, 3+1, 4+1
print()  # [2, 3, 4, 5]


def square(n: int) -> int:
    return n * n  # n=1 x=1, n=2 x=4, n=3 x=9, n=4 x=16


squares = [square(x) for x in [1, 2, 3, 4]]  #squares = [1, 4, 9, 16] same as above
print()


def check(n: int) -> bool:
    return n > 2  #n=0 false, n=1 false, n=2 false, n=3 true, n=4 true


answer = [x for x in range(5) if check(x)]  #answer=[3, 4]
print()


def inc(m: int) -> int:
    return m + 1  #m=3 return 4, m=4 return 5


def check(n: int) -> bool:
    return n > 2  #n=4 true, n=5 true


answer = [inc(x) for x in range(5) if check(x)]  #answer=[4, 5]
print()
