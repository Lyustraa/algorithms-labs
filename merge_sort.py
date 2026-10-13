# Лістинг 2.1 — Псевдокод ітеративного та рекурсивного сортування злиттям. 

def merge_sort_iterative(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    assignments = 0
    
    print("--- Ітеративний Merge Sort ---")
    print(f"Початковий масив: {a}\n")
    
    i = 1
    while i < n:
        print(f"=== Крок i = {i} ===")
        j = 0
        while j < n:
            left = j
            mid = min(j + i, n)
            right = min(j + 2 * i, n)
            
            if mid < right:
                L = a[left:mid]
                R = a[mid:right]
                assignments += len(L) + len(R)
                
                idx_l = idx_r = 0
                curr = left
                
                while idx_l < len(L) and idx_r < len(R):
                    comparisons += 1
                    if L[idx_l] <= R[idx_r]:
                        a[curr] = L[idx_l]
                        idx_l += 1
                    else:
                        a[curr] = R[idx_r]
                        idx_r += 1
                    assignments += 1
                    curr += 1
                    
                while idx_l < len(L):
                    a[curr] = L[idx_l]
                    idx_l += 1
                    curr += 1
                    assignments += 1
                    
                while idx_r < len(R):
                    a[curr] = R[idx_r]
                    idx_r += 1
                    curr += 1
                    assignments += 1
                    
                print(f"Об'єднуємо підмасиви a[{left}:{mid}] ({L}) і a[{mid}:{right}] ({R})")
                print(f"Масив після об'єднання: {a}")
                
            j += 2 * i
        i *= 2
        
    print(f"\nВідсортований масив: {a}")
    print(f"Порівнянь: {comparisons}, Присвоєнь: {assignments}\n")
    return a

rec_comps = 0
rec_assigns = 0
rec_calls = 0

def merge_sort_recursive(arr):
    global rec_comps, rec_assigns, rec_calls
    rec_calls += 1
    
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        rec_comps += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        rec_assigns += 1
        
    merged.extend(left[i:])
    merged.extend(right[j:])
    rec_assigns += len(left[i:]) + len(right[j:])
    
    print(f"Злиття {left} та {right} -> {merged}")
    return merged

if __name__ == "__main__":
    A = [87, 79, 97, 82, 98, 40, 42, 88, 61]
    merge_sort_iterative(A)
    print("--- Рекурсивний Merge Sort ---")
    res = merge_sort_recursive(A)
    print(f"Результат: {res}")
    print(f"Порівнянь: {rec_comps}, Присвоєнь: {rec_assigns}, Викликів: {rec_calls}")
