"""
3 типи сортування
"""

__all__ = ["bubble_sort", "insertion_sort", "selection_sort"]


def bubble_sort(numbers):
    """
    :param numbers: відповідає за список чисел, котрі потрібно відсортувати
    методом бульбашки
    :return: повертає відсортовані числа за допомогою цієї функції
    """
    for i in range(len(numbers) - 1):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def insertion_sort(numbers):
    """
    :param numbers: відповідає за список чисел, котрі потрібно відсортувати
    методом вставки
    :return: повертає відсортовані числа за допомогою цієї функції
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


def selection_sort(numbers):
    """
    :param numbers: відповідає за список чисел, котрі потрібно відсортувати
    методом вибору
    :return: повертає відсортовані числа за допомогою цієї функції
    """
    for i in range(len(numbers)-1):
        min_index = i
        for j in range(i+1, len(numbers)-1):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

