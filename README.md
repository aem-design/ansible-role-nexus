# Ansible Role: Nexus

[![Build Status](https://travis-ci.org/aem-design/ansible-role-nexus.svg?branch=master)](https://travis-ci.org/aem-design/ansible-role-nexus)

Setup nexus in your environment.
> This role was developed as part of
> [AEM.Design](http://aem.design/)

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

| Name                          	| Required 	| Default                                                                    	| Notes                            	|
|-------------------------------	|----------	|----------------------------------------------------------------------------	|----------------------------------	|
| docker_image_user             	|          	| aemdesign                                                                  	|                                  	|
| docker_image_name             	|          	| nexus                                                                      	|                                  	|
| docker_image                  	|          	| {{ docker_image_user }}/{{ docker_image_name }}                            	|                                  	|
| docker_image_tag              	|          	| latest                                                                     	|                                  	|
| docker_container_name         	|          	| {{ docker_image_name }}                                                    	|                                  	|
| docker_registry_port          	|          	| 5000                                                                       	| port for storing images          	|
| docker_registry_mirror_port   	|          	| 5001                                                                       	| port for to mirror pull requests 	|
| docker_registry_group_port    	|          	| 5002                                                                       	| port for combined port           	|
| service_maven_repository_port 	|          	| 8081                                                                       	| port for maven repository        	|
| service_nexus_address         	|          	| localhost                                                                  	|                                  	|
| service_nexus_port            	|          	| 8081                                                                       	|                                  	|
|                               	|          	|                                                                            	|                                  	|
| docker_published_ports        	|          	|                                                                            	|                                  	|
|                               	|          	| - "0.0.0.0:{{ docker_registry_port | default('5000') }}:5000/tcp"          	|                                  	|
|                               	|          	| - "0.0.0.0:{{ docker_registry_mirror_port | default('5001') }}:5001/tcp"   	|                                  	|
|                               	|          	| - "0.0.0.0:{{ docker_registry_group_port | default('5002') }}:5002/tcp"    	|                                  	|
|                               	|          	| - "0.0.0.0:{{ service_maven_repository_port | default('8081') }}:8080/tcp" 	|                                  	|
|                               	|          	|                                                                            	|                                  	|
| docker_volumes                	|          	|                                                                            	|                                  	|
|                               	|          	| - "nexus-data:/nexus-data:z"                                               	|                                  	|
|                               	|          	|                                                                            	|                                  	|
| docker_container_user         	|          	| {{ docker_container_name }}                                                	|                                  	|
| docker_container_userid       	|          	| 10002                                                                      	|                                  	|
| docker_container_group        	|          	| {{ docker_container_name }}                                                	|                                  	|
| docker_container_groupid      	|          	| 10002                                                                      	|                                  	|
|                               	|          	|                                                                            	|                                  	|
| iptable_rules                 	|          	|                                                                            	|                                  	|
|                               	|          	| - port: "{{ docker_registry_port | default('5000') }}"                     	|                                  	|
|                               	|          	| comment: "docker_registry_port"                                            	|                                  	|
|                               	|          	| - port: "{{ service_maven_repository_port | default('8081') }}"            	|                                  	|
|                               	|          	| comment: "service_maven_repository_port"                                   	|                                  	|
|                               	|          	| - port: "{{ docker_registry_mirror_port | default('5001') }}"              	|                                  	|
|                               	|          	| comment: "docker_registry_mirror_port"                                     	|                                  	|
|                               	|          	| - port: "{{ docker_registry_group_port | default('5002') }}"               	|                                  	|
|                               	|          	| comment: "docker_registry_group_port"                                      	|                                  	|
|                               	|          	|                                                                            	|                                  	|
| nexus_host                    	|          	| {{ service_nexus_address | default('localhost') }}                          	|                                  	|
| nexus_port                    	|          	| {{ service_nexus_port | default('8081') }}                                 	|                                  	|


## Dependencies

This role depends on roles:
 
- `aem_design.docker_container`
- `aem_design.config_iptables`

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