allow(actor, action, resource) if
    role_allow(actor, action, resource);

actor_role(actor, role) if
    role in actor.get_roles();

resource(_type: Page, "page", actions, roles) if
    actions = ["read", "write"] and
    roles = {
        admin: {
            permissions: ["write"],
            implies: ["user"]
        },
        user: {
            permissions: ["read"]
        }
    };
