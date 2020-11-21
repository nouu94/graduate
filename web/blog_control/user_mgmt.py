#유저 관리 control 모듈
from flask_login import UserMixin
from db_model.mysql import conn_mysqldb

class User(UserMixin) :
    def __init__(self, user_id, user_email, blog_id) :
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self) :
        return str(self.id)

    #user_id로 db의 레코드를 찾을 수 있는 기능
    @staticmethod
    def get(user_id) :
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
        # print(sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user :
            return None
        
        user = User(user_id = user[0], user_email = user[1], blog_id = user[2])
        return user


    # 이메일로 db의 레코드를 찾을 수 있는 기능
    @staticmethod
    def find(user_email) :
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + str(user_email) + "'"
        # print(sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user :
            return None
        
        user = User(user_id = user[0], user_email = user[1], blog_id = user[2])
        return user


    #데이터를 넣는 기능
    @staticmethod
    def create(user_email, blog_id) :
        user = User.find(user_email)
        if user == None :
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" %(str(user_email), str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else : 
            return user


    @staticmethod
    def delete(user_id) :
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted

