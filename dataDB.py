import MySQLdb
#----------------------------------------------------------------------
def connectDB(data, host='localhost', user = 'root', passwd = 'Serta45!@' ):
    """
    :param data: название базы данных
    :param host: по умолчанию локальная машина 'localhost'
    :param user: имя пользователя по умолчанию 'root'
    :param passwd: пароль для базы данных
    :return: cur, bd
    """
    try:
        db = MySQLdb.connect(host=host,
                            user=user,
                            passwd=passwd,
                            db=data
                            )
    except MySQLdb.Error as err:
        #if err == MySQLdb.ER_ACCESS_DENIED_ERROR: #errorcode.ER_ACCESS_DENIED_ERROR:
        #    print("Something is wrong with your user or password")
        #if err == MySQLdb.OperationalError():
        #    print("Unknow database %s", data)
        #else:
        print(err)
        db.close()

    cur = db.cursor()
    format = "use " + data
    cur.execute(format)

    print('sucessfull')
    return cur, db
#---------------------------------------------------------------------
def insertTable(cur, db, title, price, metro, url):
    """
    Запись данных в таблицу avitoData.
    :param cur:  курсор
    :param db:  база данных
    :param title: заголовок
    :param price: цена
    :param metro: станция метро
    :param url: url страницы
    """
    try:
        hello = "insert into avitoData(title, price, metro, url)  values(%s, %s, %s, %s)"
        args = (title, price, metro, url)
        cur.execute(hello, args)
        db.commit()
        print(args)
    except MySQLdb.Error as err:
        print(err)
        cur.close()
        db.close()
#---------------------------------------------------------------------
def sortedTable():
    pass
#----------------------------------------------------------------------
def closeDB(cur, db):
    """
    Закрытие базы данных.
    """
    cur.close()
    db.close()
    #print('close')
#-----------------------------------------------------------------------
if __name__ == '__main__':
    db = connectDB(data='avitoDB')
    data = {
        'title' : '1',
        'price' : '2',
        'metro' : '3',
        'url'   : '4'
    }
    for i in range(0, 10):
        insertTable(*db, **data)
    closeDB(*db)
