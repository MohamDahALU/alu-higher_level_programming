#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
            new_list.append(num)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except (TypeError, ValueError):
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
            break

    return new_list
