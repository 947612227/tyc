class Test():
    def func(self, l):
        i = 0
        l_1 = []
        while i < len(l):
            temp = l[i]
            temp = temp[::-1]
            i += 1
            l_1.append(temp)
        j = 0
        while j < len(l_1):
            z = 0
            while z < len(l_1[0]):
                if l_1[j][z] is 0:
                    l_1[j][z] = 1
                else:
                    l_1[j][z] =0
        return l_1


if __name__ == "__main__":
    l = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    t = Test()
    print (t.func(l))

if __name__ == '__main__':
    t = Test()
    print(t.func())