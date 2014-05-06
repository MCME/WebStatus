from flask import jsonify
from mcmeAPI import app
from mcmeAPI.ranks import get_ranks, update_user_db
from mcmeAPI.servers import get_status


@app.route('/')
def front():
    return 'MCME API'

@app.route('/ranks/update')
def update_ranks():
    update_user_db()
    return 'OK'

@app.route('/ranks', defaults={'rank': None})
@app.route('/ranks/<rank>')
def ranks(rank):
    if rank is None:
        return jsonify({'all_ranks':'everybody!'})
    else:
        rank_list = get_ranks(rank)
        if rank_list is not None:
            return jsonify({'rank':rank, 'players': rank_list, 'num_players': len(rank_list)})#rank.serialize)

        return jsonify({"error": "Can't find the rank '"+rank+"'"}), 404

# class ServerStats(Handler):
#     def __init(self, request, response):
#         super(ServerStats, self).__init__(request,response)
#         self.response.headers['Content-Type'] = 'application/json'

#     def get(self, server_name):
#         server = get_status(server_name)
#         if server is not None:
#             self.writeJSON(server.serialize)
#         else:
#             self.error(404)
#             self.writeJSON({"error":"Trouble connecting to server: "+server_name})