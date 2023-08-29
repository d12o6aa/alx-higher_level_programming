#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    v = 0
    for i in range(0, list_length):
        try:
            v = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            v = 0
        except TypeError:
            print("wrong type")
            v = 0
        except IndexError:
            print("out of range")
            v = 0
        finally:
            my_list_3.append(v)
    return my_list_3
