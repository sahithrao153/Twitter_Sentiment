import MySQLdb


def connect():
    db = MySQLdb.connect('127.0.0.1', 'root', 'root', 'riesen')
    cursor = db.cursor()
    sql = "SHOW TABLES"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)


connect()
