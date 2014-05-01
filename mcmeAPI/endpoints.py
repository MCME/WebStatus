from mcmeAPI.utils import Handler

class Ranks(Handler):
    def __init__(self, request, response):
        super(Ranks, self).__init__(request, response)
        self.response.headers['Content-Type'] = 'application/json'

    def get(self, path):
        if not path:
            self.writeJSON({'all_ranks':'everybody!'})
        else:
            self.writeJSON({'path':path})