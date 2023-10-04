import requests
import logging
import ratelimit
from backoff import on_exception, expo
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class LeagueOfLegendsAPI(ABC):
    def __init__(self, queue: str) -> None:
        self.queue = queue
        self.base_endpoint = "https://br1.api.riotgames.com/lol/league-exp/v4"

    @abstractmethod
    def _get_endpoint(self, **kwargs) -> str:
        pass

    @on_exception(expo, ratelimit.exception.RateLimitException, max_tries=10)
    @ratelimit.limits(calls=29, period=30)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def get_data(self, **kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f"Gettting data from endpoint: {endpoint}")
        response = requests.get(endpoint, headers={'X-Riot-Token': ''})
        response.raise_for_status()
        return response.json()

class LeagueQueuesApi(LeagueOfLegendsAPI):
    type = "entries"

    def _get_endpoint(self, tier: str, division: str, page: int) -> str:
        return f"{self.base_endpoint}/{self.type}/{self.queue}/{tier}/{division}?page={page}"