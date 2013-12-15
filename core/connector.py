__name__ = "connector"

import facebook

class FacebookConnector:
    """ Class to communicate with Facebook REST API """

    #Facebook access token
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAKZAoZB6IZCs1aKcpcASY3tfcaFu4KOsbxeD2IFRbACruqYMburxhgL7mI36Qg1EurH2hZAjNWavaV97QCsoH3ZBI9dP1xK3p5ZAy1rozrH4wMw3QRhbXQICDJB6YqLIEBMFjRpDncvpt6HIKNKDX56bI3AH3QpjPZB0tZBe2NP4rw1i0pApI8Tz8fe50MSIAQZDZD'

    def __init__(self):
        """ constructor """
        try:
            self.graph = facebook.GraphAPI(self.ACCESS_TOKEN)
        except facebook.GraphAPIError as e:
            raise e
        
    def get_user(self, id):
        """ returns object for given id """
        try:
            out = self.graph.get_object(id)
            #print out
            return out
        except facebook.GraphAPIError as e:
            raise e 

    def get_friends(self,id):
        """ returns connections for given id  """
        try:
            out = self.graph.get_connections(id,"friends")
            return out
        except facebook.GraphAPIError as e:
            raise e
    
