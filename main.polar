resource Repository {
	permissions = ["read", "push", "delete"];
	roles = ["contributor", "maintainer", "admin"];

	"read" if "contributor";
	"push" if "maintainer";
	"delete" if "admin";

	"maintainer" if "admin";
	"contributor" if "maintainer";
}
