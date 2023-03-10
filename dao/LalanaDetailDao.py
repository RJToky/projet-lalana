from connection.Bdd import Bdd
from model.LalanaDetail import LalanaDetail

class LalanaDetailDAO:
    @staticmethod
    def find_by_id(con, id: int) -> LalanaDetail:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from lalanaDetail
                where idLalana = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = LalanaDetail(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep

    @staticmethod
    def find_all(con):
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from lalanaDetail
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = LalanaDetail(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep