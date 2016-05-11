class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert_helper(new_val,self.root)

    def _insert_helper(self,new_val,current):
        if new_val > current.value:
            if current.right:
                self._insert_helper(new_val,current.right)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self._insert_helper(new_val,current.left)
            else:
                current.left = Node(new_val)




    def search(self, find_val):
        return self._search_helper(find_val,self.root)

    def _search_helper(self,value,current):
        if current:
            if value == current.value:
                return True
            elif value < current.value:
                return self._search_helper(value,current.left)
            else:
                return self._search_helper(value,current.right)
        else:
            return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
