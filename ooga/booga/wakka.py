import logging
import logging.config
import yaml

import foo
import flim.flam

logger = logging.getLogger(__name__)

def wakka():
  logger.debug("oogabooga")
  logger.info("wakkawakka")

if __name__ == "__main__":
  with open("resources/logging.yaml") as f:
    loggingConfig = yaml.safe_load(f)
  logging.config.dictConfig(loggingConfig)
  wakka()
  foo.bar()
  flim.flam.flimflam()

