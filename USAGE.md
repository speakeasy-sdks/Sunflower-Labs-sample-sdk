<!-- Start SDK Example Usage -->


```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeFollowRequest(
    request_body=operations.BeeFollowRequestBody(
        target_id='string',
    ),
    hive_id='HIVE12',
)

res = s.bee.bee_follow(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->