def data_types():

    int_type = 101 #целые числа
    str_type = "Pythonchik" #строки
    float_type = 15.5 #вещественные числа
    bool_type = True #Правда/ложь
    list_type = [1, 2, 3, 4, 5] #список (изменяемый, можно дубли, есть индексация)
    dict_type = {"key": "value"} #словарь (ключ: значение)
    tuple_type = (1, 2, 3, 4, 5) #кортеж (неизменяемый, есть индексация)
    set_type = {1, 2, 3, 4, 5} #множество (изменяемый, уникальные элементы, нет индексации)

    types = [type(int_type).__name__, type (str_type).__name__, type(float_type).__name__, type(bool_type).__name__, type(list_type).__name__, type (dict_type).__name__, type(tuple_type).__name__, type(set_type).__name__]
    # с помощью .__name__ превращаем <class 'int'> в 'int'
    
    formatted_output = f"[{', '.join(types)}]" #убираем кавычки

    print(formatted_output)

if __name__ == '__main__':
    data_types()