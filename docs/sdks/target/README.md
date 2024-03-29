# Target
(*target*)

## Overview

Set a dynamic target.

### Available Operations

* [target_position](#target_position) - Set a dynamic target

## target_position

Set or update the position of a dynamic target. Please be aware of the default timeout 60s (if timeout is not specified). A target must be within the operational geofence. If the altitude is not specified, the target is assumed to be on top of the 3D mesh at the given latitude and longitude. A target will be ignored if the given time or position is invalid.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.TargetPositionRequest(
    hive_id='HIVE12',
)

res = s.target.target_position(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.TargetPositionRequest](../../models/operations/targetpositionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.TargetPositionResponse](../../models/operations/targetpositionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
