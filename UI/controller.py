import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    #funzione che popola il menù a tendina delle biblioteche
    def popola_dd_biblioteca(self):
        self._view._dd_biblioteca.options.clear()     #svuota la lista contenente le biblioteche
        self._view._dd_biblioteca.options.append(ft.DropdownOption(None, "Nessun Filtro"))   #aggiungo alla lista "nessun filtro"
        biblioteche = self._model.get_biblioteche()   #creo una lista contente le biblioteche del database chiamando la funzione della sezione model

        if biblioteche:       #controllo che le biblioteche siano state caricate correttamente
            for biblioteca in biblioteche:
                #aggiungo alla lista da stampare tutte le biblioteche del database
                self._view._dd_biblioteca.options.append(ft.DropdownOption(biblioteca.nome))
        else:
            #stampo messaggio se si verifica un problema con il caricamento delle biblioteche
            self._view.show_alert("Le biblioteche non sono state inserite correttamente")

        self._view.update()   #aggiorno la vista

    #funzione che popola il menù a tendina dei generi
    def popola_dd_genere(self):
        self._view._dd_genere.options.clear()       #svuota la lista contenente i generi
        self._view._dd_genere.options.append(ft.DropdownOption(None, "Nessun Filtro"))   #aggiungo alla lista "nessun filtro"
        generi = self._model.get_generi() #creo una lista contente i generi del database chiamando la funzione della sezione model

        if generi:         #controllo che i generi siano stati caricati correttamente
            for genere in generi:
                #aggiungo alla lista da stampare tutti i generi del database
                self._view._dd_genere.options.append(ft.DropdownOption(genere))
        else:
            #stampo messaggio se si verifica un problema con il caricamento dei generi
            self._view.show_alert("I generi non sono stati inseriti correttamente")

        self._view.update()  #aggiorno la vista

    # CALLBACKS DROPDOWN
    #handler che cambia il valore della biblioteca selezionata che servirà poi per stampare i libri filtrati
    def handler_biblioteca_sel(self,e):
        if e.control.value == "Nessun Filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = e.control.value

    # handler che cambia il valore del genere selezionato che servirà poi per stampare i libri filtrati
    def handler_genere_sel(self,e):
        if e.control.value == "Nessun Filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    #handler che stampa i libri filtrati in base ai criteri selezionati quando si preme il pulsante "Mostra Libri"
    def handler_mostra(self,e):
        self._view._lista_libri.controls.clear()   #svuota la lista contenente i libri filtrati
        # creo una lista contente i libri filtrati del database chiamando la funzione della sezione model
        lista_libri_filtrati = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if lista_libri_filtrati is None:   #controllo che sia avvenuta correttamente la connessione
            self._view.show_alert("Errore di connessione al database.")
        elif len(lista_libri_filtrati) == 0:    #controllo che siano presenti dei libri in base ai criteri selezionati
            self._view.show_alert("Nessun libro trovato per i criteri selezionati")
        else:
            for libro in lista_libri_filtrati:
                #aggiungo alla lista da stampare tutti i generi del database
                self._view._lista_libri.controls.append(ft.Text(f"{libro}"))

        self._view.update()   #aggiorno la vista
