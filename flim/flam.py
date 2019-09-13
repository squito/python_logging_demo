import logging
import logging.config
import yaml

import ooga.booga.wakka

logger = logging.getLogger(__name__)
logger.propagate = True

def flimflam():
  logger.debug("flim")
  logger.info("flam")
