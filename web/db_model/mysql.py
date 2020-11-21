import pymysql

MYSQL_CONN = pymysql.connect( # mysql을 파이썬 코드로 이용하여 연결
    host = "localhost",
    port = 3306,
    user = 'root',
    passwd = 'choi30133!',
    db = 'choongchung',
    charset = 'utf8'
)

def conn_mysqldb() :
    if not MYSQL_CONN.open :
        MYSQL_CONN.ping(reconnect = True) # mysql이 끊기면 다시 연결하는 함수
    return MYSQL_CONN