from lib.minecraft_query import MinecraftQuery

from mcmeAPI.utils import Handler
from mcmeAPI.ranks import get_ranks
from mcmeAPI.servers import get_status

@app.route('/ranks' defaults={'rank': None})
@app.route('/ranks/<rank>')
def ranks(rank):
    def get(self, path=None, json=None):
        if not path:
            self.writeJSON({'all_ranks':'everybody!'})
        else:
            rank = get_ranks(path.lstrip('/'))
            if rank is not None:
                if json:
                    self.writeJSON(rank.serialize)
                else:
                    #render html page
                    self.response.headers['Content-Type'] = 'text/html'
                    self.render('ranks.html', rank=rank)
            else:
                self.error(404)
                self.writeJSON({"error": "Can't find the rank '"+path.lstrip('/')+"'"})

class ServerStats(Handler):
    def __init(self, request, response):
        super(ServerStats, self).__init__(request,response)
        self.response.headers['Content-Type'] = 'application/json'

    def get(self, server_name):
        server = get_status(server_name)
        if server is not None:
            self.writeJSON(server.serialize)
        else:
            self.error(404)
            self.writeJSON({"error":"Trouble connecting to server: "+server_name})