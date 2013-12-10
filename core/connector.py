__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAFaZBGLsC8DdK3c12WmZA1iiyli7zHLD3rwO53n9o3PUiYDt5nZCfWEcd7tZASMi0yZC7BZB3BFWfgZAUZCL1IgLbMfTIfprf1n7AZBBpEpUhDbSLqZBiB0awB50DOE5bjZCtYll5txKdcNK4LaBqinjZCZAf97zVI480LvJ9cjaH3oKMxO2zZAL39HkeRk9oycXGAJAZDZD'
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
            
    
