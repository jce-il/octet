# -*- coding: utf-8 -*-

from math import pi
import math

'''container class for EXTENSIVE CONTINUOUS QUANTITIES''' 
class Extensive_Continues_quantity:
    _TypeName = "not defined"  # example, mass, Volume, Energy, Kinetic Energy
    _Units = "Not defined" # Kg, Jaoul, mol, 
    _Value = -999999.99
    
    def __init__(self,TypeName,Units,Value):
        self._TypeName = TypeName
        self._Units = Units
        self._Value = Value
    
    def Add(self,ValueToAdd,Units):
        if self._Units == Units:
            self._Value+=ValueToAdd
    def subtract(self,ValueToSubtract,Units):
        if self._Units == Units:
            self._Value-=ValueToSubtract
    def IsEqual(self,ECQ):
        if((self._TypeName == ECQ._TypeName) and (self._Units == ECQ._Units) and (self._Value == ECQ._Value)):
            return True
        else:
            return False
    def IsGreater(self,ECQ):
         if((self._TypeName == ECQ._TypeName) and (self._Units == ECQ._Units)):
             if(self._Value > ECQ._Value):
                 return True
             else:
                 return False

    def IsLower(self,ECQ):
         if((self._TypeName == ECQ._TypeName) and (self._Units == ECQ._Units)):
             if(self._Value < ECQ._Value):
                 return True
             else:
                 return False
                     
    def __str__(self):
        s = ""
        s='%s : %d %s'% (self._TypeName,self._Value,self._Units)
        return s
    
        
class molar:
     def molarOfSubstenceInSolution(name,gramsOfSubstance,MolecularWeight,VolumOfSolution_liter):
         ''' the funciton clacs the molarity of a substance in solution'''
         #check the amount of mol of the substance we have
         molOfsubstance = gramsOfSubstance/MolecularWeight
         Molar = molOfsubstance/VolumOfSolution_liter
         return (Molar,'-molar',name)
         
         
class volume:
    '''#http://ascopubs.org/doi/full/10.1200/JCO.2001.19.2.551
      
    this class contains a minimal set of volume calculations'''
    def BoxVoume(width,height,depth):
        '''this function retuns the volume of 3d  box'''
        return width*height*depth;
    def ConeVolume(baseRadius,height):
      '''claculate cone volume'''
      V = (pi*baseRadius*baseRadius*height)/3
      return V
    def SphereVolume(radius):
        '''claculate Sphere Volume'''
        V = (4/3)*pi*math.pow(radius,3)
        return V
    def EllipsoidVolume(a,b,c):
        ''' a, b, c are the three ellipsoid radii,'''
        V = (4/3)*pi*a*b*c
        return V
    def PyramidVolume(baseX,baseY,height):
        ''' compute the volue of a pyramid.
        enter pyramid base dimentions "baseX, baseY" and pyramid height'''
        S = baseX*baseY
        V = (S*height)/3
        return V
    
    def VolumeOfLisionInSlice(sliceArea, sliceThickness):
        ''' when mesuriong a lesion volume, corss sectional imagery is used such as MRI
        in each layer the area of a lision is marked, the layer thickness is given to mesure the 
        volume of part of the lesion that is found in this layer.'''
        return sliceArea*sliceThickness;
    
        
                 
            
            
    
        
        