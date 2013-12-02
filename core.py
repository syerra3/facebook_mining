# first commit
__name__ = "core"


class AppException(Exception):
    """ """
    def __init__(self,value):
        self.message = value

    def __str__(self):
        return repr(self.message)

class User:
    """ """
    def __init__(self):
        """ """
        self.name = ''
        self.gender = ''
        self.relationship_status = ''
        self.hometown = ''
        self.location = ''
        self.religion = ''
        self.birthday = None
        self.favorite_athletes = None
        self.education = None
        self.sports = None
        self.languages = None
        self.work = None

    def __str__(self):
        """ """
        return str(self.name +', '+self.religion+', '+self.gender+', '
                   +self.relationship_status+', '+self.hometown+', '
                   +self.location)
        
