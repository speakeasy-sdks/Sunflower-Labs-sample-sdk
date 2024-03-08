# Hive
(*hive*)

## Overview

Hive status, command and control.

### Available Operations

* [hive_roof_control](#hive_roof_control) - Manual control for the Hive roof
* [hive_roof_status](#hive_roof_status) - Get status of the Hive roof

## hive_roof_control

Manually open/close/stop the Hive roof. Not required for normal operations.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.HiveRoofControlRequest(
    hive_id='HIVE12',
)

res = s.hive.hive_roof_control(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.HiveRoofControlRequest](../../models/operations/hiveroofcontrolrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.HiveRoofControlResponse](../../models/operations/hiveroofcontrolresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## hive_roof_status

Request the Hive roof status. The status may be one of the following: stopped, open, closed, error, opening, closing, unknown

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.HiveRoofStatusRequest(
    hive_id='HIVE12',
)

res = s.hive.hive_roof_status(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.HiveRoofStatusRequest](../../models/operations/hiveroofstatusrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.HiveRoofStatusResponse](../../models/operations/hiveroofstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
