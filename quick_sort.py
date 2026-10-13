# Лістинг 2.2 — Швидке сортування за схемою Хоара (Quick Sort) 

qs_comps = 0
qs_assigns = 0
qs_calls = 0

def partition_hoare(arr, low, high):
    global qs_comps, qs_assigns
    pivot = arr[low]
    qs_assigns += 1
    i = low - 1
    j = high + 1
    
    while True:
        while True:
            i += 1
            qs_comps += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            qs_comps += 1
            if arr[j] <= pivot:
                break
                
        if i >= j:
            return j
            
        arr[i], arr[j] = arr[j], arr[i]
        qs_assigns += 3
        print(f"   Обмін arr[{i}] ({arr[j]}) і arr[{j}] ({arr[i]}) -> {arr}")

def quicksort_hoare(arr, low, high):
    global qs_calls
    qs_calls += 1
    if low < high:
        print(f"Виклик quicksort(a, {low}, {high}), pivot = arr[{low}] = {arr[low]}")
        q = partition_hoare(arr, low, high)
        print(f"Результат розбиття (j = {q}): {arr}")
        quicksort_hoare(arr, low, q)
        quicksort_hoare(arr, q + 1, high)

if __name__ == "__main__":
    A = [87, 79, 97, 82, 98, 40, 42, 88, 61]
    print("--- Quick Sort за Хоаром ---")
    quicksort_hoare(A, 0, len(A) - 1)
    print(f"\nВідсортований масив: {A}")
    print(f"Порівнянь: {qs_comps}, Присвоєнь: {qs_assigns}, Викликів: {qs_calls}")
