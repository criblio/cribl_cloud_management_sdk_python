# V1APICredentialsUpdateAPICredentialRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `organization_id`                                                                  | *str*                                                                              | :heavy_check_mark:                                                                 | The <code>id</code> of the Organization whose API Credential you want to update.   |
| `api_credential_id`                                                                | *str*                                                                              | :heavy_check_mark:                                                                 | The <code>clientId</code> of the API Credential to update.                         |
| `api_credential_update_request_dto`                                                | [models.APICredentialUpdateRequestDTO](../models/apicredentialupdaterequestdto.md) | :heavy_check_mark:                                                                 | N/A                                                                                |