
dict = {}

def get_count_char(str_):
    str_ = str_.lower()
    for i in str_:
        if i.isalpha():
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1


    return dict





main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

new_dict = dict.copy()

def get_percentage_char(new_dict):
    summ = sum(new_dict.values())
    new_dict.values = new_dict.values()
    for value in new_dict.values:
        value = (value/summ) * 100
    return new_dict
print(new_dict)
