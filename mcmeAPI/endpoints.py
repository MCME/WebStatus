import json
from flask import jsonify
from mcmeAPI import app
from mcmeAPI.users import get_user_group, get_user, update_user_db
from mcmeAPI.servers import get_status, update_server_db


@app.route('/')
def front():
    return 'MCME API'

@app.route('/users/update')
def update_ranks():
    update_user_db()
    return 'OK'

@app.route('/export/<group>')
def ranks(group):
    group_list = get_user_group(group)
    if len(group_list) > 0:
        return jsonify({'group':group, 'players': group_list, 'num_players': len(group_list)})#group.serialize)

    return jsonify({"error": "Can't find the group '"+group+"'"}), 404

@app.route('/export/user/<user_name>')
def users(user_name):
    user = get_user(user_name)
    if user is not None:
        return jsonify(user.serialize)

    return jsonify({"error": "Can't find the user '"+user_name+"'"}), 404

@app.route('/server/<server_name>')
def servers(server_name):
    server = get_status(server_name)
    if server is not None:
        return jsonify(server.serialize)
    else:
        return jsonify({"error": "Trouble connecting to the server '"+server_name+"'"}), 404

@app.route('/server/update')
def update_servers():
    update_server_db()
    return 'OK'

