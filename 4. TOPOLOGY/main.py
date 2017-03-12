import  sys;
import  Classes
from Topology import  *
from Classes import  *


import sys

def main():
    Topology = TopologyClass ()
    n1=  Topology.AddNode(Classes.Node("Nati"))
    n2=   Topology.AddNode(Classes.Node("Iren",30,45))
    n3 = Topology.AddNode(Classes.Node("Ran",30,45))
    n4= Topology.AddNode(Classes.Node("Roni",30,45))
    Topology.AddEdge(Classes.Edge(n1,n2,0.1,'a'))
    Topology.AddEdge(Classes.Edge(n1, n4, 0.1,'b'))
    Topology.AddEdge(Classes.Edge(n4, n3, 0.1,'c'))
    Topology.AddEdge(Classes.Edge(n2, n3, 0.1,'d'))
    Topology.AddEdge(Classes.Edge(n1, n3, 0.1,'e'))

    #This will build the graph from the nodes that we create above
    Topology.BuildTopolgy();
    # This will build the graph from the nodes that data.json file
    TopologyFromFile = Topology()
    TopologyFromFile.BuildTopolgyFromFile("data.json")


if __name__ == "__main__":
    main()