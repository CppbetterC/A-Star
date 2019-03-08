"""
Generate the dimension data and append
"""

import random
import os

from LoadData import LoadData
from Export import Export


def generate_link_table(data):
    """
    Generate the link table for experiment
    :param data:
    :return:
    """
    link = {}
    for key in data.keys():
        if link.__contains__(key[0]):
            link[key[0]] = link[key[0]] + (key[1],)
        else:
            link[key[0]] = (key[1],)

        if link.__contains__(key[1]):
            link[key[1]] = link[key[1]] + (key[0],)
        else:
            link[key[1]] = (key[0],)
    return link


def generate_dimension(data):
    """
    Generate the dimension data for experiment
    Skyline path, multiple dimension
    :param data:
    :return:
    """
    result = {}
    scope = list(data.values())
    upper = max(scope)[0]
    lower = min(scope)[0]
    for key, value in data.items():
        result[key] = data[key] + (round(random.uniform(lower, upper), 6),)
    return result


dimension = 1
location = 'California'
path = {}
rel_path = 'data/' + location + '/' + str(dimension) + '_goEdge.txt'
abs_path = os.path.join(os.path.dirname(__file__), rel_path)
with open(abs_path, 'r') as file_handle:
    for line in file_handle:
        tmp = line.split(' ')
        path[(int(tmp[1]), int(tmp[2]))] = (float(tmp[3].strip()),)

link_table = generate_link_table(path)
Export.export_link_table(location, link_table)

dimension_data = generate_dimension(path)
dimension += 1
Export.export_dimension_data(location, dimension, dimension_data)
