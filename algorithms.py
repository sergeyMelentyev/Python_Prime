import random
from time import time

"""BINARY SEARCH ORDERED COLLECTION ONLY"""


def classic_search(collection, target):
    """Determine whether collection contains target"""
    return target in collection


def classic_insert(collection, target):
    """Insert target into it proper location"""
    for i in range(len(collection)):
        if target < collection[i]:
            collection.insert(i, target)
            return
        collection.append(target)


def binary_search(collection, target):
    """Use binary array search to determine if target is in collection"""
    low = 0
    high = len(collection) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == collection[mid]:
            return True
        elif target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_contains_for_insert(collection, target):
    """Use binary array search to return index position of target in collection"""
    low = 0
    high = len(collection) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == collection[mid]:
            return mid
        elif target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -(low + 1)


def binary_insert(collection, target):
    """Inserts target into it proper location"""
    idx = binary_contains_for_insert(collection, target)
    if idx < 0:
        collection.insert(-(idx + 1), target)
        return
    collection.insert(idx, target)


def performance_binary_search():
    """Demonstrate execution performance of contains"""
    n = 1
    while n < 50000000:
        sorted_list = list(range(n))
        now = time()
        # classic_search(sorted_list, -1)
        # binary_search(sorted_list, -1)
        # classic_insert(sorted_list, n + 1)
        binary_insert(sorted_list, n + 1)
        done = time()
        print(n, (done-now)*1000)
        n *= 2

# performance_binary_search()


"""BINARY TREE DATA STRUCTURE"""


class BinaryNode:
    def __init__(self, value=None):
        """Create binary tree"""
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        """Adds a new node to the tree containing this value"""
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)


class BinaryTree:
    def __init__(self):
        """Create empty binary tree"""
        self.root = None

    def add(self, value):
        """Insert value into proper location in Binary Tree"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        """Check whether Binary Search Tree contains target value"""
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False


def performance_binary_tree():
    """Demonstrate execution performance of contains"""
    n = 1024
    while n <= 500000:
        bt = BinaryTree()
        for i in range(n):
            bt.add(random.randint(1, n))
        now = time()
        bt.contains(random.randint(1, n))
        print(n, (time() - now)*1000)
        n *= 2


# performance_binary_tree()

