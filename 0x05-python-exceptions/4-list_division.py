#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    y = 0
    for i in range(0, list_length):
        try:
            y = my_list_1[i] / my_list_2[i]
        except TypeError:
            y = 0
            print("wrong type")
        except ZeroDivisionError:
            y = 0
            print("division by 0")
        except IndexError:
            y = 0
            print("out of range")
        finally:
            pass
        x.append(y)
    return x
