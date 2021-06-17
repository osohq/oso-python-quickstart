
actor_role(actor, role) if
    resources = Page.pages and
    r in resources and
    actions = r.has_roles(actor) and
    action in actions and
    role = { name: action, resource: r };

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