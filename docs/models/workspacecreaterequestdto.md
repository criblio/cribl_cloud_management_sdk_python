# WorkspaceCreateRequestDTO


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `workspace_id`                                         | *str*                                                  | :heavy_check_mark:                                     | Unique identifier for the Workspace.                   | main                                                   |
| `alias`                                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | User-friendly alias for the Workspace.                 | Production Environment                                 |
| `description`                                          | *Optional[str]*                                        | :heavy_minus_sign:                                     | Brief description of the Workspace.                    | Main production Workspace for customer data processing |
| `tags`                                                 | List[*str*]                                            | :heavy_minus_sign:                                     | Tags associated with the Workspace.                    | [<br/>"production",<br/>"customer-data"<br/>]          |