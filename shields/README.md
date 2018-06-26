### Fetch inventory
```
ansible-playbook -i hosts shields-inventory.yml
docker@me:/mnt/c/Users/irekromaniuk/Ansible/shields$ fetched/
pingfull.yml
```
### Dyn inventory
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible/shields$ python fetched/pingfull.py --list --file fetched/pingfull.yml
```
### Run command
#### Remember to keep ansible_ssh_pass as seperate external arguments because of special characters, see also example of command with spaces

```
docker@me:...shields$ ansible-playbook -i fetched/pingfull.py shields-subset.yml -e cmd=uptime -e ansible_user=admin -e ansible_ssh_pass='password'
docker@me:...shields$ ansible-playbook  shields-subset.yml -e 'cmd="show interface Internet1"' -e ansible_user=admin -e ansible_ssh_pass='password'
```
also: ver, 'show interface Internet1','show admin-access-ipv4-addresses'

### Retry 
```
docker@me:....shields$ ansible-playbook -i fetched/pingfull.py shields-subset.yml --limit @./shields-subset.retry -e cmd=uptime -e ansible_user=admin -e ansible_ssh_pass='password'
```