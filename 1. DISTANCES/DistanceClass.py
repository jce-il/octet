import numpy as np
import networkx as nx
from ase import Atoms
from geopy.distance import vincenty
from scipy.spatial.distance import canberra
from skyfield.api import load
from numpy.core.umath_tests import inner1d

class DistanceCalculator:
    
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000, 'inch':39.3700787, 'foot': 3.2808399, 'mile': 1609.344}

    @staticmethod
    def convertor(val, unit1, unit2):
        """Distance units convertor"""
        return val * SI[unit1]/SI[unit2]
    
    
    @staticmethod
    def euclidean_distance(p1, p2):
        """In mathematics, the Euclidean distance or Euclidean metric is the "ordinary" 
        (i.e. straight-line) distance between two points in Euclidean space."""
        pOne = np.array(p1)
        pTwo = np.array(p2)
        return np.sqrt(np.sum(np.power((pOne - pTwo), 2)))

    
    @staticmethod
    def geographical_distance(cord1, cord2, metric_method):
        """Geographical distance is the distance measured along the surface of the earth. 
        The formulae in this article calculate distances between points which are defined 
        by geographical coordinates in terms of latitude and longitude."""
        if metric_method == 'km':
            return vincenty(cord1, cord2).kilometers
        elif metric_method == 'm':
            return vincenty(cord1, cord2).meters
        elif metric_method == 'mile':
            return vincenty(cord1, cord2).miles
        
        
    @staticmethod
    def astronomical_distance(planet1, planet2):
        """The astronomical unit (symbol au, or ua) is a unit of length, 
        roughly the distance from planet1 to planet2."""
        planets = load('de421.bsp')
        planet1, planet2 = planets[planet1], planets[planet2]
        ts = load.timescale()
        t = ts.now()
        position = planet1.at(t).observe(planet2)
        ra, dec, distance = position.radec()
        return distance.m

    
    @staticmethod
    def bond_length(mol, a0, a1):  
        """In molecular geometry, bond length or bond distance is the average distance
        between nuclei of two bonded atoms in a molecule. 
        It is a transferable property of a bond between atoms of fixed types, 
        relatively independent of the rest of the rest of the molecule.""" 
        return mol.get_distance(a0, a1)
    
    
    @staticmethod
    def canberra_distance(u, v):
        """The Canberra distance is a numerical measure of the 
        distance between pairs of points in a vector space."""
        return canberra(u, v)
    
    
    @staticmethod
    def distance_unweighted_graph(g, vertex1, vertex2): #return number of hops
        """In the mathematical field of graph theory, the distance between two vertices in a 
        graph is the number of edges in a shortest path (also called a graph geodesic) connecting them."""
        return nx.dijkstra_path_length(g, vertex1, vertex2)


    @staticmethod
    def distance_weighted_graph(g, vertex1, vertex2):
        """Find a path between two vertices (or nodes) in a graph such that
        the sum of the weights of its constituent edges is minimized."""
        return nx.dijkstra_path_length(g, vertex1, vertex2, 'distance')


    
print("Euclidean disatance between (1,1,1) and (4,4,4): " + str(DistanceCalculator.euclidean_distance((1,1,1), (4,4,4))))

jerusalem_israel = (31.783333, 35.216667)
tel_aviv_israel = (32.066667, 34.783333)
print("Geographical disatance between Jerusalem and Tel-Aviv: " + str(DistanceCalculator.geographical_distance(jerusalem_israel, tel_aviv_israel, 'm')) + "m")

h2o = Atoms(symbols='H2O',
                positions=[( 0.776070, 0.590459, 0.00000),
                           (-0.776070, 0.590459, 0.00000),
                           (0.000000,  -0.007702,  -0.000001)],
                pbc=(1,1,1))
    
print("H2O Bond length: %.4f" % DistanceCalculator.bond_length(h2o, 0, 2))

print("Geographical disatance between Earth and Mars: " + str(DistanceCalculator.astronomical_distance('earth', 'mars')) + "m")

print("Canberra disatance between [1,2,3] and [2,4,6]: " + str(DistanceCalculator.canberra_distance([1,2,3], [2,4,6])))

g = nx.Graph()
g.add_edge('a', 'b', distance=0.3)
g.add_edge('a', 'c', distance=0.7)
print("Unweighted distance between vertex b and vertex c in graph g: " + str(DistanceCalculator.distance_unweighted_graph(g, 'b', 'c')))
print("Weighted distance between vertex b and vertex c in graph g: " + str(DistanceCalculator.distance_weighted_graph(g, 'b', 'c')))


