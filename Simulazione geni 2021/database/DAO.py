from database.DB_connect import DBConnect
from model.Gene import Genes


class DAO():

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct g.*
                        from genes g 
                        where g.Essential = 'Essential'
                        group by g.GeneID"""

            cursor.execute(query)

            for row in cursor:
                result.append(Genes(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_geneID():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct g.GeneID as GeneID
                            from genes g 
                            where g.Essential = 'Essential'
                            order by g.GeneID asc"""

            cursor.execute(query)

            for row in cursor:
                result.append(row["GeneID"])

            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getAllConnectedGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g1.GeneID as gene1, g1.Chromosome as c1, g2.GeneID as gene2, g2.Chromosome as c2, i.Expression_Corr as peso
                    from genes g1, genes g2, interactions i 
                    where g1.GeneID <> g2.GeneID 
                    and g1.GeneID = i.GeneID1 
                    and g2.GeneID = i.GeneID2
                    group by gene1, gene2 """

        cursor.execute(query)


        for row in cursor:
            result.append((row["gene1"], row["c1"], row["gene2"], row["c2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


