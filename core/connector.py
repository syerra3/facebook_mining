__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAKKomd1b4lPagtRXtZB4ZAqfTRZCDHCuf3582iYIiuK12HwKNjCCzkuOhtCy3w4pZAGe5vAsjKjBx35CMXLTriZCZB8Vc5RR1wpZASQCZAksLD0brvLLb5ZAHoQ1QSdQmPLVz8OYdosZARZBQP27bOMubTgww2sZB6ZAcwia2LiJLZBom5MqHBeav1vPJRdFflX2wo0QZDZD'
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

    
            
        
