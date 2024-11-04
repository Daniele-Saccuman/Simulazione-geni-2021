import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.graph = nx.Graph()

        self._listChromo = []
        self._listConnectedGenes = []
        self._listGenes = []
        self._idMap ={}
        self.listaUscenti = []
        self.listaBest = []

    def build_graph(self):

        self._listGenes = DAO.get_all_geneID()
        self.graph.add_nodes_from(self._listGenes)
        for g in self._idMap:
            self._idMap[g.GeneID] = g

        self._listConnectedGenes = DAO.getAllConnectedGenes()
        for c in self._listConnectedGenes:
            if c[0] in self._listGenes and c[2] in self._listGenes:
                if c[1] != c[3]:
                    peso = abs(c[4])
                    self.graph.add_edge(c[0], c[2], weight=peso)
                elif c[1] == c[3]:
                    peso = 2*abs(c[4])
                    self.graph.add_edge(c[0], c[2], weight=peso)

    def getGeni(self):
        listaGeni = DAO.get_all_geneID()
        return listaGeni

    def archiAdiacenti(self):
        listaVicini = []
        for g in self._listGenes:
            for vicino in self.graph.neighbors(g):
                peso = self.graph[g][vicino]["weight"]
                listaVicini.append((g, vicino, peso))
        listaVicini.sort(key=lambda x: x[2], reverse=True)
        return listaVicini

    def get_weakly_connected_components(self):
        # Ottiene le componenti debolmente connesse del grafo
        components = list(nx.weakly_connected_components(self.graph))
        return components

    def get_nodes(self):
        return self.graph.nodes()

    def get_edges(self):
        return list(self.graph.edges(data=True))

    def get_num_of_nodes(self):
        return self.graph.number_of_nodes()

    def get_num_of_edges(self):
        return self.graph.number_of_edges()