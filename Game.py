from collections import defaultdict


class River(object):
    def __init__(self, numOfElements=100):
        self.rank = [0 for _ in range(numOfElements)]
        self.parents = [0 for _ in range(numOfElements)]
        self.n = numOfElements

    def init (self, numOfElements):
        self.makeSet()

    def makeSet(self):
        for i in range(self.n):
            self.parents[i] = i

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return
        if self.rank[parentX] > self.rank[parentY]:
            self.parents[parentY] = parentX
        elif self.rank[parentX] < self.rank[parentY]:
            self.parents[parentX] = parentY
        else:
            self.parents[parentX] = parentY
            self.rank[parentY] += 1

    def find(self, x):
        parentX = self.parents[x]
        if x != parentX:
            parentX = self.find(parentX)
        return parentX


def riverSizes(matrix):
    global i, j
    if not matrix:
        return []

    rowCount, colCount = len(matrix), len(matrix[0])
    djs = River()
    for i in range(rowCount):
        for j in range(colCount):
            val = matrix[i][j]
            if val == 0:
                continue

    if i + 1 < rowCount and matrix[i + 1][j] == 1:
        djs.union(i * colCount + j, (i + 1) * colCount + j)

    if i - 1 >= 0 and matrix[i - 1][j] == 1:
        djs.union(i * colCount + j, (i - 1) * colCount + j)

    if j + 1 < colCount and matrix[i][j + 1] == 1:
        djs.union(i * colCount + j, (i) * colCount + j + 1)

    if j - 1 >= 0 and matrix[i][j - 1] == 1:
        djs.union(i * colCount + j, (i) * colCount + j - 1)

    islands = defaultdict(int)
    for i in range(rowCount):
        for j in range(colCount):
            if matrix[i][j] == 1:
                val = i * colCount + j
                parent = djs.find(val)
                islands[parent] += 1

    return islands.values()

