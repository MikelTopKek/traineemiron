import abc


class Human(abc.ABC):

    @abc.abstractmethod
    def think(self):
        pass

    def walk(self):
        pass


class Man(Human):
    def think(self):
        pass


class Woman(Human):
    def think(self):
        pass


woman = Woman()
man = Man()
people = [woman, man]
...
for p in people:
    p.think()
    p.walk()
