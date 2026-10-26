"""Лабораторна робота №3 (варіант 10): сортування купою (Heapsort) з трасуванням."""


def swap(arr, i, j):
    """Міняє місцями два елементи в масиві."""
    arr[i], arr[j] = arr[j], arr[i]


def sink(arr, i, n, trace=True):
    """Процедура 'занурення' елемента arr[i] вниз по купі розміру n."""
    k = i
    if trace:
        print(f"Починаємо 'занурювати' елемент: {arr[k]} з індексу {k}")
    while True:
        j = 2 * k + 1                      # лівий нащадок
        if j >= n:
            if trace:
                print(f"Елемент {arr[k]} на індексі {k} досяг кінця купи. Завершуємо.")
            break
        if j + 1 < n and arr[j + 1] > arr[j]:
            if trace:
                print(f"  Порівнюємо {arr[j]} (лівий) та {arr[j+1]} (правий). Обираємо {arr[j+1]}")
            j += 1
        elif trace:
            print(f"  Обираємо лівий дочірній елемент: {arr[j]} на індексі {j}")
        if arr[k] >= arr[j]:
            if trace:
                print(f"  {arr[k]} (батько) >= {arr[j]} (найбільший дочірній). Елемент на своєму місці.")
            break
        if trace:
            print(f"  Міняємо місцями {arr[k]} (батько) та {arr[j]} (дочірній)")
        swap(arr, k, j)
        if trace:
            print(f"  Масив після обміну: {arr}")
        k = j


def heapsort(arr, trace=True):
    n = len(arr)
    if trace:
        print(f"Початковий масив: {arr}\n")
        print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        sink(arr, i, n, trace)
        if trace:
            print("---------------------------------")
    if trace:
        print(f"Масив після побудови купи: {arr}\n")
        print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        if trace:
            print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        if trace:
            print(f"Розмір купи зменшився до {i}. Відновлюємо властивості купи.")
        sink(arr, 0, i, trace)
        if trace:
            print(f"Масив на поточному кроці: {arr}\n")
    return arr


if __name__ == "__main__":
    A = [87, 79, 97, 82, 98, 40, 42, 88, 61]      # Варіант 10
    sorted_A = heapsort(A)
    print(f"Відсортований масив: {sorted_A}")
