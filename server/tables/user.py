from server.config import connection
from typing import List,Any

class User:
    def construct_output(user: List[Any]):
        return {
            "email" : user[0],
            "name" : user[1],
            "password" : user[2]
        }
    
    def init():
        return connection.execute('''CREATE TABLE if not exists user(
            
            EMAIL TEXT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            PASSWORD  TEXT  NOT NULL);
        ''')
        

    def add_user(name, email, password):
        cursor = connection.cursor() 
        cursor.execute("SELECT EMAIL FROM USER WHERE EMAIL = ?",(email,))
        existing_user = cursor.fetchone()
        if existing_user != None:
            return None
        cursor = connection.cursor()
        res = connection.execute("INSERT INTO user VALUES(?,?,?)",(
            email, name, password,
        ))
        connection.commit()
        
        cursor.execute("SELECT * FROM USER WHERE EMAIL= ?",(email,))
        created_user = cursor.fetchone()
        return User.construct_output(created_user)
    
    def get_user(email,password):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USER WHERE EMAIL= ? AND PASSWORD= ?",(email,password,))
        getUser = cursor.fetchone()
        if not getUser :
            return None
        return User.construct_output(getUser)
    
__table__ = User