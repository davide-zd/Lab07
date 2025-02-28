from database.DB_connect import DBConnect
from model.situazione import Situazione


class DAO():

    @staticmethod
    def get_misure(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s.Localita, s.Data, AVG(s.Umidita) Umidita
                        from situazione s 
                        where MONTH(Data) = %s
                        group by s.Localita"""
            cursor.execute(query, (mese, ))
            for row in cursor:
                result.append(Situazione(**row))
            cursor.close()
            cnx.close()
        return result


