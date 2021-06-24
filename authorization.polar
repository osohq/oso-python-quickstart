allow(actor, action, resource) if
    role_allow(actor, action, resource);

actor_has_role_for_resource(actor, role_name, resource) if
    role in actor.get_roles() and
    role_name = role.name and
    resource = role.resource;

resource(_type: Page, "page", actions, roles) if
    actions = ["read", "write"] and
    roles = {
        user: {
            permissions: ["read"]
        },
        admin: {
            permissions: ["write"],
            implies: ["user"]
        }
    };
