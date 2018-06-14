### Examples
```
ansible-playbook --version
ansible-playbook netlab.yml -i hosts -l netlab --extra-vars "cmd='pip install awscli'" --user=docker --ask-pass
```
##### Verified commands:
```
aws --version
pip --version

export ANSIBLE_HOST_KEY_CHECKING=False
```
### make sure ssh without password is possible and user is in sudoers

ssh-copy-id -i ~/.ssh/id_rsa.pub docker@

/etc/sudoers:
docker ALL=(ALL:ALL) NOPASSWD:ALL



