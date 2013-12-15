__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAKZAoZB6IZCs1aKcpcASY3tfcaFu4KOsbxeD2IFRbACruqYMburxhgL7mI36Qg1EurH2hZAjNWavaV97QCsoH3ZBI9dP1xK3p5ZAy1rozrH4wMw3QRhbXQICDJB6YqLIEBMFjRpDncvpt6HIKNKDX56bI3AH3QpjPZB0tZBe2NP4rw1i0pApI8Tz8fe50MSIAQZDZD'
    def __init__(self):
        """ """
        try:
            self.graph = facebook.GraphAPI(self.ACCESS_TOKEN)
        except facebook.GraphAPIError as e:
            raise e
        
    def get_user(self, id):
        """ """
        try:
            out = self.graph.get_object(id)
            #print out
            return out
        except facebook.GraphAPIError as e:
            raise e 

    def get_friends(self,id):
        """ """
        try:
            out = self.graph.get_connections(id,"friends")
            return out
        except facebook.GraphAPIError as e:
            raise e

    def execute_fql(self, query):
        """ """
        try:
            out = self.graph.fql(query)
            return out
        except facebook.GraphAPIError as ge:
            raise ge
        except Exception as ex:
            print ex
            raise ex
            
    
