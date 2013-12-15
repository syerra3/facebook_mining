__name__ = "connector"

import facebook

class FacebookConnector:
    """ Class to communicate with Facebook REST API """

    #Facebook access token
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAKnMR9pf03N6sRkTXQc5FEiQUwquR5OB5kBZB99TW4mrPMChUKDVozAdRqez0rELyNDAcH8fxoraR0Eb9wZAF3au9tDzCun2X9QfshllOZC2rvBoFy2FhDbIsxRNjH8ZApwGtZBV8jg5kLHz23ylvN9KZA3X2IN6KiUz8lAtJJH6lh4nFDay0ZD'

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
    
