from random import *
import uuid
class Node:
    def __init__(self,name,rightAngel ='Not Define',leftAngel="Not Define"):
        self.group = "nodes";
        self.removed = False;
        self.selected = False;
        self.selectabl = True;
        self.locked = False;
        self.grabbed = False;
        self.grabbable = True;
        self.position = []
        self.data = NodeData(name,rightAngel,leftAngel)


class Edge:
    def __init__(self,source,target,weight,label) :
        self.group = "edges";
        self.position = [];
        self.removed= True;
        self.selected= False;
        self.selectable= False;
        self.locked= False;
        self.grabbed= False;
        self.grabbable= False;
        self.classes= ""
        self.data = EdgeData(source,target,weight,label)


class Position:

    def __init__(self, x,y):
        self.x =x
        self.y = y

class EdgeData :
    def __init__(self, source,target,weight,label):
        self.source = source.data.id;
        self.target = target.data.id;
        self.id = source.data.name + target.data.name;
        self.intn = True;
        self.group = "path"
        self.weight = weight
        self.label = label;


class NodeData :
    def __init__(self,name,rightAngel,leftAngel):
        u = uuid.uuid1()
        self.id =u.hex
        self.idInt = u.hex
        self.name = name;
        self.rightAngel =rightAngel;
        self.leftAngel = leftAngel

