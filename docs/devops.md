Welcome to the Capstone wiki!  

# Table of Content  

- [Project Requirement](#Project-Requirement)
- [Pre-requisite](#Pre-requisite)
- [Configuring Environment](#Configuring-Environment)
- [Executing Devops Project](#Executing-Devops-Project)
  * [Test case output](#Test-case-output)
  * [Deployed output in production server](#Deployed-output-in-production-server)

## Project Requirement:  

You have been Hired Sr. Devops Engineer in Abode Softwares.  
They want to implement Devops Lifecycle in their company.  
You have been asked to implement this lifecycle as fast as possible.  

Abode Softwares is a product based company, their product is available on this github link.

<Git-Hub>

Following are the specifications of the lifecycle:

1. Git Workflow has to be implemented
2. Code Build should automatically be triggered once commit is made to master branch or develop branch.

If commit is made to master branch, test and push to prod
If commit is made to develop branch, just test the product, do not push to prod


3. The Code should be containerized with the help of a Dockerfile.  The Dockerfile should be built everytime there is a push to Git-Hub. Use the following pre-built container for your application:
hshar/webapp

The code should reside in '/var/www/html'

4. Once the website is built, you have to design a test-case, which will basically check if the website can be opened or not. If yes, the test should pass. This test has to run in headless mode, on the test server.

5. Since you are setting up the server for the first time, ensure the following file exists on both Test and Prod server in /home/ubuntu/config-management/status.txt. This file will be used by a third party tool.

The content of this file, should be based on whether git is installed or not.

If git is installed => "Git is Installed on this System"
If git is not installed => "Git is not installed on this System"

For improving code readability, ensure you create modules on Puppet-Master, to accomplish this task.


__Architectural Advice:__  

Create 3 servers on AWS __"t2.micro"__  
Server 1 - should have Jenkins Master and Puppet Master Installed  
Server 2 - Testing Server, Jenkins Slave  
Server 3 - Prod Server, Jenkins Slave  

## Pre-requisite

- [x] Github Account
- [x] Travis CI account
- [x] AWS Account
- [x] AWS access_key and secret_key

## Configuring Environment  

1. To configure the environment as per architecture advice, i have created a ansible-role-intellipaat project using ansible.  

__Environment Project:__ https://github.com/hemanth22/ansible-role-intellipaat.git  

__Devops Project code:__ https://github.com/hemanth22/Capstone.git

2. Go to your AWS Account and create AWS Access Key and AWS Secret Key from Amazon IAM console.  

3. Go to AWS account and create a keypair and download .pem file.  

4. Configure the AWS EC2 __Access Key__ and __Secret Key__ in the travis CI as below.  

![Image of travisconfig](https://raw.githubusercontent.com/hemanth22/Images/master/travisconfig.png)

## Executing Devops Project  

1. Now go to ansible-role-intellipaat repository in your github account and modify below values in `defaults/main.yml` and commit in your github repository.  

keypair: hemanth __(add your ec2 keypair)__  
security_group: sg-0fa454335a1f75b19 __(add security group id from ec2 console)__    
vpc_subnet_id: subnet-05078fa4222866fef __(add vpc id from ec2 console)__  


2. After committing above changes, Travis CI will start three ec2 instances as shown in below link.  

```yaml
 Remove log  Raw log
0.00s0.13s0.06s
worker_info
Worker information
0.13s0.00s0.01s0.00s0.01s
system_info
Build system information
0.04s0.00s0.42s0.18s0.05s0.00s0.04s0.00s0.01s0.01s0.01s0.01s0.01s0.00s0.00s0.02s0.00s0.01s0.27s0.00s0.00s0.00s0.01s0.00s0.09s0.00s0.73s0.00s0.09s6.03s0.00s2.25s0.00s2.09s
docker_mtu
resolvconf
services
3.01s$ sudo systemctl start docker
git.checkout
0.48s$ git clone --depth=50 --branch=master https://github.com/hemanth22/ansible-role-intellipaat.git hemanth22/ansible-role-intellipaat
0.01s
Setting environment variables from repository settings
$ export TicketApi=[secure]
$ export access_key=[secure]
$ export secret_key=[secure]
Setting environment variables from .travis.yml
$ export ROLE_NAME=intellipaat
$ export MOLECULE_DISTRO=centos7
0.01s$ source ~/virtualenv/python3.6/bin/activate
$ python --version
Python 3.6.7
$ pip --version
pip 19.0.3 from /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/pip (python 3.6)
install
39.62s$ pip install molecule docker
before_script.1
0.00s$ cd ../
before_script.2
0.00s$ mv ansible-role-$ROLE_NAME hemanth22.$ROLE_NAME
before_script.3
0.00s$ cd hemanth22.$ROLE_NAME
132.00s$ molecule test
--> Validating schema /home/travis/build/hemanth22/hemanth22.intellipaat/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix
    
└── default
    ├── lint
    ├── destroy
    ├── syntax
    ├── create
    ├── converge
    ├── verify
    └── destroy
    
--> Scenario: 'default'
--> Action: 'lint'
--> Executing Yamllint on files found in /home/travis/build/hemanth22/hemanth22.intellipaat/...
Lint completed successfully.
--> Executing Flake8 on files found in /home/travis/build/hemanth22/hemanth22.intellipaat/molecule/default/tests/...
Lint completed successfully.
--> Executing Ansible Lint on /home/travis/build/hemanth22/hemanth22.intellipaat/molecule/default/playbook.yml...
Lint completed successfully.
--> Scenario: 'default'
--> Action: 'destroy'
--> Sanity checks: 'docker'
    
    PLAY [Destroy] *****************************************************************
    
    TASK [Destroy molecule instance(s)] ********************************************
    changed: [localhost] => (item=instance)
    
    TASK [Wait for instance(s) deletion to complete] *******************************
    ok: [localhost] => (item=None)
    ok: [localhost]
    
    TASK [Delete docker network(s)] ************************************************
    
    PLAY RECAP *********************************************************************
    localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
    
--> Scenario: 'default'
--> Action: 'syntax'
--> Sanity checks: 'docker'
    
    playbook: /home/travis/build/hemanth22/hemanth22.intellipaat/molecule/default/playbook.yml
--> Scenario: 'default'
--> Action: 'create'
    
    PLAY [Create] ******************************************************************
    
    TASK [Log into a Docker registry] **********************************************
    skipping: [localhost] => (item=None) 
    
    TASK [Create Dockerfiles from image names] *************************************
    skipping: [localhost] => (item=None) 
    
    TASK [Determine which docker image info module to use] *************************
    ok: [localhost]
    
    TASK [Discover local Docker images] ********************************************
    ok: [localhost] => (item=None)
    ok: [localhost]
    
    TASK [Build an Ansible compatible image (new)] *********************************
    skipping: [localhost] => (item=molecule_local/geerlingguy/docker-centos7-ansible:latest) 
    
    TASK [Build an Ansible compatible image (old)] *********************************
    skipping: [localhost] => (item=molecule_local/geerlingguy/docker-centos7-ansible:latest) 
    
    TASK [Create docker network(s)] ************************************************
    
    TASK [Determine the CMD directives] ********************************************
    ok: [localhost] => (item=None)
    ok: [localhost]
    
    TASK [Create molecule instance(s)] *********************************************
    changed: [localhost] => (item=instance)
    
    TASK [Wait for instance(s) creation to complete] *******************************
    FAILED - RETRYING: Wait for instance(s) creation to complete (300 retries left).
    FAILED - RETRYING: Wait for instance(s) creation to complete (299 retries left).
    FAILED - RETRYING: Wait for instance(s) creation to complete (298 retries left).
    changed: [localhost] => (item=None)
    changed: [localhost]
    
    PLAY RECAP *********************************************************************
    localhost                  : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
    
--> Scenario: 'default'
--> Action: 'converge'
    
    PLAY [Converge] ****************************************************************
    
    TASK [hemanth22.intellipaat : Installing boto.] ********************************
    changed: [instance]
    
    TASK [hemanth22.intellipaat : Launch instance of jenkins and puppet] ***********
    changed: [instance]
    
    TASK [hemanth22.intellipaat : Add new instance to host group] ******************
    changed: [instance] => (item={'kernel': None, 'ebs_optimized': False, 'root_device_type': 'ebs', 'private_dns_name': 'ip-10-0-5-7.us-west-2.compute.internal', 'public_ip': '34.211.180.85', 'private_ip': '10.0.5.7', 'id': 'i-055734da0b45fccd6', 'block_device_mapping': {'/dev/sda1': {'status': 'attached', 'delete_on_termination': True, 'volume_id': 'vol-05cf77a67e6ef1754'}}, 'state': 'running', 'virtualization_type': 'hvm', 'root_device_name': '/dev/sda1', 'ramdisk': None, 'tags': {'Environment': 'Production', 'Name': 'Master'}, 'key_name': 'hemanth', 'image_id': 'ami-01ed306a12b7d1c96', 'tenancy': 'default', 'groups': {'sg-0fa454335a1f75b19': 'allports'}, 'public_dns_name': 'ec2-34-211-180-85.us-west-2.compute.amazonaws.com', 'state_code': 16, 'placement': 'us-west-2a', 'ami_launch_index': '0', 'dns_name': 'ec2-34-211-180-85.us-west-2.compute.amazonaws.com', 'region': 'us-west-2', 'launch_time': '2020-01-18T10:43:29.000Z', 'instance_type': 't2.micro', 'architecture': 'x86_64', 'hypervisor': 'xen'})
    
    TASK [hemanth22.intellipaat : Launch prod server instance] *********************
    changed: [instance]
    
    TASK [hemanth22.intellipaat : Add new instance to host group] ******************
    changed: [instance] => (item={'kernel': None, 'ebs_optimized': False, 'root_device_type': 'ebs', 'private_dns_name': 'ip-10-0-5-100.us-west-2.compute.internal', 'public_ip': '34.219.56.90', 'private_ip': '10.0.5.100', 'id': 'i-0ac3aab492ff6b92a', 'block_device_mapping': {'/dev/sda1': {'status': 'attached', 'delete_on_termination': True, 'volume_id': 'vol-0bc0f9621ad4f0385'}}, 'state': 'running', 'virtualization_type': 'hvm', 'root_device_name': '/dev/sda1', 'ramdisk': None, 'tags': {'Environment': 'Production', 'Name': 'puppet-agent-prod'}, 'key_name': 'hemanth', 'image_id': 'ami-01ed306a12b7d1c96', 'tenancy': 'default', 'groups': {'sg-0fa454335a1f75b19': 'allports'}, 'public_dns_name': 'ec2-34-219-56-90.us-west-2.compute.amazonaws.com', 'state_code': 16, 'placement': 'us-west-2a', 'ami_launch_index': '0', 'dns_name': 'ec2-34-219-56-90.us-west-2.compute.amazonaws.com', 'region': 'us-west-2', 'launch_time': '2020-01-18T10:43:59.000Z', 'instance_type': 't2.micro', 'architecture': 'x86_64', 'hypervisor': 'xen'})
    
    TASK [hemanth22.intellipaat : Launch test server instance] *********************
    changed: [instance]
    
    TASK [hemanth22.intellipaat : Add new instance to host group] ******************
    changed: [instance] => (item={'kernel': None, 'ebs_optimized': False, 'root_device_type': 'ebs', 'private_dns_name': 'ip-10-0-5-29.us-west-2.compute.internal', 'public_ip': '34.221.222.213', 'private_ip': '10.0.5.29', 'id': 'i-026a5a9bd17fd28ed', 'block_device_mapping': {'/dev/sda1': {'status': 'attached', 'delete_on_termination': True, 'volume_id': 'vol-0a43b417d1a952a81'}}, 'state': 'running', 'virtualization_type': 'hvm', 'root_device_name': '/dev/sda1', 'ramdisk': None, 'tags': {'Environment': 'Development', 'Name': 'puppet-agent-test'}, 'key_name': 'hemanth', 'image_id': 'ami-01ed306a12b7d1c96', 'tenancy': 'default', 'groups': {'sg-0fa454335a1f75b19': 'allports'}, 'public_dns_name': 'ec2-34-221-222-213.us-west-2.compute.amazonaws.com', 'state_code': 16, 'placement': 'us-west-2a', 'ami_launch_index': '0', 'dns_name': 'ec2-34-221-222-213.us-west-2.compute.amazonaws.com', 'region': 'us-west-2', 'launch_time': '2020-01-18T10:44:34.000Z', 'instance_type': 't2.micro', 'architecture': 'x86_64', 'hypervisor': 'xen'})
    
    PLAY RECAP *********************************************************************
    instance                   : ok=7    changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    
--> Scenario: 'default'
--> Action: 'verify'
--> Executing Testinfra tests found in /home/travis/build/hemanth22/hemanth22.intellipaat/molecule/default/tests/...
    ============================= test session starts ==============================
    platform linux -- Python 3.6.7, pytest-4.3.1, py-1.7.0, pluggy-0.8.0
    rootdir: /home/travis/build/hemanth22/hemanth22.intellipaat/molecule/default, inifile:
    plugins: testinfra-3.4.0
collected 1 item                                                               
    
    tests/test_default.py .                                                  [100%]
    
    =========================== 1 passed in 1.37 seconds ===========================
Verifier completed successfully.
--> Scenario: 'default'
--> Action: 'destroy'
    
    PLAY [Destroy] *****************************************************************
    
    TASK [Destroy molecule instance(s)] ********************************************
    changed: [localhost] => (item=instance)
    
    TASK [Wait for instance(s) deletion to complete] *******************************
    FAILED - RETRYING: Wait for instance(s) deletion to complete (300 retries left).
    changed: [localhost] => (item=None)
    changed: [localhost]
    
    TASK [Delete docker network(s)] ************************************************
    
    PLAY RECAP *********************************************************************
    localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
    
--> Pruning extra files from scenario ephemeral directory
The command "molecule test" exited with 0.
Done. Your build exited with 0.
```
3. Now configure the ip address in /etc/hosts for puppet requirement using below command and test the puppet ip address with ping.  

```
echo "10.0.5.7 puppet" >> /etc/hosts
ping puppet -c 5
```

4. Now stop the jenkins using command `systemctl stop jenkins`, and start the puppet server using command `systemctl start puppetserver` and configure the puppet module using below commands.  

```
cd /etc/puppetlabs/code/environments/production/modules

pdk new module abc-git

cd /etc/puppetlabs/code/environments/production/modules/git/manifests

wget -O init.pp https://gist.github.com/hemanth22/ddbb6f9e8e6cce155a11e90c8208f422/raw

cd /etc/puppetlabs/code/environments/production/modules/git

puppet parser validate manifests/init.pp
```  

5. Now login to test and prod instance using ssh and start the puppet agent using command `systemctl start puppet`.  

6. In the test and prod instance execute below command to send the signed fingerprint to puppet server.  

`puppet agent --fingerprint`

7. Now login to jenkins and puppetserver hosted instance and execute below commands to check and allow the signed fingerprint.  

```
puppetserver ca list

puppetserver ca sign --certname ip-10-0-5-100.us-west-2.compute.internal
puppetserver ca sign --certname ip-10-0-5-29.us-west-2.compute.internal
```
It will be sign the signature in the puppetserver as below.  

```
# puppetserver ca list --all
Signed Certificates:
    puppet                                    (SHA256)  7B:B8:9A:F4:74:D2:60:31:7E:3E:6E:A9:A3:EE:39:E0:6D:1A:1B:D0:6F:75:3D:B6:F6:92:FD:A3:41:97:DC:AA	alt names: ["DNS:puppet", "DNS:puppet"]
    ip-10-0-5-100.us-west-2.compute.internal   (SHA256)  3A:E5:F4:12:CF:12:7E:87:DC:E5:CF:97:B0:C6:E7:C4:DC:69:55:B9:6F:FA:ED:5E:8B:14:F3:37:09:D8:84:EB
    ip-10-0-5-29.us-west-2.compute.internal   (SHA256)  DE:CE:9C:35:C5:16:38:32:C5:E8:6C:1C:0E:D9:CA:79:C4:8B:CC:D2:7C:72:3F:E6:86:3C:A8:59:F1:51:E7:66
```
8. Now go to production manifests directions in puppetserver and add site.pp code.

`cd /etc/puppetlabs/code/environments/production/manifests`

vim site.pp
```
node ip-10-0-5-100 {
  include git
}
node ip-10-0-5-29 {
  include git
}
```


9. Now execute below command in test and prod instances to automatically provision or check the availability of required provision to test and prod instances.

`puppet agent -t`

10. After completing provising, stop the puppet server using below command.  
`systemctl stop puppetserver` 

and start the jenkins server using below command.  

`systemctl start jenkins`  

11. Now create a __Multibranch pipeline with defaults__ job in jenkins and give the capstone project link, it will automatically scans the capstone project, it will creates and execute the jobs as below.  

![Image of Jenkins](https://raw.githubusercontent.com/hemanth22/Images/master/Jenkins.jpg)

## Test case output.

As per Jenkinsfile pipeline code, it will test the code using selenium headless web test and display's output as below.  

![Image of testcase](https://raw.githubusercontent.com/hemanth22/Images/master/testcase.jpg)  

## Deployed output in production server.  

Below is the output of the website deployed in production server.  

![Image of production webpage](https://raw.githubusercontent.com/hemanth22/Images/master/webpage.jpg)  

