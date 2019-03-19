import Searching
import itertools

_array = []
file = open("Answer.txt", "r", encoding="Utf-8")
for line in file:
    line = line.rstrip('\n').split()
    _array.append(line)
merged = list(itertools.chain(*_array))
_dict ={}
_dict = Searching.SearchQuestions(merged)
file2 = open("output.txt", "w", encoding="Utf-8")
for i in _dict.values():
    file2.write(i+"\n")
file2.close()
for i in _dict.values():
    print(i+"\n")
