
class LinkedListAbc:


    def __init__(self):
        self.ll = list()

    def add_new(self, val):


        tmp = [val, None]
        if len(self.ll) == 0:
            self.ll.append(tmp)
        else:
            new_add = len(self.ll)
            self.ll[-1][-1] = new_add
            self.ll.append(tmp)

    def get(self):
        # print(self.ll)
        tmp = []
        for i in self.ll:
            tmp.append(i[0])
        return tmp


if __name__ == '__main__':

    obj = LinkedListAbc()

    obj.add_new(5)
    obj.add_new(15)
    obj.add_new(51)
    obj.add_new(50)

    # print(obj.get())


