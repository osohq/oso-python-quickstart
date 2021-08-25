allow(actor, action, resource) if
    role_allows(actor, action, resource);

actor_has_role_for_resource(actor, role_name, _resource) if
    role_name = actor.role;

resource(_type: Page, "page", actions, roles) if
    actions = ["read", "write"] and
    roles = {
        guest: {
            permissions: ["read"]
        },
        admin: {
            permissions: ["write", "read"]
        }
    };
