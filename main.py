# import os, sys

# PROJECT_DIR = '/www/helloflask.enigmeta.com/helloflask'

# activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
# execfile(activate_this, dict(__file__=activate_this))
# sys.path.append(PROJECT_DIR)


from mcmeAPI import app as application

if __name__ == '__main__':
    application.run()




# import webapp2, sys

# from mcmeAPI import Front, UpdateRanks, UpdateServers
# from mcmeAPI.endpoints import *

# app = webapp2.WSGIApplication([
#     (r'/', Front),
#     (r'/ranks/update', UpdateRanks),
#     (r'/ranks', Ranks),
#     (r'/ranks/([A-Za-z]+)(.json)?', Ranks),
#     (r'/server/(build|freebuild)', ServerStats),
#     (r'/server/update', UpdateServers)


# ], debug=True)

# def main():
    # run_wsgi_app(application)
    
# if __name__ == '__main__':
    # main()

    #cfmqfzjylhjioskv