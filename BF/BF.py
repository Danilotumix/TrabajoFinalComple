import csv
import math
import sys

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def obtener_vertice(self, key):
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def agregar_arco(self, src_key, dest_key, weight=1):
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def check_si_arco_existe(self, src_key, dest_key):
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:

    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key

    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight

    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()

    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]

    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to


def bellman_ford(g, source):

    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0

    for _ in range(len(g) - 1):
        for v in g:
            for n in v.get_neighbours():
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))

    return distance

def run(filename = "input2.csv"):
    g = Grafo()

    with open(filename) as file:
        reader = csv.reader(file)
        a = [[]]
        a = list(reader)
        for k in range(1,len(a)+1):
            g.agregar_vertice(k)
        for i in range(len(a)):
            x = a[i][3:-1]
            for j in range(len(x)):
                x = a[i][j + 3]
                a1 = float(a[i][1])
                a2 = float(a[i][2])
                b1 = float(a[int(x) - 1][1])
                b2 = float(a[int(x) - 1][2])
                s = int(i + 1)
                d = int(x)
                m=b1-a1
                n=b2-a1
                Peso = math.sqrt(m*m+n*n)
                if(k==186):
                    Peso= math.sqrt(Peso)
                g.agregar_arco(s, d, Peso)
    while(True):
        print('Desde que Nodo se desesa calcular el camino mas corto')
        Origen=int(input())
        source = g.obtener_vertice(Origen)
        distance = bellman_ford(g, source)
        print(' ')
        print('Distancia desde el nodo {}: '.format(Origen))
        for v in distance:
            print('Hasta el nodo {}: {}'.format(v.get_key(), distance[v]))
        print(' ')