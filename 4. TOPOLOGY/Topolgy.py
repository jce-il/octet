import json

import webbrowser
import jsonpickle
import tempfile
class Topolgy:

    def __init__(self):
        self.ObjectArray = []

    def AddNode(self, newNode):
        self.ObjectArray.append(newNode)
        return newNode;

    def AddEdge(self, newEdge):
        self.ObjectArray.append(newEdge)
        return newEdge;
    def ConvertToJson(nodes):
        json =  jsonpickle.encode(nodes, unpicklable=False)

        return json
    def displayTopolgy(url):
        webbrowser.open(url, new=2)
    def readJson(path):
        f = open(path, 'r')
        data = f.read();
        return data;

    def BuildTopolgyFromFile(self,path):
        data = Topolgy.readJson(path);
        f = open('Template.html', 'r')
        temp_name = next(tempfile._get_candidate_names())
        temp_name = temp_name + ".html"
        temp_name = ".\\Output\\"+ temp_name
        d = open(temp_name, 'w')
        htmlFile = f.read();
        f.close();
        htmlFile = htmlFile.replace('$JSON$', data);
        d.write(htmlFile);
        d.close();
        Topolgy.displayTopolgy(d.name);



    def BuildTopolgy(self):
        data = Topolgy.ConvertToJson(self.ObjectArray)
        f = open('Template.html', 'r')
        temp_name = next(tempfile._get_candidate_names())
        temp_name = temp_name +".html"
        temp_name =".\\Output\\"+ temp_name
        d = open(temp_name, 'w')
        htmlFile = f.read();
        htmlFile = htmlFile.replace('$JSON$', data);
        f.close();
        d.write(htmlFile);
        d.close();
        Topolgy.displayTopolgy(d.name);




