class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def find_max_value(node):
    current = node
    while current.right:
        current = current.right
    return current.val


def find_min_value(node):
    current = node
    while current.left:
        current = current.left
    return current.val


def find_sum_value(node):
    left = find_sum_value(node.left) if node.left else 0
    right = find_sum_value(node.right) if node.right else 0

    return node.val + left + right


# Приклад використання:
root = None
keys = [20, 10, 30, 5, 15, 25, 35, 20]

for key in keys:
    root = insert(root, key)

print("Дерево:")
print(root)

max_value = find_max_value(root)
print("Найбільше значення у дереві:", max_value)

min_value = find_min_value(root)
print("Найменше значення у дереві:", min_value)

sum_value = find_sum_value(root)
print("Сума значень у дереві:", sum_value)
