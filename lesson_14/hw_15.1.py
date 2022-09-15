def dict_handler(dictionary, key, default_value):
    try:
        return dictionary[key]
    except KeyError:
        dictionary[key] = default_value
    except TypeError:
        raise TypeError("key змінюваний тип данних")
    return dictionary[key]


if __name__ == "__main__":
    dictionary_1 = {'Andriy': 21, 'Stepan': 23}
    print(dict_handler(dictionary_1, 'Andriy', 26))
    print(dict_handler(dictionary_1, 'Artem', 19))
    print(dict_handler(dictionary_1, ['Artem', 'Vanya'], 25))
    print(dictionary_1)
