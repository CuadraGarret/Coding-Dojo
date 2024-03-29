from mysqlconnection import connectToMySQL

class User:
    db = "users_schema"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query  = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        all_users = []
        for user in results:
            all_users.append(cls(user))
        return all_users
    
    @classmethod
    def get_one(cls, user_id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = """UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s;"""
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete(cls, user_id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL('users_schema').query_db(query, data)