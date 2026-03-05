# State

Current state of the Workspace.

## Example Usage

```python
from cribl_mgmt_plane.models import State

value = State.PROVISIONING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `PROVISIONING`   | Provisioning     |
| `ACTIVE`         | Active           |
| `INACTIVE`       | Inactive         |
| `FAILED`         | Failed           |
| `DEPROVISIONING` | Deprovisioning   |