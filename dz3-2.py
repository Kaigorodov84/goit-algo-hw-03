import random

def get_numbers_ticket(min, max, quantity):
    number_ticket = []
    if min < 1 or max > 999 or not min <= quantity <= max:
        return number_ticket
    else:
        for i in range(quantity):
            a = random.randint(min, max)
            if a not in number_ticket:
                number_ticket.append(a)
            else:
                i -= 1
                continue
        while(len(number_ticket) < quantity):
            a = random.randint(min, max)
            if a not in number_ticket:
                number_ticket.append(a)
        return number_ticket
print(get_numbers_ticket(1, 49, 6))




