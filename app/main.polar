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

# This rule tells Oso how to fetch roles for a user
has_role(actor, role_name, repository: Repository) if
  role in actor.roles and
  role matches { name: role_name, repository: repository };

allow(actor, action, resource) if
  has_permission(actor, action, resource);
