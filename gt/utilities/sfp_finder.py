from math import isqrt, sqrt

def is_ps(n:float) -> bool:
    return sqrt(n) == isqrt(n)

def sfp(n:int) -> int:
    for i in range(1,n+1):
        if n%i == 0 and is_ps(n//i):
            break
    return i

def main():
    ...

if __name__ == "__main__":
    main()