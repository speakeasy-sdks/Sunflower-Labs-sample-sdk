# WeatherAndFlightAdvisory
(*weather_and_flight_advisory*)

## Overview

Weather & Flight Advisory

### Available Operations

* [get_flight_advisory_status](#get_flight_advisory_status) - Flight Advisory
* [get_weather_status](#get_weather_status) - Weather Condition

## get_flight_advisory_status

Request the status of flight advisory

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.GetFlightAdvisoryStatusRequest(
    hive_id='HIVE12',
)

res = s.weather_and_flight_advisory.get_flight_advisory_status(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetFlightAdvisoryStatusRequest](../../models/operations/getflightadvisorystatusrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetFlightAdvisoryStatusResponse](../../models/operations/getflightadvisorystatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_weather_status

Request the status of weather

### Example Usage

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.GetWeatherStatusRequest(
    hive_id='HIVE12',
)

res = s.weather_and_flight_advisory.get_weather_status(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetWeatherStatusRequest](../../models/operations/getweatherstatusrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetWeatherStatusResponse](../../models/operations/getweatherstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
