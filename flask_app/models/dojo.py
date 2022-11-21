from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    db_name='dojos_ninjas'
    def __init__(self,data):
        self.id=data['id'],
        self.name=data['name'],
        self.created_at=data['created_at'],
        self.update_at=data['update_at']

    @classmethod
    def getAllDojos(cls):
        query ='SELECT * FROM dojos;'
        results = connectToMySQL(cls.db_name).query_db(query)
        dojos = []
        for row in results:
            dojos.append(row)
        return dojos


    @classmethod
    def create_dojo(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete_dojo(cls,data):
        query="DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


    @classmethod
    def get_dojos_by_id(cls,data):
        query="SELECT * FROM dojos WHERE id=%(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results[0]


    
