class Tree:
    def grow(self) -> None:
        print("grow tree")


class Child:
    def born(self) -> None:
        print("born child")


class House:
    def build(self) -> None:
        print("build house")


class TheMenFacade:

    def __init__(self):
        self._tree = Tree()
        self._child = Child()
        self._house = House()

    def grow_tree(self) -> None:
        self._tree.grow()

    def born_child(self):
        self._child.born()

    def build_house(self):
        self._house.build()


if __name__ == '__main__':
    facade = TheMenFacade()
    facade.born_child()
    facade.build_house()
    facade.grow_tree()
