import logging

from ._version import __version__

__all__ = [
    "__version__",
]

logger = logging.getLogger(__name__)
logging.basicConfig()
