ansible -i hosts all --list-hosts
ansible all --list-hosts
ansible -i hosts all -m ping -o
ansible all -m ping -o
ansible-playbook -i hosts shutunshut.yml -e ansible_user=irekromaniuk -e ansible_ssh_pass='password' --check
ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --check
ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --extra-vars "hosts=core-DC1"

ansible-playbook shutunshut.yml -e ansible_ssh_pass='Zakopane7&' --tags "test" --check

ansible-playbook shutunshut.yml -e ansible_ssh_pass='Zakopane7&' --tags "test" 

```
# sh int statu | i Ansible
Eth1/52       test core Ansible  xcvrAbsen routed    auto    auto    --
Eth2/52       test core Ansible  xcvrAbsen routed    auto    auto    --
```