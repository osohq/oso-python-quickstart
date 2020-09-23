from http.server import HTTPServer, BaseHTTPRequestHandler
from oso import Oso

from quickstart.expense import db, Expense

oso = Oso()
oso.register_class(Expense)
oso.load_file("expenses.polar")


class RequestHandler(BaseHTTPRequestHandler):
    def _respond(self, msg, code=200):
        self.send_response(code)
        self.end_headers()
        self.wfile.write(str(msg).encode() + b"\n")
        # self.wfile.write(b"\n")

    def do_GET(self):
        try:
            _, resource, id = self.path.split("/")
            if resource != "expenses":
                return self._respond("Not Found!", 404)
            expense = db[int(id)]
        except (ValueError, KeyError):
            return self._respond("Not Found!", 404)

        actor = self.headers.get("user", None)
        action = "GET"
        if oso.is_allowed(actor, action, expense):
            self._respond(expense)
        else:
            self._respond("Not Authorized!", 403)


if __name__ == "__main__":
    print("running on port 5050")
    HTTPServer(("", 5050), RequestHandler).serve_forever()
