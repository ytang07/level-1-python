class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def append(self, value):
        while self.next is not None:
            self = self.next
        self.next = Node(value)

    def print_nodes(self):
        while self.next is not None:
            print(self.value, end=" ")
            self = self.next
        print(self.value)
    
    # keep track of min and parent
    # while parent has next
    # # if next value is 
    def find_min(self):
        if self.next is None:
            return self, self
        min = self
        parent = None
        while self.next is not None:
            if self.next.value < min.value:
                parent = self
                min = self.next
            self = self.next
        return parent, min
    
    # find minimum and parent
    # point parent.next to min.next if it exists
    # point min.next to original root
    def remove_min(self):
        parent, min = self.find_min()
        if parent is None:
            self = min.next
            min.next = None
            return self, min

        if min.next is not None:
            parent.next = min.next
            min.next = None
        else:
            parent.next = None
            min.next = None
        return self, min

# 1. remove minimum and put it into a new linked list
# 2. repeat 1 until original linked list no longer exists
def sort_nodes(root: Node):
    new_list, min = root.remove_min()
    new_root = min
    while new_list.next is not None:
        new_list, min = new_list.remove_min()
        new_root.append(min.value)
    new_root.append(new_list.value)
    return new_root

root = Node(8)
root.append(4)
root.append(2)
root = sort_nodes(root)
root.print_nodes()

root.append(1)
root.append(5)
root = sort_nodes(root)
root.print_nodes()

root.append(7)
root = sort_nodes(root)
root.print_nodes()
