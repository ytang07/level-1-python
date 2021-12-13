class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class Linked_List(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    
    # append at the end
    def append(self, node):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        self.size += 1
    
    def size(self):
        return self.size
    
    def search(self, value):
        cur = self.head
        found = False
        while not found:
            if cur.data == value:
                found = True
                return cur
            elif cur.next:
                cur = cur.next
            else:
                return ValueError("Value not found")
        
    def delete(self, value):
        cur = self.head
        if cur.data == value:
            self.head = cur.next
        else:
            while cur.data != value:
                cur = cur.next
            if cur.next:
                cur.data = cur.next.data
                cur.next = cur.next.next
            else:
                cur.next = None
                cur.data = None
                    

    def traverse(self):
        cur = self.head
        arr = [cur.data]
        while cur.next:
            cur = cur.next
            arr.append(cur.data)
        return arr

node1 = Node(4)
node2 = Node(2)
node3 = Node(6)
node4 = Node(10)
node5 = Node(5)
ll = Linked_List(node1)
print(f"Current linked list is {ll.traverse()}")
ll.append(node2)
ll.append(node3)
print(f"After adding some nodes, we get {ll.traverse()}")
print(f"Now the size of the linked list is {ll.size}")
print(f"If we search for 10, we should see that it is not in the list: {ll.search(10)}")
ll.append(node4)
ll.append(node5)
print(f"However if we append some nodes, and one of them has value 10 like: {ll.traverse()}")
print(f"We should now get a response for searching for 10: {ll.search(10)}")
ll.delete(2)
print(f"After deleting node 2, we get {ll.traverse()}")