import os
import ast

from LoadData import LoadData

city = 'California'
file_path = 'data/' + city + '/FoundShortestPath.txt'

found = set()
with open(file_path, "r", encoding="utf-8") as file_handle:
    for line in file_handle:
        tmp = ast.literal_eval(line.strip("\n"))
        key = (tmp[0], tmp[-1])
        found.add(key)


# org_node = list(LoadData.load_org_node(city).keys())
# all_pair = set()
# for i in range(len(org_node)):
#     for j in range(len(org_node)):
#         if i == j:
#             continue
#         else:
#             all_pair.add((org_node[i], org_node[j]))
# not_found = all_pair - found

print(len(found))

file_path = 'data/' + city + '/FoundPair.txt'
with open(file_path, 'w', encoding='utf-8') as f:
    for element in found:
        f.writelines(str(element))
        f.writelines('\n')


