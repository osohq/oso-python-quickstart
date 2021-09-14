from flask import Flask
from oso import Oso, NotFoundError
from .models import User, Repository

# Initialize the Oso object. This object is usually used globally throughout
# an application.
oso = Oso()

# Tell Oso about the data you will authorize. These types can be referenced
# in the policy.
oso.register_class(User)
oso.register_class(Repository)

# Load your policy files.
oso.load_files(["app/main.polar"])

app = Flask(__name__)


@app.route("/repo/<name>")
def repo_show(name):
    repo = Repository.get_by_name(name)

    try:
        oso.authorize(User.get_current_user(), "read", repo)
        return f"<h1>A Repo</h1><p>Welcome to repo {repo.name}</p>", 200
    except NotFoundError:
        return f"<h1>Whoops!</h1><p>Repo named {name} was not found</p>", 404
