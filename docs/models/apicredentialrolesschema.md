# APICredentialRolesSchema


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_role`                                                  | [models.OrganizationRole](../models/organizationrole.md)             | :heavy_check_mark:                                                   | Organization-level Role assigned to the API Credential.              | admin                                                                |
| `workspaces`                                                         | List[[models.WorkspaceRoleSchema](../models/workspaceroleschema.md)] | :heavy_minus_sign:                                                   | Workspace-level Roles assigned to the API Credential.                |                                                                      |