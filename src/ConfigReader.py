import yaml

def configReader(self):
    stream = open('spudscale.config', 'r')
    return yaml.load_all(stream)
