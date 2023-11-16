"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class BeeKillRequestBody:
    pass


@dataclasses.dataclass
class BeeKillRequest:
    hive_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'hiveId', 'style': 'simple', 'explode': False }})
    r"""The UUID of the Hive"""
    request_body: Optional[BeeKillRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class BeeKillResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    

