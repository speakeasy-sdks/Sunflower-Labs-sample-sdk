"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .auth import Auth
from .bee import Bee
from .hive import Hive
from .map import Map
from .sdkconfiguration import SDKConfiguration
from .target import Target
from .weather_and_flight_advisory import WeatherAndFlightAdvisory
from sunflower_labs_rest_api import utils
from sunflower_labs_rest_api._hooks import SDKHooks
from sunflower_labs_rest_api.models import shared
from typing import Callable, Dict, Union

class SunflowerLabsRESTAPI:
    r"""Sunflower Labs REST API: REST Bridge provides a REST API to the Sunflower Labs Home Awareness system."""
    bee: Bee
    r"""Bee status, command and control."""
    map: Map
    r"""Map definition, command and control."""
    weather_and_flight_advisory: WeatherAndFlightAdvisory
    r"""Weather & Flight Advisory"""
    hive: Hive
    r"""Hive status, command and control."""
    target: Target
    r"""Set a dynamic target."""
    auth: Auth
    r"""Authorization"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 bearer_auth: Union[str, Callable[[], str]],
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param bearer_auth: The bearer_auth required for authentication
        :type bearer_auth: Union[str, Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if callable(bearer_auth):
            def security():
                return shared.Security(bearer_auth = bearer_auth())
        else:
            security = shared.Security(bearer_auth = bearer_auth)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks=hooks
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.bee = Bee(self.sdk_configuration)
        self.map = Map(self.sdk_configuration)
        self.weather_and_flight_advisory = WeatherAndFlightAdvisory(self.sdk_configuration)
        self.hive = Hive(self.sdk_configuration)
        self.target = Target(self.sdk_configuration)
        self.auth = Auth(self.sdk_configuration)
    