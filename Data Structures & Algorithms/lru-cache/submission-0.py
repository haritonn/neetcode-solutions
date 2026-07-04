class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.value = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.length = 0

    def __len__(self): return self.length

    def push_first(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.length += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None
        self.length -= 1

    def remove_last(self):
        if self.length == 0: return
        last = self.tail.prev
        self.remove(last)
        return last.key

    def change_priority(self, node):
        self.remove(node)
        self.push_first(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.priority = LinkedList()        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.priority.change_priority(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = Node(key, value)
            self.priority.push_first(new_node)
            self.cache[key] = new_node
        else:
            node = self.cache[key]
            node.value = value
            self.priority.change_priority(node)
        if len(self.priority) > self.capacity:
            removed_key = self.priority.remove_last()
            del self.cache[removed_key]
