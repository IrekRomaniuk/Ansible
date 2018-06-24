import yaml

dc_dict={
 'netlab':
        {'hosts':
            ['1.1.1.1','2.2.2.2']},
 'dc2':
        {'hosts':
            ['3.3.3.3','4.4.4.4']}
        }
with open('hosts.yml', 'w') as outfile:
    yaml.dump(dc_dict, outfile, default_flow_style=True)