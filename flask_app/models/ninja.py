from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    db_name='dojos_ninjas'
    def __init__(self,data):
        self.id=data['id'],
        self.frist_name=data['frist_name'],
        self.last_name=data['last_name'],
        self.age=data['age'],
        self.created_at=data['created_at'],
        self.update_at=data['update_at']


    @classmethod
    def create_ninja(cls,data):
        query="INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES ( %(dojo_id)s, %(first_name)s,%(last_name)s, %(age)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def get_all_ninjas(cls,data):
        query="SELECT * FROM ninjas"
        return connectToMySQL(cls.db_name).query_db(query,data)
        
    @classmethod
    def get_all_ninjas_dojo(cls,data):
        query="SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        result=connectToMySQL(cls.db_name).query_db(query,data)
        ninjas = []
        for row in result:
            ninjas.append(row)
        return ninjas