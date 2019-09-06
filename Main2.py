"""
Additional script (For Find the shortest path on the road network )
"""

import sys
import numpy as np
import pandas as pd
import random
import timeit
import multiprocessing as mp

from sklearn.metrics.pairwise import euclidean_distances

from AStar import Astar
from LoadData import LoadData
from Export import Export


def calculate_heuristic(city):
    """
    計算 heuristic matrices
    :param city:
    :return:
    """
    org_node = LoadData.load_org_node(city)
    data = np.array(list(org_node.values()))
    result = euclidean_distances(data, data)
    header = [x for x in list(org_node.keys())]
    pd_data = pd.DataFrame(result, columns=header)
    # print(pd_data.shape)
    return pd_data


def job(data, city, dimension, heuristic_matrices, pname):
    """
    :param data: 起點陣列
    :param heuristic_matrices:
    :param pname: 多線程的編號
    :return:
    """
    print('<---Processing ' + str(pname) + ' start--->')

    adjacency_list = LoadData.load_linking_table(city)
    count = 0
    byte_limit = 1024 * 20
    full_path = []

    for (src, dst) in data:
        if src != dst:
            algorithm = Astar(src, dst, city, dimension, adjacency_list, heuristic_matrices)
            algorithm.query()
            path = algorithm.get_shortest_path()
            if bool(path):
                full_path.append(tuple(path))

            # 輸出檔案，依檔案大小分檔案
            if sys.getsizeof(full_path) >= byte_limit:
                Export.export_a_star(full_path, dimension, city, count)
                count += 1
                full_path = []

    print('<---End with ' + str(pname), '--->')


if __name__ == '__main__':
    # 基本設定
    """
    # 基本設定
    # Dimension: 目前執行的實驗有多少維度
    # city: 城市名稱(Oldenburg, California, North America)

    1. 要改地點(city)和維度名稱(dimension)
    2. 資料數量的分配情況

    """

    # 載入路網節點
    city = 'Oldenburg'
    node = list(LoadData.load_org_node(city).keys())
    heuristic_matrices = calculate_heuristic(city)
    print('終點數量', len(node))

    # 要重新收集的最段路徑維度資料(要修改)
    # file_name = ['NotFoundNode(Distance)', 'NotFoundNode(Time)',
    #              'NotFoundNode(Dimension3)', 'NotFoundNode(Dimension4)',
    #              'NotFoundNode(Dimension5)', 'NotFoundNode(Dimension6)']

    """
    # 基本設定
    dimension = [Distance, TIme, Dimension3, Dimension4, Dimension5, Dimension6]
    dimension 需要改
    """
    dimension = "Time"
    file_name = 'data/Oldenburg/NotFoundNode/NotFoundNode(' + dimension + ').txt'

    not_found_node = LoadData.load_not_found_node(file_name)
    number = len(not_found_node)
    print('number->', number)
    # x=input('Check')

    data_set1 = not_found_node[0: 474213]
    data_set2 = not_found_node[474213: 948427]
    data_set3 = not_found_node[948427: 1422641]
    data_set4 = not_found_node[1422641: 1896855]
    data_set5 = not_found_node[1896855: 2371068]
    data_set6 = not_found_node[2371068: 2845282]
    data_set7 = not_found_node[2845282: 3319496]
    data_set8 = not_found_node[3319496::]
    # data_set9 = not_found_node[3372186::]
    # data_set10 = not_found_node[3414339::]

    # 加入多線程排程
    p1 = mp.Process(target=job, args=(data_set1, city, dimension, heuristic_matrices, 1))
    p2 = mp.Process(target=job, args=(data_set2, city, dimension, heuristic_matrices, 2))
    p3 = mp.Process(target=job, args=(data_set3, city, dimension, heuristic_matrices, 3))
    p4 = mp.Process(target=job, args=(data_set4, city, dimension, heuristic_matrices, 4))
    p5 = mp.Process(target=job, args=(data_set5, city, dimension, heuristic_matrices, 5))
    p6 = mp.Process(target=job, args=(data_set6, city, dimension, heuristic_matrices, 6))
    p7 = mp.Process(target=job, args=(data_set7, city, dimension, heuristic_matrices, 7))
    p8 = mp.Process(target=job, args=(data_set8, city, dimension, heuristic_matrices, 8))
    # p9 = mp.Process(target=job, args=(data_set9, city, dimension, heuristic_matrices, 9))
    # p10 = mp.Process(target=job, args=(data_set10, city, dimension, heuristic_matrices, 10))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    # p9.start()
    # p10.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    # p9.join()
    # p10.join()
