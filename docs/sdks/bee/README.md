# Bee
(*.bee*)

## Overview

Bee status, command and control.

### Available Operations

* [bee_follow](#bee_follow) - Deploy the Bee to follow a target
* [bee_inspect](#bee_inspect) - Deploy the Bee to inspect a specific observation zone (OZ)
* [bee_kill](#bee_kill) - Shut down power to motors (Emergency Procedure)
* [bee_land](#bee_land) - Bee returns to the Hive
* [bee_land_here](#bee_land_here) - Bee lands in place (Emergency Procedure)
* [bee_ptz](#bee_ptz) - Bee camera controls
* [bee_position](#bee_position) - Bee Position
* [bee_status](#bee_status) - Bee Status
* [bee_sweep](#bee_sweep) - Deploy the Bee to perform a sweep

## bee_follow

<p>Send the Bee to follow a target. A target needs to exist before this can be used.</p><p>Please send GET requests to retrieve flight advisory and weather condition before sending this command. If flight advisory is unknown or nogo, the flight_advisory_overridden has to be set in order to acknowledge that you want to proceed anyway. Otherwise, the command will be rejected. Similarly, if weather condition is unknown or nogo, the weather_overridden has to be set.</p>

### Example Usage

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

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.BeeFollowRequest](../../models/operations/beefollowrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.BeeFollowResponse](../../models/operations/beefollowresponse.md)**


## bee_inspect

<p>Send the Bee on an inspection of a predefined observation zone (OZ).</p><p>Please send GET requests to retrieve flight advisory and weather condition before sending this command. If flight advisory is unknown or nogo, the flight_advisory_overridden has to be set in order to acknowledge that you want to proceed anyway. Otherwise, the command will be rejected. Similarly, if weather condition is unknown or nogo, the weather_overridden has to be set.</p>

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeInspectRequest(
    request_body=operations.BeeInspectRequestBody(
        oz_id='string',
    ),
    hive_id='HIVE12',
)

res = s.bee.bee_inspect(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.BeeInspectRequest](../../models/operations/beeinspectrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.BeeInspectResponse](../../models/operations/beeinspectresponse.md)**


## bee_kill

Command the Bee to kill the power to the motors. It will fall out of the sky. This should only be used in an emergency.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeKillRequest(
    request_body=operations.BeeKillRequestBody(),
    hive_id='HIVE12',
)

res = s.bee.bee_kill(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.BeeKillRequest](../../models/operations/beekillrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.BeeKillResponse](../../models/operations/beekillresponse.md)**


## bee_land

Command the Bee to return to the Hive.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeLandRequest(
    request_body=operations.BeeLandRequestBody(),
    hive_id='HIVE12',
)

res = s.bee.bee_land(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.BeeLandRequest](../../models/operations/beelandrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.BeeLandResponse](../../models/operations/beelandresponse.md)**


## bee_land_here

Command the Bee to descend and land at the current location. This should only be used in an emergency.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeLandHereRequest(
    request_body=operations.BeeLandHereRequestBody(),
    hive_id='HIVE12',
)

res = s.bee.bee_land_here(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.BeeLandHereRequest](../../models/operations/beelandhererequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.BeeLandHereResponse](../../models/operations/beelandhereresponse.md)**


## bee_ptz

<p>Control the pan, position, or zoom of the camera.</p><p>Please send GET requests to retrieve flight advisory and weather condition before sending this command (except pan left/right). If flight advisory is unknown or nogo, the flight_advisory_overridden has to be set in order to acknowledge that you want to proceed anyway. Otherwise, the command will be rejected. Similarly, if weather condition is unknown or nogo, the weather_overridden has to be set.</p>

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeePTZRequest(
    request_body=operations.BeePTZRequestBody(
        action='string',
        direction='string',
    ),
    hive_id='HIVE12',
)

res = s.bee.bee_ptz(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.BeePTZRequest](../../models/operations/beeptzrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.BeePTZResponse](../../models/operations/beeptzresponse.md)**


## bee_position

Request the Bee position. lat and lon are the latitude and longitude of the position on WGS 84, alt is the height of the position on AMSL.

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeePositionRequest(
    hive_id='HIVE12',
)

res = s.bee.bee_position(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.BeePositionRequest](../../models/operations/beepositionrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.BeePositionResponse](../../models/operations/beepositionresponse.md)**


## bee_status

Request the Bee status. The status may be one of the following: landed_in_hive, landed_outside, take_off, on_inspection, on_sweep, paused, returning, returning_fallback, landing, landing_fallback, killed, calibrating, error, hopping, unknown

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeStatusRequest(
    hive_id='HIVE12',
)

res = s.bee.bee_status(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.BeeStatusRequest](../../models/operations/beestatusrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.BeeStatusResponse](../../models/operations/beestatusresponse.md)**


## bee_sweep

<p>Send the Bee on a predefined sequence of observations (aka sweep).</p><p>Please send GET requests to retrieve flight advisory and weather condition before sending this command. If flight advisory is unknown or nogo, the flight_advisory_overridden has to be set in order to acknowledge that you want to proceed anyway. Otherwise, the command will be rejected. Similarly, if weather condition is unknown or nogo, the weather_overridden has to be set.</p>

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="",
)

req = operations.BeeSweepRequest(
    request_body=operations.BeeSweepRequestBody(
        sweep_id='string',
    ),
    hive_id='HIVE12',
)

res = s.bee.bee_sweep(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.BeeSweepRequest](../../models/operations/beesweeprequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.BeeSweepResponse](../../models/operations/beesweepresponse.md)**

