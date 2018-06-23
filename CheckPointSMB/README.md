### Dyn inventory
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible$ python pinger/pinginv.py --list --file pinger/pingfull.yml
```
### Run command
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible$ ansible-playbook -i pinger/pinginv.py CheckPointSMB/shields-random.yml -e "cmd=hostname" -e "ansible_user=ansible ansible_ssh_pass=password"
```