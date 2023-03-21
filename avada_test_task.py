from datetime import datetime,timedelta
from itertools import cycle
from typing import List




def get_schedule_generation(date_start: str, date_end: str, days_work: int, days_skip: int) -> List:

    """
    Функция генерации рабочих дней

    :param date_start:(str, isoformat date) - Дата с которой начинается расписание
    :param date_end:(str, isoformat date)  - Дата на которой заканчивается расписание
    :param days_work:(int) - Сколько дней подряд парикмахер работает
    :param days_skip:(int) - Сколько дней после этого отдыхает

    :return:(List)-Возвращать функция должна массив строк с датами в формате isoformat
    """

    #Преобразуем аргументывформат isoformat date)
    start_date =datetime.fromisoformat(date_start)
    end_date = datetime.fromisoformat(date_end)

    #Создаем пустой список для хранения рабочих дней
    list_work_days = []

    #Создаем итератор с набором рабочих  и нерабочих дней
    iter_work_and_skip_days = cycle(["work_days"]*days_work + ["skip_days"]*days_skip)

    #Создаем цыкл который проходить с начала графика и до конца
    while start_date <= end_date:
        if next(iter_work_and_skip_days) == "work_days":
            list_work_days.append(date_start)

        start_date += timedelta(days=1)



    return list_work_days

if __name__ == "__main__":
    print(get_schedule_generation('2022-04-20', '2022-04-23', 1, 1))
    print(get_schedule_generation('2022-04-25', '2022-06-26', 0, 4))
    print(get_schedule_generation('2022-05-14', '2022-05-24', 1, 95))
    print(get_schedule_generation('2022-04-10', '2022-04-23', 1, 1))