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
    opended = [False] * n  # assume all boxes are opended
    opended[0] = True  # first box is opened
    keys = boxes[0]  # the first key

    for key in keys:
        if not opended[key]:
            opended[key] = True
            keys.extend(boxes[key])

    return all(opended)
