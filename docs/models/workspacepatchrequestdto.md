# WorkspacePatchRequestDTO


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `alias`                                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | User-friendly alias for the workspace                  | Production Environment                                 |
| `description`                                          | *Optional[str]*                                        | :heavy_minus_sign:                                     | Detailed description of the workspace                  | Main production workspace for customer data processing |
| `tags`                                                 | List[*str*]                                            | :heavy_minus_sign:                                     | Tags associated with the workspace                     | [<br/>"production",<br/>"customer-data"<br/>]          |