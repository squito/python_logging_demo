import logging
import logging.config
import yaml


logger = logging.getLogger(__name__)

def bar():
  logger.debug("foo")
  logger.info("bar")

