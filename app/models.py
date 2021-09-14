from dataclasses import dataclass
from typing import List


@dataclass
class Repository:
    name: str
    is_public: bool = False

    @staticmethod
    def get_by_name(name):
        return repos_db.get(name)


@dataclass
class Role:
    name: str
    repository: Repository


@dataclass
class User:
    roles: List[Role]

    @staticmethod
    def get_current_user():
        return users_db["larry"]


repos_db = {
    "gmail": Repository("gmail"),
    "react": Repository("react", is_public=True),
    "oso": Repository("oso"),
}

users_db = {
    "larry": User([Role(name="admin", repository=repos_db["gmail"])]),
    "anne": User([Role(name="maintainer", repository=repos_db["react"])]),
    "graham": User([Role(name="contributor", repository=repos_db["oso"])]),
}
