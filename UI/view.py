import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        #creo una dropdown per selezionare la biblioteca
        self._dd_biblioteca = ft.Dropdown(label="Biblioteca",
                                          width=450,             #larghezza dropdown
                                          on_select=self.controller.handler_biblioteca_sel  #chiama la funzione quando viene selezionata una biblioteca
                                          )
        self.controller.popola_dd_biblioteca()    #funzione del controller che popola la dropdown delle biblioteche

        #creo una dropdown per selezionare il genere
        self._dd_genere = ft.Dropdown(label="Genere",
                                      width=250,           #larghezza dropdown
                                      on_select=self.controller.handler_genere_sel    #chiama la funzione quando viene selezionato un genere
                                      )
        self.controller.popola_dd_genere()         #funzione del controller che popola la dropdown dei generi


        # Sezione 3: Libri
        #creo pulsante per mostrare i libri selezionati in base ai criteri scelti
        pulsante_mostra_libri = ft.Button(content="Mostra Libri",
                                          on_click=self.controller.handler_mostra)   #quando viene premuto chiama la funzione del controller

        #creo la lista che conterrà i libri selezionati in base ai criteri
        self._lista_libri = ft.ListView(expand=True, spacing=10, auto_scroll=True)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            #creo una riga che contenga le due drop down per selezionare i criteri, allineandole al centro
            ft.Row(controls = [self._dd_biblioteca, self._dd_genere],
                   alignment = ft.MainAxisAlignment.CENTER,
                   spacing=20,
                   ),
            ft.Divider(),    #riga di divisione tra le sezioni

            # Sezione 3: Libri
            pulsante_mostra_libri,    #aggiungo il pulsante per mostrare i libri selezionati alla pagina
            self._lista_libri,        #aggiungo la lista contenente i libri selezionati alla pagina
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
