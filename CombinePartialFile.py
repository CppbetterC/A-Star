import os
import ast


def load_shortest_file_name(fpath):
    result = []
    with os.scandir(fpath) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                result.append(entry.name)
    return result


def load_offline_shortest(fname, fpath):
    data = []
    for name in fname:
        path = fpath + '/' + name
        with open(path, "r", encoding="utf-8") as file_handle:
            for line in file_handle:
                data.append(ast.literal_eval(line.strip("\n")))
    return data


city = 'California'
file_path = 'data/' + city + '/Found'
file_name = load_shortest_file_name(file_path)
found = load_offline_shortest(file_name, file_path)

print(len(found))

file_path = 'data/' + city + '/FoundShortestPath.txt'
with open(file_path, 'w', encoding='utf-8') as f:
    for element in found:
        f.writelines(str(element))
        f.writelines('\n')






