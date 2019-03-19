import AnswerOfTask

_array = []
file = open("input01.txt", "r")
for line in file:
    line = line.rstrip('\n').split()
    line = [int(el) for el in line]
    _array.append(line)
n = len(_array)
s = set()
for i in range(n - 1):
    for j in range(i+1,n):
        select = AnswerOfTask.Intersect(_array[i], _array[j])
        if select is False:
            s.add(j)
_new_array = _array[:]
for i in s:
    _new_array.pop(i)
print(_array)
file2 = open("output.txt", "w")
file2.write(','.join(map(str,_new_array)))
file2.close()
print(_new_array)

