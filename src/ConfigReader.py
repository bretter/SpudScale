import yaml


def configReader():
    stream = open('spudscale.config', 'r')
    config = {}
    for data in yaml.load_all(stream):
        config = data
    config['scales'] = scaleIndexToAddress(config['scales'])
    return config


def scaleIndexToAddress(scaleIndexedNames):
    scaleAddressNames = {}
    for index, name in scaleIndexedNames.items():
        scaleAddressNames[chr(ord('A') + (index - 1))] = name
    return scaleAddressNames
