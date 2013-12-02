import core
import algorithms
import helper

__name__ = "main"
try:
    h = helper.FacebookHelper()
    user = h.get_facebook_user("me")
    print user
    print user.favorite_athletes
    print user.languages
    print user.sports
except core.AppException as ex:
    print ex
    

