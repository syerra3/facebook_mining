__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAHZAkpHNzZBEBACHIXx3zOZAFkCVGITVXhOUDIbFK60oSuRmrnRr3g7Noze4NyavONUSEdmYfAIIoZA2v04dzH3LgmHwCCZBNc7v9xuTwEgrDpFc8UnpDYegIZBdvSQAkpQdx3KOec3o1tGZArTpijPqoIyGsoTiAuBOohc6s6f9OdBkbr5PbcKZAQLraazSOYkovMwnBjQoAZDZD'
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
            
        
