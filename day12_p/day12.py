import json


def _sum(j):
    def int_or_zero(s):
        try:
            return int(s)
        except ValueError:
            return 0

    if type(j) == dict:
        a = sum([int_or_zero(i) for i in j.keys()])
        b = sum([_sum(i) for i in j.values()])
        return a + b
    elif type(j) == list:
        return sum([_sum(i) for i in j])
    else:
        return int_or_zero(j)


print(_sum(json.loads(input())))
