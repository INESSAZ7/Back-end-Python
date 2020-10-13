class MyList(list):
    def __sub__(self, other):
        res = []
        l_self = len(self)
        l_other = len(other)
        min_len = min(l_self, l_other)
        for i in range(max(l_self, l_other)):
            if i < min_len:
                res.append(self[i] - other[i])
            else:
                if l_self < l_other:
                    res.append(0 - other[i])
                elif l_self > l_other:
                    res.append(self[i] - 0)
        return res

    def __add__(self, other):
        res = []
        l_self = len(self)
        l_other = len(other)
        min_len = min(l_self, l_other)
        for i in range(max(l_self, l_other)):
            if i < min_len:
                res.append(self[i] + other[i])
            else:
                if l_self < l_other:
                    res.append(0 + other[i])
                elif l_self > l_other:
                    res.append(self[i] + 0)
        return res

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)


if __name__ == '__main__':
    a = MyList([])
    b = MyList([3,2,4])
    c = MyList([1,2,3])
    d = MyList([9,1])

    print(a < b)
    print(b > d)
    print(a + b)
    print(b - d)
