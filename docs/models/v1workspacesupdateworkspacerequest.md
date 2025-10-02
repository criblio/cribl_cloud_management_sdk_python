# V1WorkspacesUpdateWorkspaceRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `organization_id`                                                        | *str*                                                                    | :heavy_check_mark:                                                       | The <code>id</code> of the Organization that contains the Workspace.     |
| `workspace_id`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | The <code>id</code> of the Workspace to update.                          |
| `workspace_patch_request_dto`                                            | [models.WorkspacePatchRequestDTO](../models/workspacepatchrequestdto.md) | :heavy_check_mark:                                                       | N/A                                                                      |