import  sys;
import  Classes
from Topolgy import  *
from Classes import  *


import sys

def main():
    topolgy = Topolgy ()
    n1=  topolgy.AddNode(Classes.Node("Nati"))
    n2=   topolgy.AddNode(Classes.Node("Iren"))
    n3 = topolgy.AddNode(Classes.Node("Ran"))
    n4= topolgy.AddNode(Classes.Node("Roni"))
    topolgy.AddEdge(Classes.Edge(n1,n2,0.1))
    topolgy.AddEdge(Classes.Edge(n1, n4, 0.1))
    topolgy.AddEdge(Classes.Edge(n4, n3, 0.1))
    topolgy.AddEdge(Classes.Edge(n2, n3, 0.1))
    topolgy.AddEdge(Classes.Edge(n1, n3, 0.1))

    #This will build the graph from the nodes that we create above
    topolgy.BuildTopolgy();
    # This will build the graph from the nodes that data.json file
    topolgyFromFile = Topolgy()
    topolgyFromFile.BuildTopolgyFromFile("data.json")


if __name__ == "__main__":
    main()