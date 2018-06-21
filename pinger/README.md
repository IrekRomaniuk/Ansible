### pinger
#### based on the fork from [sourceperl/th_pinger.py](https://gist.github.com/irom77/794c18ba392e42e944b09c42493b1786)

```
ansible-playbook -i hosts pinger/copy.yml

ansible-playbook -i hosts pinger/ping.yml > output/pingcount.theping

ansible-playbook -i hosts pinger/copy_and_ping.yml > output/pingcount.theping
```