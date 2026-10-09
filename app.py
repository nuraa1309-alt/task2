def fibonacci(n):
    if n <= 0:
        return "Zəhmət olmasa 0-dan böyük müsbət ədəd daxil edin."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# İstifadəçidən ədəd alırıq
try:
    n = int(input("Hansi sira daxilindeki Fibonacci ededini tapmaq isteyirsiniz (n): "))
    result = fibonacci(n)
    print(f"Fibonacci ardicilliginda {n}-ci hedd: {result}")
except ValueError:
    print("Xahis olunur tam eded daxil edin!")