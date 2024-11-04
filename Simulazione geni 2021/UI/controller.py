import flet as ft
from UI.view import View
from model.model import Model


class Controller:

    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listChromo = []
        self._chromo = None
        self.min = None
        self.max = None
        self.listaBest = []
        self.listaBest2 = []

    def handle_graph(self, e):

        self._model.build_graph()
        self._view.txt_result1.controls.append(ft.Text(
            f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        self._view.update_page()



    def handle_path(self, e):
        gene = self._view.dd_geni.value
        listaVicini = self._model.archiAdiacenti()
        self._view.txt_result2.controls.append(
                    ft.Text(f"Geni adiacenti a {gene}:"))
        for vicino in listaVicini:
            if gene == vicino[0]:
                self._view.txt_result2.controls.append(
                    ft.Text(f"{vicino[1]} con peso {vicino[2]}"))
        self._view.update_page()



    def fillDD(self):
        self._listChromo = self._model.getGeni()
        for c in self._listChromo:
            self._view.dd_geni.options.append(ft.dropdown.Option(c))
        self._view.update_page()

    def read_geni(self, e):
        if e.control.value is None:
            self._geni = None
        else:
            self._geni = e.control.value

