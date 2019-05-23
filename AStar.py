import datetime

from LoadData import LoadData
from Heap import Heap
from Edges import Edges


class AStar:
    """
    # test data in full road network
    # 0=>49;0->1->3->4->6->8->10->13->17->24->28->35->47->49;1616.7403550000001;642.211637
    """

    def __init__(self, src, dst, dtype, location, dimension):
        self.src = int(src)
        self.dst = int(dst)

        self.org_node = LoadData.load_org_node(location)
        self.org_path = LoadData.load_org_path(location, dimension)
        self.link_table = LoadData.load_linking_table(location)
        # print('org_node', self.org_node)
        # print('org_path', self.org_path)
        # print('self.link_table', self.link_table)

        self.heap = Heap(dtype)
        self.quadrant = self.__get_quadrant(self.src, self.dst)
        # print('<---quadrant--->', self.quadrant)

    def algorithm(self):
        """
        Algorithm， 每次將維度數值最小的路徑去做延伸
        設定查詢時間條件 180 秒
        :return:
        """
        start_time = datetime.datetime.now()
        self.heap.insert(Edges((self.src,), 0, 0))
        while True:
            end_time = datetime.datetime.now()
            if (end_time - start_time).seconds >= 60:
                # print('(', self.src, self.dst, ')搜尋時間超出3分鐘--->')
                return []

            root = self.heap.extract_max()
            if not bool(root):
                return []
            else:
                # print('root.id', root.id)
                node_path = root.id
                check_point = node_path[-1]
                if check_point == self.dst:
                    return root
                else:
                    if not self.link_table.__contains__(check_point):
                        return []
                    else:
                        for element in self.link_table[check_point]:
                            if element in node_path:
                                continue
                            if self.quadrant != self.__get_quadrant(self.src, element):
                                continue
                            else:
                                self.heap.insert(self.__concat_edges(root, element))

    def __get_quadrant(self, x, y):
        """
        紀錄相對位置
        判斷下一步走的節點方向是否正確
        :param x:
        :param y:
        :return: 象限
        """
        x_data = self.org_node[x]
        y_data = self.org_node[y]
        coordinate = [y_data[0]-x_data[0], y_data[1]-y_data[1]]
        if coordinate[0] > 0 and coordinate[1] >= 0:
            quadrant = 1
        elif coordinate[0] <= 0 and coordinate[1] > 0:
            quadrant = 2
        elif coordinate[0] < 0 and coordinate[1] <= 0:
            quadrant = 3
        elif coordinate[0] >= 0 and coordinate[1] < 0:
            quadrant = 4
        else:
            quadrant = -1
            # print('<---Quadrant Error--->')
        return quadrant

    def __concat_edges(self, edge, node):
        """
        Connect the path
        :param path:
        :param edge:
        :return:
        """
        if not bool(node):
            return edge
        else:
            pid = edge.id + (node, )
            try:
                dist = self.org_path[(pid[-2], pid[-1])][0]
                tim = self.org_path[(pid[-2], pid[-1])][1]
            except KeyError:
                dist = self.org_path[(pid[-1], pid[-2])][0]
                tim = self.org_path[(pid[-1], pid[-2])][1]
            p_dist = edge.distance + dist
            p_time = edge.time + tim
            return Edges(pid, p_dist, p_time)

    @staticmethod
    def show(data):
        for e in data:
            print(e.id)
            print(e.distance)
            print(e.time)
            print('------------------')


