#gives http://www.pythonchallenge.com/pc/hex/lake.html
#! /usr/bin/env python

from PIL import Image

class AStar(object):
    def __init__ (self, maphandler):
        self.mh = maphandler

    def _getBestOpenNode (self):
        bestNode = None

        for n in self.on:
            if not bestNode:
                bestNode = n
            elif n.score < bestNode.score:
                bestNode = n

        return bestNode

    def _tracePath (self, n):
        nodes = []
        totalCost = n.mCost
        p = n.parent
        nodes.insert(0, n)

        while True:
            if p.parent is None:
                break

            nodes.insert(0, p)
            p = p.parent

        return Path(nodes, totalCost)

    def _handleNode (self, node, end):
        i = self.o.index(node.lid)
        self.on.pop(i)
        self.o.pop(i)
        self.c.append(node.lid)

        nodes = self.mh.getAdjacentNodes(node, end)
        # print('%d visited' % len(self.c))
        for n in nodes:
            # print("iter node", (n.location.x, n.location.y), n.lid)
            if n.location == end:
                return n
            elif n.lid in self.c:
                # print('visited')
                continue
            elif n.lid in self.o:
                i = self.o.index(n.lid)
                on = self.on[i]
                if n.mCost < on.mCost:
                    print("update", (n.location.x, n.location.y), n.mCost)
                    self.on.pop(i)
                    self.o.pop(i)
                    self.on.append(n)
                    self.o.append(n.lid)
            else:
                # print('%d put to open node' % n.lid)
                self.on.append(n)
                self.o.append(n.lid)

        return None

    def findPath (self, fromLoacation, toLocation):
        self.o = []
        self.on = []
        self.c = []

        end = toLocation
        fnode = self.mh.getNode(fromLoacation)
        self.on.append(fnode)
        self.o.append(fnode.lid)
        nextNode = fnode

        while nextNode is not None:
        # for i in range(10):
            finish = self._handleNode(nextNode, end)

            if finish:
                return self._tracePath(finish)

            nextNode = self._getBestOpenNode()

        return None

class Path(object):
    def __init__ (self, nodes, totalCost):
        self.nodes = nodes
        self.totalCost = totalCost

    def getNodes (self):
        return self.nodes

    def getTotalMoveCost (self):
        return self.totalCost

class Node(object):
    def __init__ (self, location, mCost, lid, parent = None):
        self.location = location
        self.mCost = mCost
        self.parent = parent
        self.score = 0
        self.lid = lid

    def __eq__ (self, n):
        if n == self.lid:
            return True
        else:
            return False

class SQ_Location(object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __eq__ (self, l):
        if l.x == self.x and l.y == self.y:
            return True
        else:
            return False

class SQ_MapHandler(object):
    def __init__ (self, mapdata, width, height):
        self.m = mapdata
        self.w = width
        self.h = height

    def getNode(self, location):
        x = location.x
        y = location.y

        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None

        lid = (y * self.w) + x

        cost = self.m[lid]

        if cost == -1:
            return None

        return Node(location, cost, lid)

    def _handleNode (self, fromNode, path, destLocation):
        x = fromNode.location.x + path[0]
        y = fromNode.location.y + path[1]

        n = self.getNode(SQ_Location(x, y))
        # print('get node:(%d, %d)' % (x, y) )
        destx, desty = destLocation.x, destLocation.y

        if n is not None:
            dx = abs(x - destx)
            dy = abs(y - desty)
            emCost = dx + dy
            n.mCost += fromNode.mCost
            n.score = n.mCost + emCost
            n.parent = fromNode

            return n

        return None

    def getAdjacentNodes (self, curNode, dest):
        result = []
        cl = curNode.location
        dl = dest
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for d in dirs:
            n = self._handleNode(curNode, d, dest)
            if n:
                result.append(n)

        return result

def main ():
    im = Image.open('maze.png')
    # im2 = Image.new(im.mode, im.size)
    px = im.load()
    # px2 = im2.load()
    mapdata = []

    for p in im.getdata():
        if p == (255, 255, 255, 255):
            mapdata.append(-1)
        else:
            mapdata.append(1)

    mapdata[639] = 5
    mapdata[410241] = 6

    astar = AStar(SQ_MapHandler(mapdata, 641, 641))
    start = SQ_Location(639, 0)
    end = SQ_Location(1, 640)
    p = astar.findPath(start, end)
    data = []

    for node in p.nodes:
        x = node.location.x
        y = node.location.y
        if x % 2 and y % 2:
            data.append((px[x, y][0]))
            # px2[x, y] = (0, 255, 0, 255)
            # im2.putpixel((x, y), (0, 255, 0, 255))

    # data
    with open('unzip_maze.zip', 'wb') as f:
        f.write(bytes(data))

    # im2.save('maze_out.png')

if __name__ == '__main__':
    main()
    # im = Image.open('maze_out.png')
    # im2 = Image.new(im.mode, im.size)
    #
    # for x in range(im.size[0]):
    #     for y in range(im.size[1]):
    #         if im.getpixel((x, y)) == (0, 0, 0, 255):
    #             im2.putpixel((x, y), (0, 0, 0, 255))
    #
    # im2.save('out.png')
