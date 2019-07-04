"""
Implement the A stat shortest path algorithm in offline
Use the heap tree to be priority queue
heuristic function is the euclidean distance
"""

import heapq
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import euclidean_distances

from LoadData import LoadData


class Astar:

    def __init__(self, src, dst, city, dimension, adjacency_list):
        self.__src = src
        self.__dst = dst
        self.__city = city

        self.__open_list = []
        self.__closed_list = []
        self.__dimension = self.__dimension_index(dimension)

        self.__org_node = LoadData.load_org_node(city)
        self.__org_path = LoadData.load_org_path(city, 2)

        self.__link_table = adjacency_list
        self.__heuristic = self.__calculate_heuristic()

        self.__dimension_cost, self.__heuristic_cost, self.__total_cost = ({} for _ in range(3))

        self.__dimension_cost = {node: float("inf") for node in self.__org_node.keys()}
        self.__dimension_cost[self.__src] = 0
        self.__heuristic_cost[self.__src] = self.__heuristic.loc[self.__src, self.__dst]
        self.__total_cost[self.__src] = \
            self.__heuristic_cost[self.__src] + self.__heuristic_cost[self.__src]

        self.__previous_node = {self.__src: None}

        heapq.heappush(self.__open_list, (self.__total_cost[self.__src], self.__src))

    def query(self):
        while len(self.__open_list) > 0:
            data = heapq.heappop(self.__open_list)
            expanded = data[-1]

            if expanded == self.__dst:
                return

            self.__closed_list.append(expanded)

            for node in self.__link_table[expanded]:
                if node in self.__closed_list:
                    continue
                try:
                    cost = self.__dimension_cost[expanded] + self.__org_path[(expanded, node)][self.__dimension]
                except KeyError:
                    cost = self.__dimension_cost[expanded] + self.__org_path[(node, expanded)][self.__dimension]

                if cost < self.__dimension_cost[node]:
                    self.__dimension_cost[node] = cost
                    self.__previous_node[node] = expanded
                self.__heuristic_cost[node] = self.__heuristic.loc[node, self.__dst]
                self.__total_cost[node] = self.__dimension_cost[node] + self.__heuristic_cost[node]

                heapq.heappush(self.__open_list, (self.__total_cost[node], node))

        return

    def __calculate_heuristic(self):
        data = np.array(list(self.__org_node.values()))
        result = euclidean_distances(data, data)
        header = [x for x in list(self.__org_node.keys())]
        pd_data = pd.DataFrame(result, columns=header)
        # print(pd_data.shape)
        return pd_data

    @staticmethod
    def __dimension_index(dimension):
        """
        Add others dimension
        :param dimension:
        :return:
        """
        idx = -1
        if dimension == "Distance":
            idx = 0
        elif dimension == "Time":
            idx = 1
        else:
            print('Error')
        return idx

    def get_shortest_path(self):
        result = []
        node = self.__previous_node[self.__dst]
        while not(node is None):
            result = [node] + result
            node = self.__previous_node[node]
        result = result + [self.__dst]
        return result
