from database.DB_connect import DBConnect
from model.aereoporto import Aereoporto


class DAO():
    @staticmethod
    def getAllNodes():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select a.ID ,a.AIRPORT 
                          from extflightdelays.airports a  
                         """)  # questo valore si sostituisce a %s
        lista = cursor.fetchall()

        risultati = []
        for diz in lista:
            dto = Aereoporto(diz["ID"],diz["AIRPORT"])
            risultati.append(dto)

        cursor.close()
        cnx.close()
        return risultati

    @staticmethod
    def getArchi(dist):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as a1, GREATEST(f.DESTINATION_AIRPORT_ID,f.ORIGIN_AIRPORT_ID) as a2,AVG(f.DISTANCE) as d
                          from extflightdelays.flights f 
                          group by LEAST(f.ORIGIN_AIRPORT_ID,f.DESTINATION_AIRPORT_ID), greatest(f.DESTINATION_AIRPORT_ID,f.ORIGIN_AIRPORT_ID) 
                          having d>%s
                             """, (dist,))  # questo valore si sostituisce a %s
        lista = cursor.fetchall()

        risultati = []
        for diz in lista: #tuple di (id_origine,id_dest,avgdist)
            dto = (diz["a1"], diz["a2"],diz["d"])
            risultati.append(dto)

        cursor.close()
        cnx.close()
        return risultati




