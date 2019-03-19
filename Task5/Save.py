from ListCollection import ListCollection
from Decorator import SavingFile


@SavingFile
def Save(_dict, filename):
    file2 = open(filename, "w", encoding="Utf-8")
    aggregate = ListCollection(_dict)
    itr = aggregate.iterator()
    while True:
        try:
            itr.next()
            print(itr.current())
            file2.write(itr.current() + "\n")
        except StopIteration:
            break
    file2.close()
