import main_menu        #добавляет то что бует нарисовано на экране

import json             #для работы с JSON-файлами
import os               #чтобы проверить, существует ли файл (os.path.exists).


#загружаем список из джсон и в джсон
def load_tasks():
    # Загружает задачи из tasks.json. Если файла нет — возвращает пустой список."""
    
    # Проверяем: существует ли файл tasks.json?
    if not os.path.exists("tasks.json"):
        return []   # Файла нет — возвращаем пустой список
    
    # Открываем файл на чтение
    with open("tasks.json", "r", encoding="utf-8") as file:
        data = json.load(file)   # Читаем JSON и превращаем в словарь Python
    
    return data["tasks"]   # Возвращаем список задач

# Сохраняет список задач в tasks.json.
def save_tasks(tasks):

    data = {"tasks": tasks}   # Оборачиваем список в словарь
    
    # Открываем файл на запись
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# показывает весь список блокнота
def show_tasks_1(list_tasks):
            
    # если список задачь пуст - даем пользователю об этом знать.
    if not list_tasks:
        print("Список пуст")
        input("\nНажмите Enter для выхода в главное меню... ")
        return True

    # если список задачь не пуст - показываем список
    else:
        print(f"Актуальный список: {list_tasks}")
        input("\nНажмите Enter для выхода в главное меню... ")
        return True

# вносит в конец списка новую задачу + показывает весь список блокнота
def adding_task_2(list_tasks):
    input_add_task = input("Введите текст: ")
    if input_add_task == "":
        print("ВНИМАНИЕ ВЫ НЕ ВВЕЛИ ТЕКСТ!")
        return True
    else:
        list_tasks.append(input_add_task)
        save_tasks(list_tasks)

    print("Задача внесена в список дел!")
    print(f"Актуальный список: {list_tasks}")
    input("\nНажмите Enter для выхода в главное меню... ")
    return True

# удаляет задачу по выбору пользователя из списка. + делает проверки на правильность выбора удаляемой задачи + показывает весь список блокнота
def block_delete_3(list_tasks):

    # если список задачь пуст - даем пользователю об этом знать.
    if not list_tasks:
        print("Список пуст")
        input("\nНажмите Enter для выхода в главное меню... ")
        return True

    # если список задачь не пуст - выполняется код дальше
    else:

        while True:

            # перед тем как принять цифру тестим то что ввёл пользователь
            try:
                print(f"Актуальный список: {list_tasks}")
                delete_task = int(input("Какую задачу желаете удалить? (укажите соответствующую цифру по порядку: 1 или 2 или 3 и т.п...): "))

            # ловит ошибку если пользователь ввёл текст
            except ValueError:
                print("Ошибка! Нужно ввести цифру...")

            # если ошибки нет
            else:
                # если введённое число больше чем всего задачь - ловит ошибку и говорит об
                if 1 <= delete_task <= len(list_tasks):
                    index_to_delete = delete_task - 1
                    list_tasks.pop(index_to_delete)
                    save_tasks(list_tasks)
                    print("Задача успешно удалена!")
                    print(f"Актуальный список: {list_tasks}")
                    input("\nНажмите Enter для выхода в главное меню... ")
                    return False

                # если введённое число соответствует кол-ву задачь : задача успешно удаляется
                else:
                    input("Задачи с таким номером нет... Нажмите Enter для выхода в главное меню... ")
                    return False

# минипрограммка, высчитывающяая среднюю зп за минуту секунду и тп
def calculate_salary_4():
    # =========== КОНСТАНТЫ (Нормативы времени) ===========
    WORKING_DAYS_PER_YEAR = 247
    MONTHS_PER_YEAR = 12
    WEEKS_PER_YEAR = 52.14
    WORKING_HOURS_PER_YEAR = 1972
    WORKING_MINUTES_PER_YEAR = WORKING_HOURS_PER_YEAR * 60
    WORKING_SECONDS_PER_YEAR = WORKING_MINUTES_PER_YEAR * 60
    
    
    # =========== 1. СЛОЙ РАСЧЕТОВ ===========
    def calculate_salary_metrics(
        salary: int, 
        bonus: int, 
        quarterly_bonus: int, 
        salary_13: int, 
        other_bonus_year: int
    ) -> dict:
        # Считаем средний доход в месяц
        salary_per_months = (
            salary 
            + bonus 
            + (quarterly_bonus * 4 / MONTHS_PER_YEAR) 
            + (salary_13 / MONTHS_PER_YEAR) 
            + (other_bonus_year / MONTHS_PER_YEAR)
        )
        
        # Считаем все остальные периоды
        salary_per_year    = salary_per_months * MONTHS_PER_YEAR
        salary_per_weeks   = salary_per_year / WEEKS_PER_YEAR
        salary_per_days    = salary_per_year / WORKING_DAYS_PER_YEAR
        salary_per_hours   = salary_per_year / WORKING_HOURS_PER_YEAR
        salary_per_minutes = salary_per_year / WORKING_MINUTES_PER_YEAR
        salary_per_seconds = salary_per_year / WORKING_SECONDS_PER_YEAR
    
        return {
            "year": salary_per_year,
            "month": salary_per_months,
            "week": salary_per_weeks,
            "day": salary_per_days,
            "hour": salary_per_hours,
            "minute": salary_per_minutes,
            "second": salary_per_seconds
        }
        
    # =========== СЛОЙ ИНТЕРФЕЙСА ===========
    
    def print_report(metrics: dict) -> None:
        # 1. Сначала собираем многострочный текст в одну переменную
        report_text = f"""Общий доход со всеми надбавками:
    Общий доход за год:                  {metrics['year']:,.2f} руб.
    Средний доход в месяц:               {metrics['month']:,.2f} руб.
    Средний доход в календарную неделю:  {metrics['week']:,.2f} руб.
    -------------------------------------------
    Стоимость одного рабочего дня:       {metrics['day']:,.2f} руб.
    Стоимость одного рабочего часа:      {metrics['hour']:,.2f} руб.
    Стоимость одной рабочей минуты:      {metrics['minute']:,.4f} руб.
    Стоимость одной рабочей секунды:     {metrics['second']:,.4f} руб."""
    
        print(report_text)
    
        
    
    # =========== ГЛАВНАЯ ТОЧКА ВХОДА ===========
    def main() -> None:
        print("=== КАЛЬКУЛЯТОР v1.02 ===")
        
        # отображение пользователю
        prompt_salary          = "Введите ваш оклад в месяц, без учёта премий: "
        prompt_bonus           = "Введите вашу премию в месяц, без учёта оклада: "
        prompt_quarterly_bonus = "Введите вашу квартальную премию: "
        prompt_salary_13       = "Введите вашу 13 зарплату: "
        prompt_other_bonus     = "Введите сумму ваших других годовых премий: "
        prompt_HELP            = " (ВВОДИТЕ ТОЛЬКО ЦИФРЫ!!!!!!!!)"
        
        ### СБОР ДАННЫХ У ПОЛЬЗОВАТЕЛЯ + ПРОВЕРКА:
        
        # 1. salary (оклад)
        current_prompt = prompt_salary
        while True:
            try:
                salary = int(input(current_prompt))
                break
            except ValueError:
                current_prompt = f"{prompt_salary}{prompt_HELP}"
        
        # 2. bonus (премия) - ИСПРАВЛЕНО: записываем в переменную bonus
        current_prompt = prompt_bonus
        while True:
            try:
                bonus = int(input(current_prompt))
                break
            except ValueError:
                current_prompt = f"{prompt_bonus}{prompt_HELP}"
        
        # 3. quarterly_bonus (квартальная) - ИСПРАВЛЕНО: выровнен отступ и пишем в quarterly_bonus
        current_prompt = prompt_quarterly_bonus
        while True:
            try:
                quarterly_bonus = int(input(current_prompt))
                break
            except ValueError:
                current_prompt = f"{prompt_quarterly_bonus}{prompt_HELP}"
        
        # 4. salary_13 (13-я ЗП) - ИСПРАВЛЕНО: выровнен отступ и пишем в salary_13
        current_prompt = prompt_salary_13
        while True:
            try:
                salary_13 = int(input(current_prompt))
                break
            except ValueError:
                current_prompt = f"{prompt_salary_13}{prompt_HELP}"
        
        # 5. other_bonus (другие доходы) - ИСПРАВЛЕНО: записываем в other_bonus
        current_prompt = prompt_other_bonus
        while True:
            try:
                other_bonus = int(input(current_prompt))
                break
            except ValueError:
                current_prompt = f"{prompt_other_bonus}{prompt_HELP}"
    
        # Отправляем данные в расчетную функцию
        result_data = calculate_salary_metrics(salary, bonus, quarterly_bonus, salary_13, other_bonus)
    
        # Передаем этот словарь в функцию печати
        print_report(result_data)
        
        # Чтобы консоль не закрывалась
        input("\nНажмите Enter для выхода из калькулятора зарплаты...")
    
    main()

# основная логика программы
def main():

    # создание словаря (блокнота) (по дефолту при запуске программы он пустой)
    list_tasks = load_tasks()
    
    # запускаем цикл
    while True:
        
        # показывает на экране мейн меню
        main_menu.run()
            
        # запрашивает у пользователя действие
        input_user = input("Выберите действие (0-4): ").lower().strip()
    
        if input_user not in ["1", "2", "3", "4", "0"]:
            print("Ошибка! Выберите действие которое хотите совершить (для этого нужно написать 1 число: 1, 2, 3, 4 или 0)")
            input("\nНажмите Enter для выхода в главное меню... ")
            continue
            
        # если 1 то показывает весь список блокнота
        elif input_user == "1":

            # вызвать блок 
            show_tasks_1(list_tasks)
        
        # если 2 делает так чтобы в список была внесена новая задача в конец списка, после чего показывает весь список.
        elif input_user == "2":

            # вызвать блок
            adding_task_2(list_tasks)

        # если 3 показывает список задач и спрашивает какую конкретно задачу удалить (выбрать цифрами так же) после чего удаляет и возвращает в меню
        elif input_user == "3":

            # вызвать блок 
            block_delete_3(list_tasks)

            continue
        
        # если 4 то открывает минипрограммку , высчитывающую среднюю зп за минуту секунду и тп
        elif input_user == "4":
            calculate_salary_4()
            continue
        
        # если 0 выходит из программы
        elif input_user == "0":
            print("Программа успешно закрыта!")
            break
        
        else:
            continue

# начать исполнять программу
main()