def iteration(phi, x0):
    for i in range(100):
        x = phi(x0)
        if abs(x - x0) < 1e-6:
            return x
        x0 = x

    print("Достигнуто максимальное число итераций.")
    return None