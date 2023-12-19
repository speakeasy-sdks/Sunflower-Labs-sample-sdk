# Auth
(*auth*)

## Overview

Authorization

### Available Operations

* [auth_token](#auth_token) - Request an authorization token

## auth_token

Request a token for use in API calls. The hive ID and the API key must be specified in the body.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI()

req = operations.AuthTokenRequest(
    request_body=operations.AuthTokenRequestBody(
        api_key='string',
        hive_id='string',
    ),
    valid_for_seconds=3600,
)

res = s.auth.auth_token(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.AuthTokenRequest](../../models/operations/authtokenrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.AuthTokenResponse](../../models/operations/authtokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
