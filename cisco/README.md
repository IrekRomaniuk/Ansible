ansible -i hosts all --list-hosts
ansible all --list-hosts
ansible -i hosts all -m ping -o
ansible all -m ping -o
ansible-playbook -i hosts shutunshut.yml -e ansible_user=irekromaniuk -e ansible_ssh_pass='password' --check
ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --check
ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --extra-vars "hosts=core-DC1"

ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --tags "test" --check

ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --tags "test" 

ansible-playbook showint.yml -e ansible_ssh_pass='password'

ansible-playbook shutnew.yml -e ansible_ssh_pass='password' --tags "core"

```
# sh int statu | i Ansible
Eth1/52       test core Ansible  xcvrAbsen routed    auto    auto    --
Eth2/52       test core Ansible  xcvrAbsen routed    auto    auto    --
```

ansible-playbook infobloxold2new.yml -e pass='password'