from flask_app.config.mysqconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for i in results:
            dojos.append(cls(i))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s)"
        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(result[0])
        for i in result:
            nin = {
                'id': i['ninjas.id'],
                'first_name': i['first_name'],
                'last_name': i['last_name'],
                'age': i['age'],
                'created_at': i['created_at'],
                'updated_at': i['updated_at']
            }

            dojo.ninjas.append(Ninja(nin))
        return dojo
