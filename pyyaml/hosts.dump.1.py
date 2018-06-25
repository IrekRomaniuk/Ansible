import yaml
#dc_dict={'pingfull':{'hosts':[]},'dc1notdc2':{'hosts':[]},'dc2notdc1':{'hosts':[]}}

dc_dict={
    'netlab':
        {'hosts':
            ['10.29.195.9','10.29.95.19','10.29.95.9','10.29.95.102']},
    'dc2':
        {'hosts':
            ['10.41.1.100','10.41.1.102']}
        }
with open('hosts.yml', 'w') as outfile:
    yaml.dump(dc_dict, outfile, default_flow_style=False)