<!-- Start SDK Example Usage [usage] -->
```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.BeeFollowRequest(
    hive_id='HIVE12',
    request_body=operations.BeeFollowRequestBody(
        target_id='string',
    ),
)

res = s.bee.bee_follow(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->