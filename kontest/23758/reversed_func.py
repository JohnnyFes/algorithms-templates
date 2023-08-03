def solution(node):
    index = 0
    while node and index < 1000:
        next_item = node.next
        node.next = node.prev
        node.prev = next_item
        if next_item is None:
            return node
        node = node.prev
        index += 1
