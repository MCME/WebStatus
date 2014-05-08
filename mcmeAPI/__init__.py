import logging
from flask import Flask
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

import mcmeAPI.endpoints



#---------#
# logging #
#---------#
file_handler = RotatingFileHandler('./logs/mcmeAPI.log', maxBytes=200000, backupCount=5)
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('\n'+'*'*80+'\n[%(asctime)s] [%(levelname)s] [%(message)s]'+'\n'+'*'*80)
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)


from db import init_db, db_session
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# class Front(Handler):
#     def get(self):
#         self.write('MCME API')

# class UpdateRanks(Handler):
#     def get(self):
#         update_rank_db()

# class UpdateServers(Handler):
# 	def get(self):
# 		update_server_db()

