import AnswerOfTask

_array = []
file = open("input01.txt", "r")
for line in file:
    line = line.rstrip('\n').split()
    line = [float(el) for el in line]
    _array.append(line)
n = len(_array)
out = AnswerOfTask.Lines(_array)
print(out[0], out[1], out[2], sep="\n")
file2 = open("output.txt", "w")
file2.write(','.join(map(str, out)))
file2.close()

