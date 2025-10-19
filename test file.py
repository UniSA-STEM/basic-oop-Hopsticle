class Hacker:
    def __init__(self):
        self.list = ['cat','dog']
        test = self.list
class New:
    def __init__(self):
        self.list2 = Hacker.test.copy()
        return 'list2'


print(New)

