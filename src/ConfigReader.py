import yaml

def configReader():
    stream = open('spudscale.config', 'r')
    config = {}
    for data in yaml.load_all(stream):
        config = data
    return config

if __name__ == '__main__':
    configReader()
