import sys
import random
import timeit
import multiprocessing as mp

from AStar import Astar
from LoadData import LoadData
from Export import Export

"""
Implement the a-star-algorithm to find the path
Enter the src and dst to get the different results
"""


# def test(src, dst):
#     """
#     測試 A* 演算法
#     單起點，單終點
#     :param src: 起點節點名稱
#     :param dst: 終點節點名稱
#     :return: 路徑 ID
#     """
#     algorithm = Astar(src, dst, dimension_type, location, dimension)
#     path = algorithm.algorithm()
#     if not bool(path):
#         data = []
#         print('data', data)
#     else:
#         data = path
#         print('data', data.id)


def job(data, all_node, name):
    """
    多起點多終點的 A* 路徑查詢
    # 加入只搜尋部分的條件
    # 原始的查詢為 n**n 次
    # 現在改為 n**50
    # 並加入時間的條件，超過搜尋時間捨棄此查詢
    :param data: 起點陣列
    :param all_node:終點陣列
    :param name: 多線程的編號
    :return:
    """
    print('<---Processing ' + str(name) + ' start--->')
    # 基本設定
    city = 'California'
    # dimemsion = ["Distance", "Time"]
    dimension = "Distance"
    adjacency_list = LoadData.load_linking_table(location)
    found_pair = LoadData.load_found_pair(city)
    count = 0
    byte_limit = 1024
    full_path = []

    # limited_number = 5
    # sub_all_node = random.sample(all_node, limited_number)

    for src in data:
        for dst in all_node:
            if src == dst:
                continue
            if (src, dst) in found_pair:
                continue

            algorithm = Astar(src, dst, city, dimension, adjacency_list)
            # path = algorithm.algorithm(
            algorithm.query()
            path = algorithm.get_shortest_path()
            if not bool(path):
                continue
            full_path.append(tuple(path))

        # 輸出檔案，依檔案大小分檔案
        if sys.getsizeof(full_path) >= byte_limit:
            Export.export_a_star(full_path, dimension, city, count)
            count += 1
            full_path = []
        else:
            continue
        print('<---Block', src, '--->')
    print('<---End with ' + str(name), '--->')


if __name__ == '__main__':
    """
    Parameter
    location = ['Oldenburg', 'California', 'North America']
    dimension_type = ['distance', 'time']
    Use the multiprocessing to run code
    """
    dimension = 2

    # location = 'Oldenburg'
    location = 'California'
    # location = 'North America'

    # dimension_type = 'distance'
    # dimension_type = 'time'

    org_node = LoadData.load_org_node(location)
    node = list(org_node.keys())
    print('終點數量', len(node))

    # data_set1, data_set2, data_set3, data_set4, data_set5, data_set6, \
    # data_set7, data_set8, data_set9, data_set10 = ([] for _ in range(10))

    data_set1 = node[0: 1000]
    # data_set2 = node[1000: 2000]
    # data_set3 = node[2000::]
    # data_set4 = node[6000: 8000]
    # data_set5 = node[8000: 10000]
    # data_set6 = node[10000: 12000]
    # data_set7 = node[12000: 14000]
    # data_set8 = node[14000: 16000]
    # data_set9 = node[16000: 18000]
    # data_set10 = node[18000::]

    p1 = mp.Process(target=job, args=(data_set1, node, 1))
    # p2 = mp.Process(target=job, args=(data_set2, node, dimension_type, location, dimension, 2))
    # p3 = mp.Process(target=job, args=(data_set3, node, dimension_type, location, dimension, 3))
    # p4 = mp.Process(target=job, args=(data_set4, node, dimension_type, location, dimension, 4))
    # p5 = mp.Process(target=job, args=(data_set5, node, dimension_type, location, dimension, 5))
    # p6 = mp.Process(target=job, args=(data_set6, node, dimension_type, location, dimension, 6))
    # p7 = mp.Process(target=job, args=(data_set7, node, dimension_type, location, dimension, 7))
    # p8 = mp.Process(target=job, args=(data_set8, node, dimension_type, location, dimension, 8))
    # p9 = mp.Process(target=job, args=(data_set9, node, dimension_type, location, dimension, 9))
    # p10 = mp.Process(target=job, args=(data_set10, node, dimension_type, location, dimension, 10))

    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
    # p7.start()
    # p8.start()
    # p9.start()
    # p10.start()

    p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
    # p8.join()
    # p9.join()
    # p10.join()
