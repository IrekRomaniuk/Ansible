### Links 
https://github.com/ndemengel/ansible-backup-module
http://ndemengel.github.io/2015/01/20/ansible-modules-and-action-plugins/

### Run
```
docker@R90HE73F:/mnt/c/Users/irekromaniuk/Ansible$ sudo ansible-playbook backup_module/backup.yml
 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] ****************************************************************************************************************************
TASK [Gathering Facts] **********************************************************************************************************************ok: [localhost]

TASK [backup /etc/default] ******************************************************************************************************************changed: [localhost]

PLAY RECAP **********************************************************************************************************************************localhost                  : ok=2    changed=1    unreachable=0    failed=0

```
### Result
```
docker@R90HE73F:/mnt/c/Users/irekromaniuk/Ansible$ ls -l /var/backups/etc/
total 12
-rw-r--r-- 1 root root 9407 Jun 16 11:38 default.ansible.bckp.20180616.tar.gz
```