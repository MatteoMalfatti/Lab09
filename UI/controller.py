import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        self._view.txt_result.clean()
        self._view.update_page()
        distanzamin = self._view.txt_name.value
        if distanzamin is None or distanzamin == "":
            self._view.create_alert("Inserire il nome")
            return
        try:
            int(distanzamin)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un intero!"))
            self._view.update_page()
            return
        lista=self._model.buildGraph(distanzamin)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!!"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi {self._model.getNumNodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi {self._model.getNumEdges()}"))
        for n in lista:
            self._view.txt_result.controls.append(ft.Text(f"{n}"))

        self._view.update_page()











        self._view.update_page()
