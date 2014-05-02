from mcmeAPI.utils import Handler
from mcmeAPI.ranks import update_rank_db
from mcmeAPI.servers import update_server_db

class Front(Handler):
    def get(self):
        self.write('MCME API')

class UpdateRanks(Handler):
    def get(self):
        update_rank_db()

class UpdateServers(Handler):
	def get(self):
		update_server_db()