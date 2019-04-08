import sys
import multiprocessing as mp

from AStar import AStar
from LoadData import LoadData
from Export import Export

"""
Implement the a-star-algorithm to find the path
Enter the src and dst to get the different results
"""


def test(src, dst):
    algorithm = AStar(src, dst, dimension_type, location, dimension)
    path = algorithm.algorithm()
    if not bool(path):
        data = []
        print('data', data)
    else:
        data = path
        print('data', data.id)


def job(data, all_node, dtype, dlocation, ddimension, name):
    print('<---Processing ' + str(name) + ' start--->')
    count = 0
    byte_limit = 1024 * 1024
    full_path = []
    for src in data:
        for dst in all_node:
            if src == dst:
                continue
            algorithm = AStar(src, dst, dtype, dlocation, ddimension)
            path = algorithm.algorithm()
            if not bool(path):
                continue
            full_path.append(tuple(path.id))
        # 輸出檔案，依檔案大小分檔案
        if sys.getsizeof(full_path) >= byte_limit:
            Export.export_a_star(full_path, dtype, dlocation, count)
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

    dimension_type = 'distance'
    # dimension_type = 'time'

    org_node = LoadData.load_org_node(location)
    node = list(org_node.keys())
    print(node)

    # data_set1, data_set2, data_set3, data_set4, data_set5, data_set6, \
    # data_set7, data_set8, data_set9, data_set10 = ([] for _ in range(10))

    data_set1 = node[0:2000]
    data_set2 = node[2000:4000]
    data_set3 = node[4000: 6000]
    data_set4 = node[6000: 8000]
    data_set5 = node[8000: 10000]
    data_set6 = node[10000: 12000]
    data_set7 = node[12000: 14000]
    data_set8 = node[14000: 16000]
    data_set9 = node[16000: 18000]
    data_set10 = node[18000::]

    p1 = mp.Process(target=job, args=(data_set1, node, dimension_type, location, dimension, 1))
    p2 = mp.Process(target=job, args=(data_set2, node, dimension_type, location, dimension, 2))
    # p3 = mp.Process(target=job, args=(data_set3, node, dimension_type, location, dimension, 3))
    # p4 = mp.Process(target=job, args=(data_set4, node, dimension_type, location, dimension, 4))
    # p5 = mp.Process(target=job, args=(data_set5, node, dimension_type, location, dimension, 5))
    # p6 = mp.Process(target=job, args=(data_set6, node, dimension_type, location, dimension, 6))
    # p7 = mp.Process(target=job, args=(data_set7, node, dimension_type, location, dimension, 7))
    # p8 = mp.Process(target=job, args=(data_set8, node, dimension_type, location, dimension, 8))
    # p9 = mp.Process(target=job, args=(data_set9, node, dimension_type, location, dimension, 9))
    # p10 = mp.Process(target=job, args=(data_set10, node, dimension_type, location, dimension, 10))

    p1.start()
    p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
    # p7.start()
    # p8.start()
    # p9.start()
    # p10.start()

    p1.join()
    p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
    # p8.join()
    # p9.join()
    # p10.join()
