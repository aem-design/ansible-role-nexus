# Ansible Role: Nexus

[![Build Status](https://travis-ci.org/aem-design/ansible-role-nexus.svg?branch=master)](https://travis-ci.org/aem-design/ansible-role-nexus)

Setup nexus in your environment.
> This role was developed as part of
> [AEM.Design](http://aem.design/)

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

| Name                        | Required | Default                                                                                                                                                                                                                                                                                  | Notes                                                                |
|-----------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| docker_image_user           | Yes      | aemdesign                                                                                                                                                                                                                                                                                | docker image user                                                    |
| docker_image_name           | Yes      | nexus                                                                                                                                                                                                                                                                                    | docker image name                                                    |
| docker_image                | No       | {{ docker_image_user }}/{{ docker_image_name }}                                                                                                                                                                                                                                          | docker image full name                                               |
| docker_image_tag            |          | latest                                                                                                                                                                                                                                                                                   | docker image tag                                                     |
| docker_container_name       |          | {{ docker_image_name }}                                                                                                                                                                                                                                                                  | docker container name                                                |
| docker_timezone             |          | Australia/Melbourne                                                                                                                                                                                                                                                                      | docker time zone                                                     |
| nexus_registry_port         |          | 5000                                                                                                                                                                                                                                                                                     | port for storing images                                              |
| nexus_registry_mirror_port  |          | 5001                                                                                                                                                                                                                                                                                     | port for to mirror pull requests                                     |
| nexus_registry_group_port   |          | 5002                                                                                                                                                                                                                                                                                     | port for combined port                                               |
| nexus_maven_repository_port |          | 8081                                                                                                                                                                                                                                                                                     | port for maven repository                                            |
| nexus_host                  |          | {{ service_nexus_host }}                                                                                                                                                                                                                                                                 | Nexus host                                                           |
| nexus_port                  |          | {{ service_nexus_port }}                                                                                                                                                                                                                                                                 | Nexus port                                                           |
| nexus_user                  |          | admin                                                                                                                                                                                                                                                                                    | Nexus admin username( default: admin)                                |
| nexus_password              |          | admin123                                                                                                                                                                                                                                                                                 | Nexus admin password( default: admin123)                             |
| nexus_url                   |          | http://{{ service_nexus_host }}:{{ service_nexus_port }}                                                                                                                                                                                                                                 | Nexus url                                                            |
| nexus_url_api_script        |          | {{ nexus_url }}/service/rest/v1/script                                                                                                                                                                                                                                                   | Nexus script API base url                                            |
| docker_published_ports      |          | - "0.0.0.0:{{ nexus_registry_port | default('5000') }}:5000/tcp" - "0.0.0.0:{{ nexus_registry_mirror_port | default('8081') }}:8080/tcp" - "0.0.0.0:{{ nexus_registry_group_port | default('5001') }}:5001/tcp" - "0.0.0.0:{{ nexus_maven_repository_port | default('5002') }}:5002/tcp" | docker published ports                                               |
| docker_volumes              |          | - "nexus-data:/nexus-data:z"                                                                                                                                                                                                                                                             | docker volumes                                                       |
| docker_host                 |          | "unix://var/run/docker.sock"                                                                                                                                                                                                                                                             | host where to run the docker container for executing pyaem2 commands |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: nexus    
```

## License

Apache 2.0

## Author Information

This role was created by [Max Barrass](https://aem.design/).