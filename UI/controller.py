import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        mese = self._view.dd_mese.value
        self._view.lst_result.controls.clear()
        if mese is None:
            self._view.lst_result.controls.append(ft.Text("Non hai selezionato il mese"))
            self._view.update_page()
            return
        lista_misure = self._model.get_misure(mese)
        for l in lista_misure:
            self._view.lst_result.controls.append(ft.Text(f"{l.Localita}: {l.Umidita}"))
        self._view.update_page()



    def handle_sequenza(self, e):
        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)

