import json


def _sum(j, dict_predicate):
    def int_or_zero(s):
        try:
            return int(s)
        except ValueError:
            return 0

    if type(j) == dict:
        if dict_predicate(j):
            a = sum([int_or_zero(i) for i in j.keys()])
            b = sum([_sum(i, dict_predicate) for i in j.values()])
            return a + b
        else:
            return 0
    elif type(j) == list:
        return sum([_sum(i, dict_predicate) for i in j])
    else:
        return int_or_zero(j)

j = json.loads(input())
print(_sum(j, lambda d : d))
print(_sum(j, lambda d : not ('red' in d.values())))
