### pinger
#### based on the fork from [sourceperl/th_pinger.py](https://gist.github.com/irom77/794c18ba392e42e944b09c42493b1786)

- Copy list of targets in file 'pinglist.txt' or 'pinglist-all.txt' to both hosts and run 'theping.py' 
- Fetch results (files with 'ping-result' prefix) to the local 'fetched' dir and run 'thediff.py' to find diff and unique targets
- Copy back inventory 'pingfull.yml' with unique targets to both hosts 

#### Todo:
- add sections 'dc1notdc2' and 'dc2notdc1' in the 'pingfull.yml' inventory
- pick random targets and ssh to run command

#### Usefull commands
```
ansible-playbook pinger.yml --tags local
docker@me:/mnt/c/Users/irekromaniuk/Ansible/pinger$ ansible pingnet -a 'ls -l pinglist.txt' -o
10.10.1.100 | CHANGED | rc=0 | (stdout) -rw-rw-r--. 1 docker docker 14444 Jul 14  2017 pinglist.txt
10.20.1.100 | CHANGED | rc=0 | (stdout) -rw-rw-r--. 1 docker docker 14444 Jun 21 13:19 pinglist.txt
docker@me:/mnt/c/Users/irekromaniuk/Ansible/pinger$ ansible pingnet -a 'ls -l pinglist-all.txt' -o
10.10.1.100 | CHANGED | rc=0 | (stdout) -rw-rw-r--. 1 docker docker 27696 Aug 11  2016 pinglist-all.txt
10.20.1.100 | CHANGED | rc=0 | (stdout) -rw-rw-r--. 1 docker docker 27696 Jun 21 12:10 pinglist-all.txt
docker@me:/mnt/c/Users/irekromaniuk/Ansible/pinger$ ansible pingnet -a 'ls -l pingfull.yml' -o
10.10.1.100 | CHANGED | rc=0 | (stdout) -rw-rw-r--. 1 docker docker 15593 Jun 21 15:54 pingfull.yml
10.20.1.100 | CHANGED | rc=0 | (stdout) -rw-rw-r--. 1 docker docker 15593 Jun 21 15:54 pingfull.yml
```
### Dynamic inventory
```
docker@R90HE73F:/mnt/c/Users/irekromaniuk/Ansible/pinger$ python pingfull.py -h
usage: pingfull.py [-h] [--list] [--host HOST] --file FILE

optional arguments:
  -h, --help   show this help message and exit
  --list       list inventory
  --host HOST  show HOST variables
  --file FILE  YAML file to read inventory from
docker@me:/mnt/c/Users/irekromaniuk/Ansible/pinger$ python /pingfull.py --list --file pingfull.1.yml
{
    "dc1notdc2": {
        "hosts": []
    },
    "dc2notdc1": {
        "hosts": []
    },
    "pingfull": {
        "hosts": [
            "10.197.143.1",
            "10.197.71.1",
            "10.195.89.1"
        ]
    }
}
```
#### Playbook
```
docker@me:/mnt/c/Users/irekromaniuk/Ansible/pinger$ ansible-playbook pinger.yml

PLAY [pingnet] *****************************************************************************************************************************************************************************************************************
TASK [Gathering Facts] *********************************************************************************************************************************************************************************************************ok: [10.10.1.100]
ok: [10.20.1.100]

TASK [Copying files to DC1 and DC2] ***************************************************************************************************************************************************************************************ok: [10.10.1.100] => (item=theping.py)
ok: [10.10.1.100] => (item=pinglist-all.txt)
ok: [10.20.1.100] => (item=theping.py)
ok: [10.10.1.100] => (item=pinglist.txt)
ok: [10.20.1.100] => (item=pinglist-all.txt)
ok: [10.20.1.100] => (item=pinglist.txt)

TASK [Ping from DC1] ***********************************************************************************************************************************************************************************************************skipping: [10.20.1.100]
changed: [10.10.1.100]

TASK [Ping from DC2] ***********************************************************************************************************************************************************************************************************skipping: [10.10.1.100]
changed: [10.20.1.100]

TASK [Capture Job IDs] *********************************************************************************************************************************************************************************************************ok: [10.10.1.100] => (item={u'ansible_job_id': u'38602379960.31049', u'started': 1, 'changed': True, 'failed': False, u'finished': 0, u'results_file': u'/home/docker/.ansible_async/38602379960.31049'})
ok: [10.10.1.100] => (item={'skipped': True, 'changed': False, 'skip_reason': u'Conditional result was False'})
ok: [10.20.1.100] => (item={'skipped': True, 'changed': False, 'skip_reason': u'Conditional result was False'})
ok: [10.20.1.100] => (item={u'ansible_job_id': u'436746783415.23460', u'started': 1, 'changed': True, 'failed': False, u'finished': 0, u'results_file': u'/home/docker/.ansible_async/436746783415.23460'})

TASK [Wait for Job IDs] ********************************************************************************************************************************************************************************************************changed: [10.10.1.100] => (item=38602379960.31049)
changed: [10.20.1.100] => (item=436746783415.23460)

TASK [debug] *******************************************************************************************************************************************************************************************************************ok: [10.10.1.100] => {
    "msg": "1061/1149"
}
ok: [10.20.1.100] => {
    "msg": "1066/1149"
}

TASK [Fetching results from DC1 and DC2] ***************************************************************************************************************************************************************************************changed: [10.10.1.100]
changed: [10.20.1.100]

TASK [Find diff] ***************************************************************************************************************************************************************************************************************changed: [10.10.1.100 -> localhost]
changed: [10.20.1.100 -> localhost]

TASK [Copying pingfull.yml back  to DC1 and DC2] *******************************************************************************************************************************************************************************changed: [10.10.1.100]
changed: [10.20.1.100]

PLAY RECAP *********************************************************************************************************************************************************************************************************************10.10.1.100                : ok=9    changed=5    unreachable=0    failed=0
10.20.1.100                : ok=9    changed=5    unreachable=0    failed=0
```