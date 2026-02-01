# APICredentialRolesSchema


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_role`                                                  | [models.OrganizationRole](../models/organizationrole.md)             | :heavy_check_mark:                                                   | Organization-level role                                              | admin                                                                |
| `workspaces`                                                         | List[[models.WorkspaceRoleSchema](../models/workspaceroleschema.md)] | :heavy_minus_sign:                                                   | Workspace roles assigned to this credential                          |                                                                      |