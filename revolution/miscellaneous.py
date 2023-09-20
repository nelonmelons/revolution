from dataclasses import dataclass
from logging import getLogger
from typing import ClassVar

from revolution.application import Application
from revolution.utilities import Endpoint

_logger = getLogger(__name__)


@dataclass
class Miscellaneous(Application):
    endpoint: ClassVar[Endpoint] = Endpoint.MISCELLANEOUS
