# https://www.tryexponent.com/practice/prepare/root-of-number
def power(base: float, exponent: int) -> float:
    result = 1.0
    for _ in range(exponent):
        result *= base
    return result

def root(x: float, n: int) -> float:
    if x == 0:
        return 0.0

    lower_bound = 0.0
    upper_bound = max(1.0, x)
    approx_root = (upper_bound + lower_bound) / 2.0

    while (upper_bound - lower_bound) >= 0.001:
        if power(approx_root, n) > x:
            upper_bound = approx_root
        elif power(approx_root, n) < x:
            lower_bound = approx_root
        else:
            break

        approx_root = (upper_bound + lower_bound) / 2.0

    return approx_root