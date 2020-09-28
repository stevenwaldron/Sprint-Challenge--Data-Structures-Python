class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def view(self):
        values = []
        currentnode = self.head
        while currentnode != None:
            values.append(str(currentnode.value))
            currentnode = currentnode.next_node
        return '-->'.join(values)
            

    def reverse_list(self,node,prev):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next_node
            current.next_node = prev
            prev = current 
            current = next 
        self.head = prev
        return self.view()

       
       
       
        

LL = LinkedList()
LL.add_to_head(6)
LL.add_to_head(4)
LL.add_to_head(2)
print(LL.view())
print(LL.reverse_list(None,None))


