import os


class Export:
    @staticmethod
    def export_link_table(location, data):
        """
        Export the link table
        :param location:
        :param data:
        :return:
        """
        rel_path = 'data/'+location+'/LinkTable.txt'
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        with open(abs_path, 'w') as f:
            for key, value in data.items():
                element = (key, value)
                f.writelines(str(element))
                f.write('\n')
        f.close()

    @staticmethod
    def export_dimension_data(location, dimension, data):
        """
        Export the dimension data
        :param location:
        :param dimension:
        :param data:
        :return:
        """
        rel_path = 'data/'+location+'/'+str(dimension)+'_goEdge.txt'
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        with open(abs_path, 'w') as f:
            count = 0
            for key, value in data.items():
                f.write(str(count)+' '+str(key[0])+' '+str(key[1])+
                        ' '+str(value[0])+' '+str(value[1]))
                f.write('\n')
        f.close()

    @staticmethod
    def export_a_star(data, dtype, location, count):
        """
        Export the A* path
        :param data:
        :return:
        """
        path_name = 'data/' + location + '/offline_a_star(' + dtype + ')_'+str(count)+'.txt'
        path_name = os.path.join(os.path.dirname(__file__), path_name)
        with open(path_name, 'a+') as f:
            for path in data:
                f.writelines(str(path))
                f.write("\n")

        f.close()