__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBALrYAwPKcI7HqfDEALYEAvibZAe8J6ZChLaa2rU9k7vbc2TKj3Gpi31KCVHJ1FxqOjxnZAyCEZCZAfzc4cI5gkTj2DEg0Yvb8GkjGmWNrIrMr5ZAgJiMABkeExRv9SyZA0l3DBaXZCWB2Je7MIMLQT0SZAi7dXSQ5ZCpDIUxmnkhYBJu9dWCVJFgIZD'
    def __init__(self):
        """ """
        try:
            self.graph = facebook.GraphAPI(self.ACCESS_TOKEN)
        except:
            raise
        
    def get_user(self, id):
        """ """
        try:
            out = self.graph.get_object(id)
            return out
        except Exception as e:
            raise e 

    def get_friends(self,id):
        """ """
        try:
            out = self.graph.get_connections(id,"friends")
            return out
        except Exception as e:
            raise e

    
            
        
