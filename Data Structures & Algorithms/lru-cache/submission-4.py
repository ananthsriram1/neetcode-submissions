class ListNode:
    def __init__(self, key: None, val: None):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}

        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        new_next = self.right
        new_prev = self.right.prev

        node.next = new_next
        node.prev = new_prev

        new_next.prev = node
        new_prev.next = node

    def remove(self, node):
        new_prev = node.prev
        new_next = node.next

        new_prev.next = new_next
        new_next.prev = new_prev
        

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        
        node = self.mapping[key]
        rv = node.val

        self.remove(node)
        self.insert(node)

        return rv

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
        elif len(self.mapping) == self.capacity:
            self.mapping.pop(self.left.next.key, None)
            self.remove(self.left.next)
            
        new_node = ListNode(key, value)
        self.insert(new_node)
        self.mapping[key] = new_node
