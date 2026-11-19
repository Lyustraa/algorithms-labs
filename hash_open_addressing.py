# Лабораторна робота № 4, варіант 10
# Лістинг 4.2. Хешування з відкритою адресацією (закрите хешування)
# Константи, ключі та хеш-функції - з лістингу 4.1
from hash_chaining import *

NIL = None
DELETED = "<DELETED>"


def build_closed_hash_table(words: list, m: int, h) -> list:
    """Хеш-таблиця з відкритою адресацією (лінійне дослідження)."""
    table = [NIL] * m
    for word in words:
        start = h(word, m)
        for i in range(m):
            j = (start + i) % m                 # h(k, i) = (h'(k) + i) mod m
            if table[j] is NIL or table[j] == DELETED:
                table[j] = word
                break
        else:
            print(f"Помилка: таблиця заповнена, слово {word} не додано")
    return table


def search_closed(table: list, word: str, h):
    """Пошук. Повертає (індекс або None, кількість порівнянь ключів)."""
    m = len(table)
    start = h(word, m)
    comparisons = 0
    for i in range(m):
        j = (start + i) % m
        if table[j] is NIL:                     # порожня комірка: ключа немає
            return None, comparisons
        if table[j] != DELETED:
            comparisons += 1
            if table[j] == word:
                return j, comparisons
    return None, comparisons


def delete_closed(table: list, word: str, h):
    """Відкладене видалення: комірку позначаємо DELETED, а не NIL."""
    j, comparisons = search_closed(table, word, h)
    if j is not None:
        table[j] = DELETED
    return j, comparisons


def display_closed_table(table: list, title: str):
    print(f"\n--- {title} ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = "(NULL)" if item is NIL else item
        print(f"{i:02d}     | {value}")


if __name__ == "__main__":
    for name, h, m in (("ділення, m=13", hash_div, M_DIV),
                       ("множення, m=16", hash_mul, M_MUL)):
        t = build_closed_hash_table(WORDS, m, h)
        display_closed_table(t, f"Відкрита адресація, метод {name}")
