<!-- Start SDK Example Usage -->


```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations, shared

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

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
<!-- End SDK Example Usage -->