import mysql.connector
from mysql.connector import errorcode
#----------------------------------------------------------------------
def connectDB(data, host='localhost', user = 'root', passwd = 'Serta45!@' ):
    try:
        db = mysql.connector.connect(host=host,
                                     user=user,
                                     passwd=passwd,
                                     database=data
                                    )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        db.close()

    cur = db.cursor()
    table = "use (%s)"
    cur.execute('use avitoDB')

    #print('sucessfull')
    return cur, db

#---------------------------------------------------------------------
#def connetcDB():
#    pass
#--------------------------------------------------------------------
def insertTable(arg1, arg2, title, price, metro, url):
    #print(type(arg1))
    try:
        hello = "insert into avitoData(title, price, metro, url)  values(%s, %s, %s, %s)"
        args = (title, price, metro, url)
        arg1.execute(hello, args)
        arg2.commit()
        print(args)
    except mysql.connector.Error as err:
        print(err)
        arg2.close()

    #print('execute')

#----------------------------------------------------------------------
def closeDB(arg1, arg2):
    arg1.close()
    arg2.close()
    #print('close')
#-----------------------------------------------------------------------
if __name__ == '__main__':
    m = connectDB(data='avitoDB')
    data = {
        'title' : '1',
        'price' : '2',
        'metro' : '3',
        'url'   : '4'

    }
    for i in range(0, 100):
        insertTable(*m, **data)
    closeDB(*m)
