from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        #quando la funzione viene chiamata dal controller vengono restituiti tutti i libri filtrati trovati tramite la funzione del DAO
        return self._libro_dao.read_libri_filtrati(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        #quando la funzione viene chiamata dal controller vengono restituiti tutti i generi trovati tramite la funzione del DAO
        return self._libro_dao.read_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        #quando la funzione viene chiamata dal controller vengono restituite tutte le biblioteche trovate tramite la funzione del DAO
        return self._biblioteca_dao.read_biblioteche()
