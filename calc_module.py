def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Число має бути невід'ємним")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_calories(weight: float, coef: float) -> float:
    if weight <= 0 or coef <= 0:
        raise ValueError("Параметри мають бути додатними")
    return round(weight * 30 * coef, 1)
