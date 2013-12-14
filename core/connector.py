__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAJAHVHdeXZCVHuVTbZChzgjkTWa98Fzfv3f6esZCv1qBlXG3u2XYDn7rpPOBCyQb74ZC73ZBT1sJoxBuX85q2UifkJVYFjOYYRbzcOOmj9X3OgOF84JuUalZC3GUKbMAAEHQHqJgmuItzJqy3kXKOFPLdYNAT3k3oKRJuIuNJQylZCUwHwdpbTB03QTxjZCouAZDZD'
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
            
    
