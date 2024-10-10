#!/usr/bin/python3
'''A module for working with lockboxes.'''


def canUnlockAll(boxes):
    """ Cheks if all the boxes can be opened, and
    Returns True if it does or False if not
    """

    n = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0])

    while keys:

        key = keys.pop()

        if key < n and key not in unlocked_boxes:

            unlocked_boxes.add(key)
            keys.update(boxes[key])

    return len(unlocked_boxes) == n
