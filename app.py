from flask import Flask
from oso import Oso

from models import Page, User

# Create the Flask app
app = Flask(__name__)

# Setup Oso
oso = Oso()
oso.enable_roles()
oso.register_class(Page)
oso.register_class(User)
oso.load_file("authorization.polar")


@app.route("/page/<pagenum>")
def page_show(pagenum):
    page = Page.get_page(pagenum)
    if oso.is_allowed(
        User.get_current_user(),  # the user doing the request
        "read",  # the action we want to do
        page,  # the resource we want to do it to
    ):
        return f"<h1>A Page</h1><p>this is page {pagenum}</p>", 200
    else:
        return f"<h1>Sorry</h1><p>You are not allowed to see this page</p>", 403
