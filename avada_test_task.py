from datetime import datetime,timedelta
from itertools import cycle
from typing import List



def get_schedule_generation(date_start: str, date_end: str, days_work: int, days_skip: int) -> List[str]:
    """
    Функция генерации рабочих дней

    :param date_start:(str, isoformat date) - Дата с которой начинается расписание
    :param date_end:(str, isoformat date)  - Дата на которой заканчивается расписание
    :param days_work:(int) - Сколько дней подряд парикмахер работает
    :param days_skip:(int) - Сколько дней после этого отдыхает

    :return:(List[str]) - Возвращать функция должна массив строк с датами в формате isoformat
    """
    # Преобразуем аргументы в формат isoformat date
    start_date = datetime.fromisoformat(date_start).date()
    end_date = datetime.fromisoformat(date_end).date()

    # Создаем пустой список для хранения рабочих дней
    list_work_days = []

    # Создаем итератор с набором рабочих и нерабочих дней
    iter_work_and_skip_days = cycle(["work_days"] * days_work + ["skip_days"] * days_skip)

    # Продолжаем генерировать даты, пока не достигнем конца периода
    while start_date <= end_date:
        # Если текущий день является рабочим, добавляем его в список рабочих дней
        if next(iter_work_and_skip_days) == "work_days":
            list_work_days.append(start_date.isoformat())

        # Увеличиваем дату на один день
        start_date += timedelta(days=1)

    return list_work_days

if __name__ == "__main__":
    print(get_schedule_generation('2022-04-20', '2022-04-23', 1, 1))
    print(get_schedule_generation('2022-04-25', '2022-06-26', 0, 4))
    print(get_schedule_generation('2022-05-14', '2022-05-24', 1, 95))
    print(get_schedule_generation('2022-04-10', '2022-04-23', 1, 1))

