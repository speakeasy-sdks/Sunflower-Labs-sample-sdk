# Sunflower-Labs-REST-API

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/Sunflower-Labs-sample-sdk.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/Sunflower-Labs-sample-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/Sunflower-Labs-sample-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [.bee](docs/sdks/bee/README.md)

* [bee_follow](docs/sdks/bee/README.md#bee_follow) - Deploy the Bee to follow a target
* [bee_inspect](docs/sdks/bee/README.md#bee_inspect) - Deploy the Bee to inspect a specific observation zone (OZ)
* [bee_kill](docs/sdks/bee/README.md#bee_kill) - Shut down power to motors (Emergency Procedure)
* [bee_land](docs/sdks/bee/README.md#bee_land) - Bee returns to the Hive
* [bee_land_here](docs/sdks/bee/README.md#bee_land_here) - Bee lands in place (Emergency Procedure)
* [bee_ptz](docs/sdks/bee/README.md#bee_ptz) - Bee camera controls
* [bee_position](docs/sdks/bee/README.md#bee_position) - Bee Position
* [bee_status](docs/sdks/bee/README.md#bee_status) - Bee Status
* [bee_sweep](docs/sdks/bee/README.md#bee_sweep) - Deploy the Bee to perform a sweep

### [.map](docs/sdks/map/README.md)

* [get_o_zs](docs/sdks/map/README.md#get_o_zs) - Observation Zones
* [get_sweeps](docs/sdks/map/README.md#get_sweeps) - Sweeps

### [.weather_and_flight_advisory](docs/sdks/weatherandflightadvisory/README.md)

* [get_flight_advisory_status](docs/sdks/weatherandflightadvisory/README.md#get_flight_advisory_status) - Flight Advisory
* [get_weather_status](docs/sdks/weatherandflightadvisory/README.md#get_weather_status) - Weather Condition

### [.hive](docs/sdks/hive/README.md)

* [hive_roof_control](docs/sdks/hive/README.md#hive_roof_control) - Manual control for the Hive roof
* [hive_roof_status](docs/sdks/hive/README.md#hive_roof_status) - Get status of the Hive roof

### [.target](docs/sdks/target/README.md)

* [target_position](docs/sdks/target/README.md#target_position) - Set a dynamic target

### [.auth](docs/sdks/auth/README.md)

* [auth_token](docs/sdks/auth/README.md#auth_token) - Request an authorization token
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.sunflower-labs.com` | None |
| 1 | `https://api.dev.sunflower-labs.com` | None |

For example:

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    server_idx=1,
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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import sunflower_labs_rest_api
from sunflower_labs_rest_api.models import operations

s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(
    server_url="https://api.sunflower-labs.com",
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
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import sunflower_labs_rest_api
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sunflower_labs_rest_api.SunflowerLabsRESTAPI(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->

# Authentication

## Per-Client Security Schemes

Your SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:

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
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
