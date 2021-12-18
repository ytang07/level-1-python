# val is the value of the node
# right is the right node
# left is the left node
class BinaryTree(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def append_val(self, val):
        self.append(BinaryTree(val))

    def append(self, node):
        _val = node.val
        if _val <= self.val:
            if self.left:
                print(f"moving left to append {_val}")
                self.left.append(node)
            else:
                print(f"setting left {_val}")
                self.left = node
        else:
            if self.right:
                print(f"moving right to append {_val}")
                self.right.append(node)
            else:
                print(f"setting right {_val}")
                self.right = node
        
    def search(self, val):
        if val == self.val:
            return True
        if val <= self.val and self.left:
            self.left.search(val)
        elif val > self.val and self.right:
            self.right.search(val)
        else:
            print("Value could not be found")
            return False
    
    # returns the parent node and the successor
    def find_successor(self, parent):
        if self.left:
            return self.left.find_successor(self)
        else:
            return parent, self
    
    def delete(self, val):
        print(f"Deleting {val} if it exists")
        if self.val == val:
            if self.right and self.left:
                parent, successor = self.right.find_successor(self)
                # split out the successor
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                # reset left and right nodes of the successor
                successor.left = self.left
                successor.right = self.right
                return successor
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if self.val > val:
                if self.left:
                    self.left = self.left.delete(val)
            else:
                if self.right:
                    self.right = self.right.delete(val)
        return self
    
    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(self.val)
        if self.right:
            self.right.inorder_print()

root = BinaryTree(5)
root.inorder_print()
print('\n')
root.append_val(2)
root.append_val(8)
root.append_val(3)
root.inorder_print()
print('\n')
root.append_val(1)
root.append_val(10)
root.append_val(7)
root.inorder_print()
root = root.delete(5)
root.inorder_print()