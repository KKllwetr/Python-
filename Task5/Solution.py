import Searching
import itertools
from Save import Save

_array = []
file = open("Answer.txt", "r", encoding="Utf-8")
for line in file:
    line = line.rstrip('\n').split()
    _array.append(line)
merged = list(itertools.chain(*_array))
_dict = []
_dict = Searching.SearchQuestions(merged)
Save(_dict,"output.txt")



