from pyleapcard import *
from pprint import pprint



def get_leap(username,password):
    try:
        session = LeapSession()
        session.try_login(username,password)
        overview = session.get_card_overview()
        pprint(vars(overview))
        return overview
    except Exception as E:
        print(E)