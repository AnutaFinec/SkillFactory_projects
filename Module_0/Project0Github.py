import numpy as np
number = np.random.randint(1, 101)  # загадываем случайное целое число, которое нужно будет угадать

def BinarySearcgith(number):
    """Запускаем функцию бинарного поиска."""
    count = 1  # запускаем счетчик попыток
    predict = list(range(1, 101))  # создаем переменную "предположение"
    first = predict[0]  # задаем начало интервала поиска
    last = predict[-1]  # задаем конец интервала поиска
    index = 0
    while (first <= last) and (index == 0):
        count += 1
        mid = (first+last) // 2  # находим середину интервала поиска
        if number == predict[mid]:  # если искомое число = середине предполагаемого интервала,
            index = mid  # то мы угадали
        else:
            if number < predict[mid]:  # если искомое число меньше середины интервала,
                last = mid - 1  # то мы уменьшаем конец интервала на 1.
            else:
                first = mid + 1  # если искомое число больше интервала, то мы увеличиваем начало интервала на 1.
    return count


def score_game(BinarySearch):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число."""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(BinarySearch(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


print(score_game(BinarySearch))
