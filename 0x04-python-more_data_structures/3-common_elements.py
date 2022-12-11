#!/usr/bin/python3
def common_elements(set_1, set_2):
    for k in set_1:
        for v in set_2:
            if k == v:
                return (k)
