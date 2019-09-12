import logging
import logging.config
import yaml

import ooga.booga.wakka

logger = logging.getLogger(__name__)

def bar():
  logger.debug("foo")
  logger.info("bar")

if __name__ == "__main__":
  with open("resources/logging.yaml") as f:
    loggingConfig = yaml.safe_load(f)
  logging.config.dictConfig(loggingConfig)
  bar()
  ooga.booga.wakka.wakka()

