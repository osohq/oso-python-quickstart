class Page:
    pages = []

    def __init__(self, pagenum):
        self.pagenum = pagenum

    @staticmethod
    def get_page(pagenum):
        num = int(pagenum)
        if num < len(Page.pages):
            return Page.pages[int(pagenum)]


Page.pages = [Page(0), Page(1), Page(2)]


ROLES = {
    "alice": [
        {"name": "guest", "resource": Page.pages[0]},
        {"name": "admin", "resource": Page.pages[1]},
    ],
    "bob": [{"name": "admin", "resource": Page.pages[2]}],
}


class User:
    def __init__(self, name):
        self.name = name

    # Get the user -- hardcoded as "bob"
    @staticmethod
    def get_current_user():
        return User("bob")

    # Get all the roles for this user
    def get_roles(self):
        global ROLES
        return ROLES[self.name]
