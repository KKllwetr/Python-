import Searching
import itertools

_array = []
file = open("input.txt", "r", encoding="Utf-8")
for line in file:
    line = line.rstrip('\n').split()
    _array.append(line)
merged = list(itertools.chain(*_array))
_list = []
_list = Searching.SearchQuestions(merged)
file2 = open("output.txt", "w", encoding="Utf-8")
for i in _list:
    file2.write(i + "\n")
file2.close()
for i in _list:
    print(i + "\n")
