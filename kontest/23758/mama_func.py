def solution(node, elem):
    index = 0
    while node and index < 5000:
        if node.value == elem:
            return index
        node = node.next_item
        index += 1
    return -1
