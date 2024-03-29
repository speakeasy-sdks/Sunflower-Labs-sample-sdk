"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sunflower_labs_rest_api import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeeFollowRequestBody:
    target_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_id') }})
    flight_advisory_overridden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flight_advisory_overridden'), 'exclude': lambda f: f is None }})
    weather_overridden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weather_overridden'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class BeeFollowRequest:
    hive_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'hiveId', 'style': 'simple', 'explode': False }})
    r"""The UUID of the Hive"""
    request_body: Optional[BeeFollowRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class BeeFollowResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

