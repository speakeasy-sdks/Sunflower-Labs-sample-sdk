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
# SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/Sunflower-Labs-sample-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
# Available Resources and Operations


## [auth](docs/sdks/auth/README.md)

* [auth_token](docs/sdks/auth/README.md#auth_token) - Request an authorization token

## [bee](docs/sdks/bee/README.md)

* [bee_follow](docs/sdks/bee/README.md#bee_follow) - Deploy the Bee to follow a target
* [bee_inspect](docs/sdks/bee/README.md#bee_inspect) - Deploy the Bee to inspect a specific observation zone (OZ)
* [bee_kill](docs/sdks/bee/README.md#bee_kill) - Shut down power to motors (Emergency Procedure)
* [bee_land](docs/sdks/bee/README.md#bee_land) - Bee returns to the Hive
* [bee_land_here](docs/sdks/bee/README.md#bee_land_here) - Bee lands in place (Emergency Procedure)
* [bee_ptz](docs/sdks/bee/README.md#bee_ptz) - Bee camera controls
* [bee_position](docs/sdks/bee/README.md#bee_position) - Bee Position
* [bee_status](docs/sdks/bee/README.md#bee_status) - Bee Status
* [bee_sweep](docs/sdks/bee/README.md#bee_sweep) - Deploy the Bee to perform a sweep

## [hive](docs/sdks/hive/README.md)

* [hive_roof_control](docs/sdks/hive/README.md#hive_roof_control) - Manual control for the Hive roof
* [hive_roof_status](docs/sdks/hive/README.md#hive_roof_status) - Get status of the Hive roof

## [map](docs/sdks/map/README.md)

* [get_o_zs](docs/sdks/map/README.md#get_o_zs) - Observation Zones
* [get_sweeps](docs/sdks/map/README.md#get_sweeps) - Sweeps

## [target](docs/sdks/target/README.md)

* [target_position](docs/sdks/target/README.md#target_position) - Set a dynamic target

## [weather_and_flight_advisory](docs/sdks/weatherandflightadvisory/README.md)

* [get_flight_advisory_status](docs/sdks/weatherandflightadvisory/README.md#get_flight_advisory_status) - Flight Advisory
* [get_weather_status](docs/sdks/weatherandflightadvisory/README.md#get_weather_status) - Weather Condition
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->



<!-- End Dev Containers -->

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
