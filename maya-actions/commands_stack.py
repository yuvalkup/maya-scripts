class CommandsStack:
    def __init__(self):
        self.list = []
        self.future = [] # a reversed list showing the "future" of the first list

    def push(self, item):
        self.list.append(item)
        self.future.clear()

    def undo(self):
        self.future.append(self.list.pop())

    def redo(self):
        self.list.append(self.future.pop())

    def clear(self):
        self.list.clear()
        self.future.clear()
