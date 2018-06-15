### Examples
```

ansible netlab -i hosts -m command -a date
ansible all -i hosts -m command -a date
ansible all -i 'localhost,' -c local -m ping
ansible-playbook --version
ansible-playbook -i hosts netlab.yml
ansible-playbook netlab-roles.yml -i hosts -l netlab --extra-vars "cmd='pip install awscli'" --user=docker --ask-pass
ansible-playbook netlab-roles.yml -i 10.254.243.100, --extra-vars "cmd='pip --version'" --user=docker
```
##### Verified commands:
```
aws --version
pip --version
```
### make sure ssh without password is possible and user is in sudoers

ssh-copy-id -i ~/.ssh/id_rsa.pub docker@

/etc/sudoers:
docker ALL=(ALL:ALL) NOPASSWD:ALL

.ansible.cfg
export ANSIBLE_HOST_KEY_CHECKING=False

### Doc

apt:
ansible-doc apt

### State

- name: ensure sysstat is installed at version 10.2.0-1
  apt:
    name: sysstat=10.2.0-1
    state: installed

