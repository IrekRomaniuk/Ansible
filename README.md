### Examples
```
ansible-playbook --version
ansible-playbook netlab.yml -i hosts -l netlab --extra-vars "cmd='pip install awscli'" --user=docker --ask-pass
ansible-playbook netlab.yml -i 10.254.243.100, --extra-vars "cmd='pip --version'" --user=docker
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

