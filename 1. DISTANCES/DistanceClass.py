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
    def bond_length(mol, a0, a1):  
        """In molecular geometry, bond length or bond distance is the average distance
        between nuclei of two bonded atoms in a molecule. 
        It is a transferable property of a bond between atoms of fixed types, 
        relatively independent of the rest of the rest of the molecule.""" 
        return mol.get_distance(a0, a1)
    
    
print(DistanceCalculator.euclidean_distance((1,1,1), (4,4,4)))

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(DistanceCalculator.geographical_distance(newport_ri, cleveland_oh, 'm'))


h2o = Atoms(symbols='H2O',
                positions=[( 0.776070, 0.590459, 0.00000),
                           (-0.776070, 0.590459, 0.00000),
                           (0.000000,  -0.007702,  -0.000001)],
                pbc=(1,1,1))
    
print "Bond length: %.4f" % DistanceCalculator.bond_length(h2o, 0, 2)