# WorkspaceRoleSchema


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `workspace_id`                                                   | *str*                                                            | :heavy_check_mark:                                               | Workspace identifier                                             | main                                                             |
| `workspace_role`                                                 | [models.WorkspaceRole](../models/workspacerole.md)               | :heavy_check_mark:                                               | Role in the workspace                                            | admin                                                            |
| `products`                                                       | List[[models.ProductRoleSchema](../models/productroleschema.md)] | :heavy_minus_sign:                                               | Product roles in the workspace                                   |                                                                  |