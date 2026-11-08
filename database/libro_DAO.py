from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    #funzione che restituisce tutti i generi presenti ne database
    def read_generi(self):
        cnx = DBConnect.get_connection()                       #apro la connessione
        if cnx is None:                                        #controllo se la connessione sia andata a buon fine
            print("Errore nella connessione al database")
            return None

        result = []                                            #creo la lista che conterrà i generi da ritornare
        cursor = cnx.cursor(dictionary=True)                   #creo un cursore "dizionario"
        #creo la query che mi restituisca tutti i generi presenti nel database
        query = """ SELECT DISTINCT genere                     
                    FROM libro"""
        try:
            cursor.execute(query)                              #provo ad eseguire la query
            for row in cursor:
                genere = row["genere"]
                result.append(genere)      #itero il cursore e appendo alla lista creata precedentemente tutti i generi

        except Exception:
            print("Errore durante l'esecuzione della query")   #messaggio da stampare se la query non è stata eseguita correttamente
            result = None

        cursor.close()                                        #chiudo il cursore
        cnx.close()                                           #chiudo la connessione
        return result                                         #ritorno la lista contenente tutti i generi


    #funzione che restituisce tutti i libri filtrati per genere e biblioteca selezionati
    def read_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()                      #apro la connessione
        if cnx is None:                                       #controllo se la connessione sia andata a buon fine
            print("Errore nella connessione al database")
            return None

        result = []                                             #creo la lista che conterrà i libri da ritornare
        cursor = cnx.cursor(dictionary=True)                    #creo un cursore "dizionario"
        #creo la query che mi restituisca i libri filtrati per genere e biblioteca selezionati
        query = """ SELECT l.*
                    FROM libro l, biblioteca b
                    WHERE b.nome = COALESCE(%s,b.nome) and l.genere = COALESCE(%s,l.genere) and l.id_biblioteca = b.id """
        try:
            cursor.execute(query, (biblioteca, genere,))         #provo ad eseguire la query
            for row in cursor:
                libro = Libro(id=row["id"], titolo=row["titolo"], autore=row["autore"], genere=row["genere"],
                              anno_pubblicazione=row["anno_pubblicazione"], id_biblioteca=row["id_biblioteca"])
                result.append(libro)     #itero il cursore e appendo alla lista creata precedentemente i libri filtrati
        except Exception:
            print("Errore durante l'esecuzione della query")    #messaggio da stampare se la query non è stata eseguita correttamente
            result = None

        cursor.close()                  #chiudo il cursore
        cnx.close()                     #chiudo la connessione
        return result                   #ritorno la lista contenente i libri filtrati per genere e biblioteca
