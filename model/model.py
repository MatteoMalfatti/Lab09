import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.Graph()
        self.idMap={}



    def buildIdMap(self,idmap):
        lista=DAO.getAllNodes()
        for n in lista:
            idmap[n.ID]=n



    def buildGraph(self,distanza):
        self.grafo.clear()
        self.idMap={}
        if len(self.idMap)==0:
           self.buildIdMap(self.idMap)
        listaArchi=[]

        for n in DAO.getArchi(distanza): #tuple di (id_1,id_2,dist media)
            id_1=n[0]
            id_2=n[1]
            dist_media=n[2]

            a1=self.idMap.get(id_1)

            a2=self.idMap.get(id_2)

            self.grafo.add_node(a1)
            self.grafo.add_node(a2)
            self.grafo.add_edge(a1,a2,weight=dist_media)
            riepilogo=f"{a1} - {a2} - {dist_media}"
            listaArchi.append(riepilogo)
        return listaArchi






    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)






