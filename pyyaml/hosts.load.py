import yaml

data_loaded={}

with open("hosts.4.yml", 'r') as stream:
    data_loaded = yaml.load(stream)            

print data_loaded            