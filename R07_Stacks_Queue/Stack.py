
class Stack:
    #content: list[object] = []

    def __init__(self, content: list[object]) -> None:
        self.content: list[object] = content

    def insert(self, item: object) -> None:
        self.content.append(item)

    def expulse(self) -> None:
        self.content.pop()

    def __str__(self):
        for i in self.content:
            print(i)

    def last(self) -> str:
        return str(self.content[-1])

    def length(self) -> int:
        return len(self.content)
