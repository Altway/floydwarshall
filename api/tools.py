# coding: utf-8
import json
import copy
import itertools
import math
import re
import sys


class AdjMatrix():

    def __init__(self, weight):
        self.weight = weight

    def __getitem__(self, key):
        try:
            item = self.weight[key]
        except KeyError as e:
            item = math.inf
        return item

    def __setitem__(self, key, value):
        self.weight[key] = value

    def __iter__(self):
        return (
            self.__getitem__(i) for i in itertools.product(
                range(0, self.__len__()+1), repeat=2
            )
        )

    def __len__(self):
        return len(self.weight)

    def __repr__(self):
        return str(self.weight)


def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    return {"node_number": data[0], "weight": data[2:]}


def read_form(data):
    tmp = re.split('\n', data)
    node_number, _, *weight_list, _ = tmp
    return {
        "node_number": node_number,
        "weight": weight_list
    }


def init_struct(problem):
    weight_list_splitted = [_.split(",") for _ in problem['weight']]
    adj_mat_weight = dict()
    for (start, end, cost) in weight_list_splitted:
        adj_mat_weight[(int(start)-1, int(end)-1)] = int(cost)

    return AdjMatrix(adj_mat_weight)


def floydWarshall(adj_mat):
    """
    let dist be a |V| × |V| array of minimum distances initialized to inf
    for each edge (u,v)
        dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
    for each vertex v
        dist[v][v] ← 0
    for k from 1 to |V|
        for i from 1 to |V|
            for j from 1 to |V|
                if dist[i][j] > dist[i][k] + dist[k][j]
                    dist[i][j] ← dist[i][k] + dist[k][j]
                end if
    """
    g = copy.deepcopy(adj_mat)
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                if g[(i, j)] > g[(i, k)] + g[(k, j)]:
                    g[(i, j)] = g[(i, k)] + g[(k, j)]

    return g

def main():
    try:
        file_path = sys.argv[1]
    except IndexError as e:
        file_path = "data/input.txt"
        print("Using default path : {}".format(file_path))

    problem = read_file(file_path)
    adj_mat = init_struct(problem)
    print("Before F-W algorithm: {}".format(adj_mat))
    new_adj_mat = floydWarshall(adj_mat)
    print("After F-W algorithm: {}".format(new_adj_mat))


if __name__ == "__main__":
    main()
