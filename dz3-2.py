import random


def get_numbers_ticket(min, max, quantity):
        try:
            quantity > (max - min + 1)
        except Exception:
            print("Кількість чисел  більша за діапазон доступних чисел")
        number_set=set()
        while len(number_set)<quantity:
            random_number = random.randint(min, max)
            number_set.add(random_number)
        return list(number_set)

    # Приклад використання:
min = 1
max = 49
quantity = 6
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
get_numbers_ticket()


