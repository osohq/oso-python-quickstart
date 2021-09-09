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

has_role(actor, role_name, resource) if
  role in actor.roles and
  role matches { name: role_name, resource: resource };

allow(actor, action, resource) if
  has_permission(actor, action, resource);
