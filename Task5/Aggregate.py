import abc


class Aggregate(abc.ABC):

    @abc.abstractmethod
    def iterator(self):
        """
        Возвращает итератор
        """
        pass
