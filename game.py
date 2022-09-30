"""Игра в угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(
        out_number: int = 1,
        out_start: int = 1,
        out_end: int = 100) -> int:
    """Угадывает число с помощью "Бинарного дерева"

    Args:
        out_number (int, optional): Загаданное число. Defaults to 1.
        out_start (int): Загаданное число.
        out_end (int): Загаданное число.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        mid = int((out_start + out_end) / 2)

        if mid > out_number:
            out_end = mid

        elif mid < out_number:
            out_start = mid

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {out_number}")
            break  # конец игры выход из цикла
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    start_rm = 1
    end_rm = 1000

    np.random.seed(1)  # фиксируем сид для Воспроизводимости!
    random_array = np.random.randint(start_rm, end_rm, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number, start_rm, end_rm))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
