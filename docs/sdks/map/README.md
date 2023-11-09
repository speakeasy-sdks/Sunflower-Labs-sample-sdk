# Map
(*map*)

## Overview

Map definition, command and control.

### Available Operations

* [get_o_zs](#get_o_zs) - Observation Zones
* [get_sweeps](#get_sweeps) - Sweeps

## get_o_zs

Request a list of available observation zones

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.GetOZsRequest(
    hive_id='HIVE12',
)

res = s.map.get_o_zs(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetOZsRequest](../../models/operations/getozsrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.GetOZsResponse](../../models/operations/getozsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_sweeps

Request a list of available sweeps

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.GetSweepsRequest(
    hive_id='HIVE12',
)

res = s.map.get_sweeps(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSweepsRequest](../../models/operations/getsweepsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSweepsResponse](../../models/operations/getsweepsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
