# from LoadData import LoadData
# from Export import Export
# import os
#
#
# def get_link_node():
#     linkedNode = {}
#     path_name = 'data/oldenburg/LinkTable.txt'
#     path_name = os.path.join(os.path.dirname(__file__), path_name)
#     f = open(path_name, 'r', encoding='UTF-8')
#     tmp = []
#     while True:
#         dd = f.readline()
#         if dd == "":
#             break
#         tmp.append(dd)
#     for data in tmp:
#         tt = data.split("\n")[0].split("|")
#         dd = tt[1].split(";")
#         linkedNode[int(tt[0])] = tuple(int(d) for d in dd)
#     f.close()
#     return linkedNode
#
# data = get_link_node()
# print(data)
# Export.export_link_table('Oldenburg', data)


# heuristic function
# heuristic table
# src is node 0
# dst is node 49
# def __euclid_distance(self):
#     # for easy_oldenburg
#     # get the limited node, edges
#     # ln is the limited nodes
#     # int_dst = int(dst)
#     # a = (self.lon[int_dst], self.lat[int_dst])
#     #
#     # for e in self.get_limited_node():
#     #     int_e = int(e)
#     #     b = (self.lon[int_e], self.lat[int_e])
#     #     self.heuristic_table[(int_e,)] = distance.euclidean(a, b)
#
#     src = self.org_node[self.src]
#     for key in self.org_node.keys():
#         dst = self.org_node[key]
#         self.heuristic_table[(key,)] = distance.euclidean(src, dst)