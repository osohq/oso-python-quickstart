from pathlib import Path

from flask import Flask, request
from oso import Oso, NotFoundError

from .models import User, Repository

APP_DIR = Path(__file__).parent

# docs: start-setup

# Initialize the Oso object. This object is usually used globally throughout
# an application.
oso = Oso()

# Tell Oso about the data you will authorize. These types can be referenced
# in the policy.
oso.register_class(User)
oso.register_class(Repository)


# Load your policy files.
oso.load_files([APP_DIR / "main.polar"])

# docs: end-setup

app = Flask(__name__)


@app.before_request
def get_user():
    username = request.headers['user']
    user = User.get_by_name(username)
    if user is None:
        return f"<p>Unable to find user with name {username}.</p", 401

    User.set_current_user(user)


@app.route("/repo/<name>")
def repo_show(name):
    repo = Repository.get_by_name(name)

    try:
        print(User.get_current_user(), "read", repo)
        oso.authorize(User.get_current_user(), "read", repo)
        return f"<h1>A Repo</h1><p>Welcome to repo {repo.name}</p>", 200
    except NotFoundError:
        return f"<h1>Whoops!</h1><p>Repo named {name} was not found</p>", 404
