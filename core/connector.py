__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAUpFj9N2IEBAHJ2GoM9h1TZAUng3T3Tmxz1fWsKZChi6ppOn9uIiyWfakiwzCc8tnZB32Se2pehlV15n0dokcoQu4ZBaUkhWQ2JQRYjliy98AGPuJz30YMNeksZCcI7OOxHwtdpiUOymB0a65b3wAiaVowfMKXyYWtLTH5knZBEq6nyPXAoNa56z1HY96K0MZD'
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
        except:
            raise

    def get_friends(self,id):
        """ """
        try:
            out = self.graph.get_connections(id,"friends")
            return out
        except Exception as e:
            raise e

    
            
        
