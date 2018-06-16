### Link

https://blog.toast38coza.me/custom-ansible-module-hello-world/


### Run
```
docker@R90HE73F:/mnt/c/Users/irekromaniuk/Ansible$ ansible-playbook github_module/play_final.yml --extra-vars "github_token='xxxx...'"
 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] ****************************************************************************************************************************
TASK [Gathering Facts] **********************************************************************************************************************ok: [localhost]

TASK [Create a github Repo] *****************************************************************************************************************changed: [localhost]

TASK [Delete that repo] *********************************************************************************************************************ok: [localhost]

PLAY RECAP **********************************************************************************************************************************localhost                  : ok=3    changed=1    unreachable=0    failed=0
```