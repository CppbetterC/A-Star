from Edges import Edges


class Heap:

    def __init__(self, dimension_type):
        self.heapTree = {}
        self.dimension_type = dimension_type

    def insert(self, data):
        index = self.tree_size + 1
        if index > 1:
            parent_index = int(index / 2)
            new_node = Edges(data.id, data.distance, data.time, index)
            self.heapTree[index] = new_node
            if new_node.index == 2 * self.heapTree[parent_index].index:
                self.heapTree[parent_index].left = new_node
            else:
                self.heapTree[parent_index].right = new_node
            new_node.parent = self.heapTree[parent_index]

            while True:
                if self.cal_weight(self.heapTree[index]) < self.cal_weight(self.heapTree[parent_index]):
                    self.__swap(self.heapTree, index, parent_index)
                    index = parent_index
                    parent_index = int(parent_index / 2)
                    if parent_index == 0:
                        break
                else:
                    break
        else:
            self.heapTree[index] = data

    def extract_max(self):
        index = self.tree_size
        if index <= 0:
            return None
        self.__swap(self.heapTree, 1, index)
        edge = self.heapTree[1]
        self.heapTree.pop(index)
        self.__heapify(self.heapTree, 1, len(self.heapTree))
        return edge

    def cal_weight(self, data):
        if 'distance' in self.dimension_type:
            return data.distance
        if 'time' in self.dimension_type:
            return data.time
        if 'distance' in self.dimension_type and 'time' in self.dimension_type:
            return data.distance + data.time
        raise Exception('<---Dimension Error--->')

    def __heapify(self, data, root, length):
        left_child = 2 * root
        right_child = 2 * root + 1
        # min_node = -1
        if left_child < length and self.cal_weight(data[left_child]) < self.cal_weight(data[root]):
            min_node = left_child
        else:
            min_node = root

        if right_child < length and self.cal_weight(data[right_child]) < self.cal_weight(data[min_node]):
            min_node = right_child

        if min_node != root:
            Heap.__swap(data, root, min_node)
            self.__heapify(data, min_node, length)

    @staticmethod
    def __swap(data, x, y):
        if x != y:
            data[x], data[y] = data[y], data[x]

    @property
    def tree_size(self):
        return len(self.heapTree)
