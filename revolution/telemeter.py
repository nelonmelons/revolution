from dataclasses import dataclass
from logging import getLogger
from typing import ClassVar

from revolution.application import Application
from revolution.environment import Endpoint

_logger = getLogger(__name__)


@dataclass
class Telemeter(Application):
    endpoint: ClassVar[Endpoint] = Endpoint.TELEMETER
