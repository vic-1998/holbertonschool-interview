#!/usr/bin/python3
"""
canUnlockAll method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
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
