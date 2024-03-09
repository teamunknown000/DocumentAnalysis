from server.config import connection
from typing import List,Any
from uuid import uuid4




class File :
    def constructor_output(file : List[Any]) :
        return {
            "ID" : file[0],
            "EMAIL" : file[1],
            "FILE_PATH": file[2],
            "CONTENT" : file[3]
            
        }
    
    def init() :
        return connection.execute('''
            CREATE TABLE IF NO EXISTS file (
                ID UUID PRIMARY KEY NOT NULL , 
                EMAIL TEXT NOT NULL,
                FILE_PATH TEXT NOT NULL,
                CONTENT TEXT,
                FOREIGN KEY (EMAIL) REFERENCES user(EMAIL)
                    ON DELETE CASCADE
            );
        ''')
    
    def add_file(email,file_path,content):
        cursor = connection.cursor()
        new_file_id = uuid4()
        cursor.execute("INSERT INTO file VALUES(?,?,?,?)",(
            new_file_id,email, file_path,content,
        ))
        
        connection.commit()
        
        cursor.execute("""
            SELECT ID, EMAIL, FILE_PATH FROM file WHERE ID = ?
        """, (new_file_id,))
        new_file_data = cursor.fetchone()
        
        return File.constructor_output(new_file_data)
    
__table__ = File
        
    
        
        