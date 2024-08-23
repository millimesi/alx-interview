#!/usr/bin/python3
""" LockBoxes question solution"""


def canUnlockAll(boxes):
    '''
    finds out if all boxes can be opened or not
    Args:
        boxes(List[List]): list of boxes with keys
    return:
        bool: true if all can be opened or false
    '''
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        box = keys.pop()
        for each in boxes[box]:
            if each >= 0 and each < n and not opened[each]:
                opened[each] = True
                keys.append(each)

    return all(opened)
