def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует список словарей по значению ключа state"""
    filtered_data = []

    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)

    return  filtered_data


# data = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]
#        [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]

# Выход функции
# print(filter_by_state(data))
# print(filter_by_state(data, "CANCELED"))


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция  сортирует список словарей по дате"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse) # Сортировка выполняется по ключу "date". Часть "reverse=reverse" устанавливает порядок сортировки - убывание (True)/возрастание (False)

# Сортировка по убыванию, т. е. сначала последние операции
sorted_data = sort_by_date(data)
print(sorted_data)

# Сортировка по возрастанию
sorted_data_asc = sort_by_date(data, reverse=False)
print(sorted_data_asc)

# date = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}, {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
