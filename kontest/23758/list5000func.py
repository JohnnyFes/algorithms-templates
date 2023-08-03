def solution(node):
    count = 0
    while node and count < 5000:
        print(node.value)
        node = node.next_item
        count += 1
