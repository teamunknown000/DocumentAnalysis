from server.config import connection
from typing import List,Any
from uuid import uuid4


class Question:
    
    def constructor_output(question : List[Any]) :
        return {
            "ID" : question[0],
            "QUESTION" : question[1],
            "ANSWER": question[2],
            "FILE" : question[3]
        }
    def init():
        return connection.execute('''
            CREATE TABLE IF NO EXISTS question (
            ID UUID PRIMARY KEY NOT NULL , 
            QUESTION TEXT NOT NULL,
            ANSWER TEXT NOT NULL,
            FILE UUID NOT NULL,
            FOREIGN KEY (FILE) REFERENCES file(ID)
                ON DELETE CASCADE
            );
            
        ''')
        
    def add_question(question,answer,file_id):
        cursor = connection.cursor()
        new_file_id = uuid4() 
        cursor.execute("INSERT INTO question VALUES(?,?,?,?)",(
           new_file_id,question,answer,file_id
        ))
        
        connection.commit()
        cursor.execute("""
            SELECT * FROM question WHERE ID = ?
                       """,(new_file_id))
        new_file_data = cursor.fetchone()
        return Question.constructor_output(new_file_data)
    
__table__ = Question
               
