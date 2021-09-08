from flask import Flask
from .model import User, Repository
from oso import Oso, NotFoundError

oso = Oso()
oso.load_file("main.polar")
oso.register_class(User)
oso.register_class(Repository)

app = Flask(__name__)


@app.route("/repo/<slug>")
def repo_show(slug):
    repo = Repository.get_repo(slug)

    try:
        oso.authorize(User.get_current_user(), "read", repo)
        return f"<h1>A Repo</h1><p>Welcome to repo {repo.name}</p>", 200
    except NotFoundError:
        return f"<h1>Whoops!</h1><p>That repo was not found</p>", 404
