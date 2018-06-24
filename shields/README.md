### Fetch inventory
```
ansible-playbook shields-inventory.yml
docker@me:/mnt/c/Users/irekromaniuk/Ansible/shields$ fetched/
pingfull.yml
```
### Dyn inventory
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible/shields$ python fetched/pingfull.py --list --file fetched/pingfull.yml
```
### Run command
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible/shieldse$ ansible-playbook -i fetched/pingfull.py shields-random.yml -e "cmd=hostname" -e "ansible_user=ansible ansible_ssh_pass=password"
```

### Retry 
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible/shields$ ansible-playbook -i fetched/pingfull.py shields-subset.yml --limit @./shields-subset.retry -e "cmd=hostname" -e "ansible_user=ansible ansible_ssh_pass=password"
```