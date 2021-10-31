import pandas as pd
import numpy as np


class Metric:

    def __init__(self, id):
        self.id = id
        self.name = 'metric name - ' + str(id)
        self.parents = []
        self.childs = []

    def show_metric(self):
        print(self.id)


class Tree(Metric):

    def __init__(self, rows, elements_size):
        self.r = rows
        self.elements_size = elements_size
        self.rows = []
        self.cells = []
        self.all_paths = []

    def generate_metric_rows(self):
        for row in range(1, self.r+1):
            self.rows.append(row)

    def generate_random_metrics(self):
        for row in self.rows:
            for element in range(1, self.elements_size+1):
                path_id = int(str(row) + str(element))
                self.all_paths.append(Metric(id=path_id))
                self.cells.append(path_id)

    def randomize_network(self):
        for path in self.all_paths:

            # remove all non interested rows from the list used to build the random network
            filtered_parents = list(filter(lambda cell: int(
                str(cell)[0:1]) == int(str(path.id)[0:1])+1, self.cells))
            filtered_childs = list(filter(lambda cell: int(
                str(cell)[0:1]) == int(str(path.id)[0:1])-1, self.cells))

            # define 2 parent
            for i in range(2):
                if filtered_parents:
                    parent = np.random.choice(
                        filtered_parents).item()
                    path.parents.append(parent)
                    filtered_parents.remove(parent)
                    i += 1

            # define 3 childs
            for i in range(3):
                if filtered_childs:
                    child = np.random.choice(filtered_childs).item()
                    path.childs.append(child)
                    filtered_childs.remove(child)
                    i += 1


tree = Tree(5, 5)
tree.generate_metric_rows()
tree.generate_random_metrics()
tree.randomize_network()

if __name__ == '__main__':
    Tree(5, 5)

print(tree)
