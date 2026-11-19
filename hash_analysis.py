# Лабораторна робота № 4, варіант 10
# Лістинг 4.3. Аналіз ефективності пошуку (видалення); функції - з лістингів 4.1, 4.2
from hash_chaining import *
from hash_open_addressing import *

KEYS = list(dict.fromkeys(WORDS))   # 8 різних ключів: пошук виконується за ключем
ABSENT = "ДІМ"                      # ключа немає в таблиці (невдалий пошук)


def analyse(table, words, h, search):
    """Кількість порівнянь для кожного ключа, максимум і середнє."""
    counts = {w: search(table, w, h)[1] for w in words}
    top = max(counts.values())
    worst = [w for w in words if counts[w] == top]
    return counts, worst, top, sum(counts.values()) / len(counts)


if __name__ == "__main__":
    for name, h, m in (("ділення, m=13", hash_div, M_DIV),
                       ("множення, m=16", hash_mul, M_MUL)):
        alpha = len(WORDS) / m              # у таблиці зберігається n = 9 елементів
        for kind, build, search in (
                ("ланцюжки", build_open_hash_table, search_open),
                ("відкрита адресація", build_closed_hash_table, search_closed)):
            t = build(WORDS, m, h)
            counts, worst, top, avg = analyse(t, KEYS, h, search)
            print(f"\n[{kind}, {name}] alpha = {alpha:.3f}")
            for w, c in counts.items():
                print(f"  {w:7s} K={key_value(w):3d} h={h(w, m):2d} порівнянь: {c}")
            print(f"  максимум: {', '.join(worst)} ({top}), середнє: {avg:.3f}")
            print(f"  невдалий пошук {ABSENT}: K={key_value(ABSENT)}, "
                  f"h={h(ABSENT, m)}, порівнянь: {search(t, ABSENT, h)[1]}")
        print(f"  теорія (ланцюжки):   успішний 1+a/2 = {1 + alpha / 2:.3f}, "
              f"невдалий a = {alpha:.3f}")
        print(f"  теорія (лін. досл.): успішний {0.5 * (1 + 1 / (1 - alpha)):.3f}, "
              f"невдалий {0.5 * (1 + 1 / (1 - alpha) ** 2):.3f}")

    # Видалення у закритій таблиці (метод ділення): DELETED проти NIL
    t = build_closed_hash_table(WORDS, M_DIV, hash_div)
    print("\n--- Видалення ВЕЧОРА з закритої таблиці (метод ділення) ---")
    t_nil = t.copy(); t_nil[t_nil.index("ВЕЧОРА")] = NIL
    print("Якщо комірку 1 зробити NIL, пошук А:", search_closed(t_nil, "А", hash_div))
    delete_closed(t, "ВЕЧОРА", hash_div)
    print("Якщо позначити DELETED, пошук А:   ", search_closed(t, "А", hash_div))
    print("Пошук ВЕЧЕРІ:", search_closed(t, "ВЕЧЕРІ", hash_div))
