import webapp2, sys

from mcmeAPI import Front, UpdateRanks
from mcmeAPI.endpoints import *

app = webapp2.WSGIApplication([
    (r'/', Front),
    (r'/ranks/update', UpdateRanks),
    (r'/ranks(/?[A-Za-z]*)', Ranks),


], debug=True)

# def main():
    # run_wsgi_app(application)
    
# if __name__ == '__main__':
    # main()