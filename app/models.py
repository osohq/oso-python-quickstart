from dataclasses import dataclass
from typing import List, Union

from flask import g

Resource = Union['Repository']


@dataclass
class Repository:
    name: str

    @staticmethod
    def get_by_name(name):
        return repos_db.get(name)


@dataclass
class Role:
    name: str
    resource: Resource


@dataclass
class User:
    roles: List[Role]

    @staticmethod
    def get_by_name(name):
        return users_db[name]

    @staticmethod
    def set_current_user(user):
        g.user = user

    @staticmethod
    def get_current_user():
        return g.user


repos_db = {
    "gmail": Repository("gmail"),
    "react": Repository("react"),
    "oso": Repository("oso"),
}

users_db = {
    "larry": User([Role(name="admin", resource=repos_db["gmail"])]),
    "anne": User([Role(name="maintainer", resource=repos_db["react"])]),
    "graham": User([Role(name="contributor", resource=repos_db["oso"])]),
    # TODO: more?
}
