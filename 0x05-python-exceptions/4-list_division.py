#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []

    for i in range(list_length):
        try:
            nlist.append(my_list_1[i] / my_list_2[i])

        except ZeroDivisionError:
            nlist.append(0)
            print("Division by 0")
            continue

        except TypeError:
            nlist.append(0)
            print("Wrong type")
            continue

        except IndexError:
            nlist.append(0)
            print("out of range")
            continue

        finally:
            pass

    return (nlist)
