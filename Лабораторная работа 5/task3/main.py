import random
def get_unique_list_numbers() -> list[int]:
    x = [i for i in range(-10,11)]
    random.shuffle(x)
    return(x[:15])




list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
