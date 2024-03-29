"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from sunflower_labs_rest_api import utils
from sunflower_labs_rest_api._hooks import HookContext
from sunflower_labs_rest_api.models import errors, operations

class Auth:
    r"""Authorization"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def auth_token(self, request: operations.AuthTokenRequest) -> operations.AuthTokenResponse:
        r"""Request an authorization token
        Request a token for use in API calls. The hive ID and the API key must be specified in the body.
        """
        hook_ctx = HookContext(operation_id='authToken', oauth2_scopes=[], security_source=None)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/auth/token'
        
        headers = {}
        query_params = {}
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.AuthTokenRequest, "request_body", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = { **utils.get_query_params(operations.AuthTokenRequest, request), **query_params }
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['403','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.AuthTokenResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 403 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    