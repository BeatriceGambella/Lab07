from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    #funzione che restituisce tutte le biblioteche del database
    def read_biblioteche(self):
        cnx = DBConnect.get_connection()                        #apro la connessione
        if cnx is None:                                         #controllo se la connessione sia andata a buon fine
            print("Errore nella connessione al database")
            return None

        result = []                                             #creo la lista che conterrà le biblioteche da ritornare
        cursor = cnx.cursor(dictionary=True)                    #creo un cursore "dizionario"
        #creo la query che mi restituisca tutte le biblioteche presenti nel database
        query = """ SELECT * 
                    FROM biblioteca """
        try:
            cursor.execute(query)                               #provo ad eseguire la query
            for row in cursor:
                biblioteca = Biblioteca( id=row["id"], nome=row["nome"], indirizzo=row["indirizzo"])
                result.append(biblioteca)      #itero il cursore e appendo alla lista creata precedentemente tutte le biblioteche
        except Exception:
            print("Errore durante l'esecuzione della query")    #messaggio da stampare se la query non è stata eseguita correttamente
            result = None

        cursor.close()                                          #chiudo il cursore
        cnx.close()                                             #chiudo la connessione
        return result                                           #ritorno la lista contenente tutte le biblioteche
