#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
	"""method that determines if all the boxes can be opened."""
	num_boxes = len(boxes)
	keys = [0]
	for key in keys:
		key_in_box = boxes[key]
		for key in key_in_box:
			if key not in keys and key < num_boxes:
				keys.append(key)
	else:
		if len(keys) < num_boxes:
			return False
	return True
