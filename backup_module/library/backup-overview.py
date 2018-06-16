#!/usr/bin/python
# -*- coding: utf-8 -*-

# [..] various imports

# this line must be written exactly that way,
# as Ansible will replace it with the "imported" code
from ansible.module_utils.basic import *


# [..] implementation code omitted

# simplified, flat version of the actual code
if __name__ == '__main__':
    global module
    module = AnsibleModule(
        argument_spec={
            'backup_dir': { 'required': True, 'type': 'str' },
            'path': { 'required': True, 'type': 'str' }
        },
        supports_check_mode=False
    )

    args = module.params
    # [..] check for early return reasons

    orig_file = _normalize_dirpath(args['path'])        
    backup_dir = _normalize_dirpath(args['backup_dir'])
    timestamp = create_timestamp()
    backup_file = create_backup_filename(backup_dir, orig_file, timestamp)

    result = do_the_magic(orig_file, backup_file)
    module.exit_json(**result)