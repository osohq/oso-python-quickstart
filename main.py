# docs: begin-import
from oso import Oso
oso = Oso()
# docs: end-import

class Page:
    def __init__(self, contents):
        self.contents = contents

class User:
    def __init__(self, role):
        self.role = role

# docs: begin-register-class
oso.register_class(Page)
# docs: end-register-class

# docs: begin-load-file
oso.load_file("authorization.polar")
# docs: end-load-file
oso.enable_roles()

# docs: begin-appcode
page = Page(contents="a readable page")
if oso.is_allowed(
        User(role="guest"),  # the user doing the request
        "read",  # the action we want to do
        page,  # the resource we want to do it to
        ):
    print(page.contents)
else:
    raise Exception("Forbidden")
# docs: end-appcode

# docs: begin-assertions
# The "guest" role has the "read" permission, so they can read a page
assert oso.is_allowed(User(role="guest"), "read", Page("readable page"))

# The "guest" role does not have the "write" permission, so they're
# forbidden from writing to a page
assert not oso.is_allowed(User(role="guest"), "write", Page("readable page"))

# The "admin" role can write to page
assert oso.is_allowed(User(role="admin"), "write", Page("readable page"))
# docs: end-assertions
