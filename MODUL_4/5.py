class node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def cari(self, dicari):
        curNode = self
        while curNode is not None:
            if curNode.next is not None:
                if curNode.data != dicari:
                    curNode = curNode.next
                else:
                    print ("Data ", dicari, "ada dalam linked list")
                    break
            elif curNode.next is None:
                print ("Data ", dicari, "tidak ada dalam linked list")
                break
