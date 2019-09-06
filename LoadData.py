"""
Load the road network
"""

import os
import ast
from ast import literal_eval as make_tuple


class LoadData:

    @staticmethod
    def load_org_node(location):
        data = {}
        rel_path = 'data/'+location+'/go_node.txt'
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        with open(abs_path, 'r') as file_handle:
            for line in file_handle:
                tmp = line.split(' ')
                data[int(tmp[0])] = (float(tmp[1]), float(tmp[2]))
        return data

    @staticmethod
    def load_org_path(location, dimension):
        path = {}
        rel_path = 'data/'+location+'/'+str(dimension)+'_goEdge.txt'
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        with open(abs_path, 'r') as file_handle:
            for line in file_handle:
                field = list(map(float, line.strip().split()))
                path[(int(field[1]), int(field[2]))] = tuple(field[3::])
        return path

    @staticmethod
    def load_linking_table(location):
        print(location)
        rel_path = 'data/'+location+'/LinkTable.txt'
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        data = {}
        with open(abs_path, 'r') as file_handle:
            for line in file_handle:
                element = make_tuple(line)
                data[element[0]] = element[1]
        return data

    @staticmethod
    def load_found_pair(city):
        path = 'data/' + city + '/FoundPair.txt'
        data = []
        with open(path, 'r', encoding='utf-8') as file_handle:
            for line in file_handle:
                element = make_tuple(line)
                data.append(element)
        return data

    @staticmethod
    def load_not_found_node(path):
        result = []
        with open(path, 'r', encoding='utf-8') as file_handle:
            for line in file_handle:
                result.append(ast.literal_eval(line))
        return result

