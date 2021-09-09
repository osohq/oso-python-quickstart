# docs: start-declaration
actor User {}

resource Repository {
	permissions = ["read", "push", "delete"];
	roles = ["contributor", "maintainer", "admin"];

	"read" if "contributor";
	"push" if "maintainer";
	"delete" if "admin";

	"maintainer" if "admin";
	"contributor" if "maintainer";
}
# docs: end-declaration

# docs: start-has-role
has_role(user: User, role_name, resource) if
    role in user.roles and
    role_name = role.name and
    resource = role.resource;
# docs: end-has-role

# docs: start-allow
allow(actor, action, resource) if
    has_permission(actor, action, resource);
# docs: end-allow
