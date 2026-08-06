from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @abstractmethod
    def display(self):
        pass