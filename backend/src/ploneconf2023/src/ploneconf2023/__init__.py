"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "ploneconf2023"

_ = MessageFactory("ploneconf2023")

logger = logging.getLogger("ploneconf2023")
