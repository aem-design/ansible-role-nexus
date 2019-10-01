#!/usr/bin/python

import docker
import json

from ansible.module_utils.basic import *

def main():
    fields = {
        "docker_container": {"required": True, "type": "str"},
        "docker_exec_command": {"required": True, "type": "str"},
        "docker_host": {"required": False, "type": "str", "default": "unix://var/run/docker.sock"}
    }

    module = AnsibleModule(argument_spec=fields)

    # stick everything into a dictionary for easy reuse
    params = dict(
        docker_container=module.params['docker_container'],
        docker_exec_command=module.params['docker_exec_command'],
        docker_host=module.params['docker_host']
    )

    client = docker.APIClient(base_url=params["docker_host"])

    if params['docker_container']:
        if params['docker_exec_command']:
            execinstance = client.exec_create(
                container=params['docker_container'],
                cmd=params['docker_exec_command']
            )

            output=client.exec_start(
                exec_id=execinstance["Id"]
            )

            module.exit_json(
                failed=False,
                msg=output
            )
            return True
        else:
            module.fail_json(
                failed=True,
                msg={
                    'msg': 'Docker exec command not specified',
                    'params': params
                }
            )
        return False
    else:
        module.fail_json(
            failed=True,
            msg={
                'msg': 'Docker container name not specified',
                'params': params
            }
        )
        return False

if __name__ == '__main__':
    main()
