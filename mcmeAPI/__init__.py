from mcmeAPI.utils import Handler
from mcmeAPI.ranks import update_rank_db

class Front(Handler):
    def get(self):
        self.write('MCME API')

class UpdateRanks(Handler):
    def get(self):
        update_rank_db()