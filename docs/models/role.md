# Role

Role assigned to the API Credential on the product.

## Example Usage

```python
from cribl_mgmt_plane.models import Role

value = Role.ADMIN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ADMIN`    | admin      |
| `EDITOR`   | editor     |
| `READER`   | reader     |
| `USER`     | user       |
| `NOACCESS` | noaccess   |