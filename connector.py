__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAUpFj9N2IEBANZC2YgCd6ZAUW8YYMPMThsEzkRQsZBcVtUlzGy76wEZAZCZCWl9CeiaYGsmNdLkdzHSnC9acRXvnWwE3eFJF3cveOXc3V839D5eQJ1Y1SVeXoiAazVpyqpyKRSrSk1KZCBpXYlVKamqTunnj3CqHjC1jtV5TroLHidlsxYP7T8DMzx9WC9fJ0ZD'
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
            
        
