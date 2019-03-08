from Edges import Edges


class Datatransform:
    def __init__(self):
        print('data transform')
    
    def node_transform(self, data):
        latitude, longitude = {}, {}
        for e in data:
            tmp = e.split(' ')
            latitude[int(tmp[0])] = float(tmp[1])
            longitude[int(tmp[0])] = float(tmp[2])
        return latitude, longitude

    def path_transform(self, data):
        e_data = {}
        for e in data:
            tmp = e.split(' ')
            e_data[tmp[1] + '->' + tmp[2]] = Edges(tmp[1] + '->' + tmp[2], float(tmp[3]), float(tmp[4]))
        return e_data

    def link_table_transform(self, data):
        return [int(x) for x in data]