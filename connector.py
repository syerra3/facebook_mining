__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBAHwNpIy1mRHgGrM5Cdtqbyp788dkD9ch557MboJ6rJ8Nr1xg34pPWzffOSu5BC0ZCtZAWbrc6yTQG8wCi544xnfBzgHo3Gjsg3maglSPVg31i4lvIlkI0ACWMngNC8UOHbGa8u7I6pi0S6DKBnj0SWs9N4ZAHTPuyVc5ALPCsPuP2qhxtIclDvcjWikmgZDZD'
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
            
        
