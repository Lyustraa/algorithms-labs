# Лабораторна робота № 4, варіант 10
# Лістинг 4.1. Хешування з роздільними ланцюжками (відкрите хешування)
import math

# Розміри таблиць
M_DIV = 13   # для методу ділення
M_MUL = 16   # для методу множення
A_CONST = (math.sqrt(5) - 1) / 2   # константа Кнута ~ 0.6180339887

# Вхідна послідовність (варіант 10): слова прислів'я
WORDS = ["НЕ", "ХВАЛИ", "ДЕНЬ", "ДО", "ВЕЧОРА", "А", "ХЛІБ", "ДО", "ВЕЧЕРІ"]

# Позиції букв українського алфавіту (рис. 4.3)
ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
POS = {ch: i + 1 for i, ch in enumerate(ALPHABET)}


def key_value(word: str) -> int:
    """Числове значення ключа K = сума номерів позицій букв."""
    return sum(POS[ch] for ch in word)


def hash_div(word: str, m: int = M_DIV) -> int:
    """Метод ділення: h(K) = K mod m."""
    return key_value(word) % m


def hash_mul(word: str, m: int = M_MUL) -> int:
    """Метод множення: h(K) = floor(m * (K*A mod 1))."""
    k = key_value(word)
    return int(m * ((k * A_CONST) % 1))


def build_open_hash_table(words: list, m: int, h) -> list:
    """Хеш-таблиця з роздільними ланцюжками (відкрите хешування)."""
    table = [[] for _ in range(m)]
    for word in words:
        address = h(word, m)
        table[address].append(word)         # вставка в кінець ланцюжка
    return table


def search_open(table: list, word: str, h):
    """Пошук у ланцюжку. Повертає (знайдено, кількість порівнянь)."""
    comparisons = 0
    for item in table[h(word, len(table))]:
        comparisons += 1
        if item == word:
            return True, comparisons
    return False, comparisons


def delete_open(table: list, word: str, h):
    """Видалення зі списку: спочатку пошук, потім видалення вузла."""
    found, comparisons = search_open(table, word, h)
    if found:
        table[h(word, len(table))].remove(word)
    return found, comparisons


def display_open_table(table: list, title: str):
    print(f"\n--- {title} ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


if __name__ == "__main__":
    for name, h, m in (("ділення, m=13", hash_div, M_DIV),
                       ("множення, m=16", hash_mul, M_MUL)):
        t = build_open_hash_table(WORDS, m, h)
        display_open_table(t, f"Відкрите хешування, метод {name}")
