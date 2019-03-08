"""
Definite the data structure
"""


class Edges:
    def __init__(self, id, distance, time, index=0):
        self.id = id
        self.distance = distance
        self.time = time
        self.index = index
        self.left = None
        self.right = None
        self.parent = None