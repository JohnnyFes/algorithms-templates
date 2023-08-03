def solution(node, idx):
    index = 0
    prev_item = head = node
    if idx == 0:
        head = head.next_item
    else:
        while node and index < 5000:
            if index == idx:
                prev_item.next_item = node.next_item
                break
            prev_item = node
            node = node.next_item
            index += 1
    return head
