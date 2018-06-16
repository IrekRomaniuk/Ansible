### Examples

ansible cli
```
docker@R90HE73F:/mnt/c/Users/irekromaniuk/Ansible$ ansible netlab,phantom,dc1,dc2 -i hosts -m command -a date
ansible netlab -i hosts -m command -a date
ansible all -i hosts -m command -a date
ansible cp -i hosts -m raw -a uptime
ansible all -i 'localhost,' -c local -m ping
```
ansible cli to run local command on remote targets
```
docker@R90HE73F:/mnt/c/Users/irekromaniuk/Ansible$ ansible all -i '10.34.1.100,10.41.1.100,' -m command -a 'which pingnet'
docker@R90HE73F:$ ansible all -i '10.41.1.100,' -m command -a pingnet
docker@R90HE73F:$ ansible all -i '10.34.1.100,' -m command -a pingnet
....
10.207.249.1
....
15.63s alive/total: 1174/4096 cur: 200
pingcount,site=DC,cur=200 total-up=1174
```
ansiblce cli with sshpass installed
```
ansible smb -i hosts -m raw -a uptime
```
ansbile playbook without roles
```
ansible-playbook --version
ansible-playbook -i hosts netlab.yml
```
ansible playbook without python and roles
```
ansible-playbook -i hosts cpraw.yml --extra-vars "cmd='uptime'"
```
ansible playbook with roles
```
ansible-playbook netlab-roles.yml -i hosts -l netlab --extra-vars "cmd='pip install awscli'" --user=docker --ask-pass
ansible-playbook netlab-roles.yml -i 10.254.243.100, --extra-vars "cmd='pip --version'" --user=docker
```
async action and polling
```
ansible-playbook -i hosts async_ping.yml
```
#### Verified commands:
```
aws --version
pip --version
```
#### make sure ssh without password is possible and user is in sudoers

ssh-copy-id -i ~/.ssh/id_rsa.pub docker@

/etc/sudoers:
docker ALL=(ALL:ALL) NOPASSWD:ALL

.ansible.cfg
export ANSIBLE_HOST_KEY_CHECKING=False

### Doc

apt:
ansible-doc apt

### State
```
- name: ensure sysstat is installed at version 10.2.0-1
  apt:
    name: sysstat=10.2.0-1
    state: installed
```

### Checkpoint related
##### works fine with admin user in ansible raw mode without Checkpoint expert (new_user with bash is not necessary)
#### smb (gaia embedded)
```
smb> add user new_user type admin password new_pass permission RW
[Expert@smb]# bashUser on
```
#### regular gaia
```
gaia:0> 
add user new_user uid 103 homedir /home/indeni
set user new_user newpass new_pass
add rba user new_user roles adminRole
set user indeni shell /bin/bash
save config
```
