ansible -i hosts all --list-hosts
ansible all --list-hosts
ansible -i hosts all -m ping -o
ansible all -m ping -o
ansible-playbook -i hosts shutunshut.yml -e ansible_user=irekromaniuk -e ansible_ssh_pass='password' --check
ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --check
ansible-playbook shutunshut.yml -e ansible_ssh_pass='password' --extra-vars "hosts=core-DC1"