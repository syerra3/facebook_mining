__name__ = "connector"

import facebook

class FacebookConnector:
    """ """
    ACCESS_TOKEN = 'CAAUpFj9N2IEBAF4ykOEqZBiry9TnhVF4Xzd7sE4lBb2wiU1S91RYQgsWHVePvUEKMvtmfcMbRqksK6hTy05S5wUlA0lWcqGyK89FWb6DjRlFQJQpZBbsSxkhkBnwi5YqV99x1KZBNzBcXJ8KPXXtwNoQTf9YqZCDOGvThZBYCiHdZA5u0xzyX5870XCMZACfhkZD'
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

    
            
        
