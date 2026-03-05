# WorkspaceRole

Role assigned to the API Credential on the Workspace.

## Example Usage

```python
from cribl_mgmt_plane.models import WorkspaceRole

value = WorkspaceRole.OWNER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `OWNER`    | owner      |
| `ADMIN`    | admin      |
| `USER`     | user       |
| `NOACCESS` | noaccess   |