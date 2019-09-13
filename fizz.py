import logging
import logging.config
import yaml

if __name__ == "__main__":
  with open("resources/logging.yaml") as f:
    loggingconfig = yaml.safe_load(f)
  logging.config.dictConfig(loggingconfig)

  # its important these get imported *after* loading the logging configuration
  import foo
  import flim.flam
  import ooga.booga.wakka
  foo.bar()
  flim.flam.flimflam()
  ooga.booga.wakka.wakka()
else:
  raise Exception("this should only be used as '__main__' entrypoint")
