import yaml

def configReader():
    stream = open('spudscale.config', 'r')
    return yaml.load_all(stream)
