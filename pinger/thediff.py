import yaml

from argparse import ArgumentParser

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

parser = ArgumentParser(description="Find missing targets")

parser.add_argument("-dc1", "--dc1", dest="dc1", default="pinger/fetched/ping-result-dc01ap-p001mon.yml",
                    help="dc1", metavar="DC1")
parser.add_argument("-dc2", "--dc2", dest="dc2", default="pinger/fetched/ping-result-dc02ap-p001mon.yml",
                    help="dc2", metavar="DC2")   
parser.add_argument("-f", "--full", dest="full", default="pinger/pingfull.yml",
                    help="Unique addresses", metavar="FULL")                                     


args = parser.parse_args()
dc_dict={'pingfull':{'hosts':[]},'dc1notdc2':{'hosts':[]},'dc2notdc1':{'hosts':[]}}
dc1_dict = yaml.load(open(args.dc1))
dc2_dict = yaml.load(open(args.dc2))

# print('{} {}'.format(len(dc1_dict['msg']),len(dc2_dict['msg'])))

dc1_list=[item.split(':')[0] for item in dc1_dict['msg']]
dc2_list=[item.split(':')[0] for item in dc2_dict['msg']]

# print('{} {}'.format(len(dc1_list),len(dc2_list)))

dc_dict['pingfull']['hosts'] = list(set(dc1_list + dc2_list))
dc_dict['dc1notdc2']['hosts'] = diff(dc1_list, dc2_list)
dc_dict['dc2notdc1']['hosts'] = diff(dc2_list, dc1_list)

print('Number of unique address: {}'.format(len(dc_dict['pingfull'])))
print('Address in DC1 but not in DC2: {}'.format(diff(dc1_list, dc2_list)))
print('Address in DC2 but not in DC1: {}'.format(diff(dc2_list, dc1_list)))

with open(args.full, 'w') as outfile:
    yaml.dump(dc_dict, outfile, default_flow_style=True)
