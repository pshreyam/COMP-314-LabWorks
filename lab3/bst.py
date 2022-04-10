class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.LEFT = None
        self.RIGHT = None


class BinarySearchTree:
    def __init__(self):
        self.ROOT = None
        self.__size = 0

    def size(self):
        return self.__size

    def add(self, key, value):
        new_node = Node(key=key, value=value)
        if not self.ROOT:
            self.ROOT = new_node
        else:
            self.__add(self.ROOT, new_node)
        self.__size += 1

    def __add(self, root, node):
        if not root:
            return

        if node.key < root.key:
            if not root.LEFT:
                root.LEFT = node
                return
            self.__add(root.LEFT, node)
            return
        else:
            if not root.RIGHT:
                root.RIGHT = node
                return
            self.__add(root.RIGHT, node)
            return

    def search(self, key):
        node = self.__search(self.ROOT, key)
        if node:
            return node.value
        return False

    def __search(self, root, key):
        if not root:
            return False
        if key == root.key:
            return root
        elif key < root.key:
            return self.__search(root.LEFT, key)
        else:
            return self.__search(root.RIGHT, key)

    def smallest(self):
        if not self.ROOT:
            return False
        smallest_node = self.__smallest(self.ROOT)
        return (smallest_node.key, smallest_node.value)

    def __smallest(self, root):
        if not root.LEFT:
            return root
        return self.__smallest(root.LEFT)

    def largest(self):
        if not self.ROOT:
            return False
        largest_node = self.__largest(self.ROOT)
        return (largest_node.key, largest_node.value)

    def __largest(self, root):
        if not root.RIGHT:
            return root
        return self.__largest(root.RIGHT)

    def remove(self, key):
        if not self.__search(self.ROOT, key):
            return False
        self.ROOT = self.__remove(self.ROOT, key)
        self.__size -= 1

    def __remove(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.LEFT = self.__remove(root.LEFT, key)
            return root
        elif key > root.key:
            root.RIGHT = self.__remove(root.RIGHT, key)
            return root
        else:
            if not root.LEFT and not root.RIGHT:
                return None
            elif not root.LEFT or not root.RIGHT:
                if root.LEFT:
                    return root.LEFT
                else:
                    return root.RIGHT
            else:
                successor = self.__largest(root.LEFT)
                root.key, root.value = successor.key, successor.value
                root.LEFT = self.__remove(root.LEFT, successor.key)
                return root

    def inorder_walk(self):
        visited_nodes = []
        self.__inorder_walk(self.ROOT, visited_nodes)
        return visited_nodes

    def __inorder_walk(self, root, visited_nodes):
        if not root:
            return
        self.__inorder_walk(root.LEFT, visited_nodes)
        visited_nodes.append(root.key)
        self.__inorder_walk(root.RIGHT, visited_nodes)

    def preorder_walk(self):
        visited_nodes = []
        self.__preorder_walk(self.ROOT, visited_nodes)
        return visited_nodes

    def __preorder_walk(self, root, visited_nodes):
        if not root:
            return
        visited_nodes.append(root.key)
        self.__preorder_walk(root.LEFT, visited_nodes)
        self.__preorder_walk(root.RIGHT, visited_nodes)

    def postorder_walk(self):
        visited_nodes = []
        self.__postorder_walk(self.ROOT, visited_nodes)
        return visited_nodes

    def __postorder_walk(self, root, visited_nodes):
        if not root:
            return
        self.__postorder_walk(root.LEFT, visited_nodes)
        self.__postorder_walk(root.RIGHT, visited_nodes)
        visited_nodes.append(root.key)
