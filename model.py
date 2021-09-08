from dataclasses import dataclass
from typing import List


@dataclass
class Repository:
    name: str

    @classmethod
    def get_by_id(id):
        return repos_db.get(id)


@dataclass
class User:
    roles: List[dict]

    @classmethod
    def get_current_user():
        return users_db["larry"]


repos_db = {
    "gmail": Repository("gmail"),
    "react": Repository("react"),
    "oso": Repository("oso"),
}

users_db = {
    "larry": User([{"name": "admin", "resource": repos_db["gmail"]}]),
    "anne": User([{"name": "maintainer", "resource": repos_db["react"]}]),
    "graham": User([{"name": "contributor", "resource": repos_db["oso"]}]),
    # TODO: more?
}
