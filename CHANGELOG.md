# Changelog
All notable changes to this project will be documented in this file.


## [2.11.0] - 2023-05-06
MD5 - 47c15f33b4ad1e47e2a66228b725dd4f

### Added
- IIP-40394 Blocked perpetual license key deployments from InfoScale 8.0.2 onwards
- ISAM-1437 Multiple RVG and diskgroup support for change_replication_state.yml playbook
- ISAM-575 Plumb VIP for on-premise machines

### Changed
- ISAM-1641 Updated unconfiguration of VVR for deletion of rvg_sg_name, mount_sg_name, logownergrp_sg_name if provided
- ISAM-1440 Improvised SFCFSHA configuration execution time by removing start and stop vcs while disabling fencing
- ISAM-1385 Remove dependency on disks parameter when diskgroup already exists for create_dg_vol.yml
- ISAM-1463 VVR configuration - used vxsnap command for data volumes 
- ISAM-1397, ISAM-1410 Support FQDN/IP for seednode in create_dg_vol.yml playbook 
- ISAM-1465 Skip disks parameter if given disk is already added in disk group previously for adddisk.yml playbook
- ISAM-1484 Updated module for identifying the EC2 
- Updated release matrix

### Fixed
- IIP-40970 Fixed rolling_upgrade.yml playbook which failed due to error encapsulated bootdisk upgrade requires a reboot
- ISAM-1526 Used common function for systemctl start/stop process
- IIP-41055 Seggrated EO Logging for SF, VCS, SFCFSHA/SFHA/SFCFS
- ISAM-1455 VVR fixes for separate creation for primary and secondary site
- ISAM-1588 SFCFSHA configuration fix for IS 7.4.1 (vxconfigd should to started before vxdmp followed by vxio, vxspec)
- ISAM-1453 Fixed cluster configuration failure post executing set_tunables.yml playbook
- ISAM-1558 Skip OS disk for DiskInit module
- ISAM-1602 Fixed issue for across AZ in AWS for routing for 4 node cluster
- ISAM-1601 ISAM-1624 SFCFSHA configuration and routing fix across AZ on RHEL 7 platform (AWS)
- ISAM-1483 Fix for handling nic speed exception

### Others
- ISAM-1466 ISAM-1464 Added msg on non-seednode for create_dg_vol and add_disks playbook
- ISAM-318 Making path as absolute to the script name for automated release matrix update


## [2.10.0] - 2023-03-31
MD5 - fd28693f80d81a131cdc7c0f10cc6250

### Added
- ISAM-158 Unconfigure Replication (VVR) using vvrresource.yml playbook (can also be used to delete primary and then secondary site separately)

### Changed
- ISAM-889 Support FQDN/IP for system in route_config.yml playbook
- ISAM-497 Support multiple DG creation (more than 9)
- Updated Release matrix

### Fixed
- STESC-7872 Fixed VVR configuration when agentinfo provided is null in vvrresource.yml playbook
- IIP-40738 Updated VRTSvxfs oslibs prerequisites for InfoScale 8.0.2 on RHEL 8 and RHEL 9 platform
- ISAM-848 Fixed Facters for cnfs/cifs configuration information
- ISAM-927 Fixed Facters for host interface information by removing dependancy on ifconfig
- ISAM-1302 Fixed services not coming online after reboot

### Other
- ISAM-318 Automate release matrix download from sort


## [2.9.0] - 2023-03-01
MD5 - dfc9e6c72c460d03816e82c73bd9551c

### Added
- ISAM-578 Added preonline trigger for logownergrp service group to come online on master
- ISAM-142, ISAM-157, ISAM-939 Playbook to change replication status to start/stop/pause/resume
- ISAM-526, ISAM-939 Using VVR playbook for separate VVR configuration for secondary/primary site individually

### Changed
- IIP-40638 Resolved race condition observed between disk initialization and DG creation
- ISAM-528 Added multinode LLT/VM/FS and clusterwide VM tunable support to set_tunables.yml Playbook
- IIP-40919 Updated Release matrix

### Fixed
- ISAM-491 Fixed fencing related information fetched in Facters and move them inside fencing
 IIP-40642 Fixed SF configuration failure for product FOUNDATION installed
- ISAM-490 Fixed llt and gab related information fetch issues in Facters 

### Others
- None


## [2.8.1] - 2023-02-01
MD5 - 5586fe45f901525123e66ac35e27edb0

### Added
- IIP-40408 Added support for non-master as seednode for VVR playbook
- ISAM-470 Playbook for Add and Remove disks from diskgroup

### Changed
- IIP-40425 Removed dependency on netadrr module for LLT/UDP configuration
- ISAM-579 Setting Critical as 1 for all VVR resources in VVR playbook
- ISAM-571 Added support for IP/FQDN for seednode in VVR playbook
- IIP-40639 Updated Release matrix

### Fixed
- IIP-40631 Fixed installation of InfoScale 8.0.2 failure on RHEL 9

### Other
- None


## [2.8.0] - 2023-01-06
MD5 - 704725b5afee7a3292f1c7fbf450a8da

### Added
- IIP-38752 InfoScale Workflow for end-to-end VVR solution deployment
- IIP-38752, IIP-39393 Added vvr_solution role for end-to-end VVR deployment and required files like main.json (vars_file), yaml (infoscale_solution)
- IIP-40405 InfoScale 8.0.2 support on RHEL9

### Changed
- IIP-39572 Added support of FQDN/IP to systems parameter for VCS/SFHA/SFCFSHA UDP and TCP link configuration
- IIP-40396 Supporting private IP for onenode CP server
- IIP-39493 In configuration playbooks cluster_uuid is optional parameter
- IIP-40402 Updated release matrix

### Fixed
- IIP-40392 SF configuration Fix (EO Logging)
- IIP-40310 Fixed Rest Server configuration for default option
- IIP-40395 Fixed RouteConfig playbook for incorrect gateway value fetched
- IIP-39659 Fixed overlayIP issues for VVR configuration
- IIP-40429 Fix for get_tunables exception in module site-facters
- IIP-40449 Fixed issues encountered during VVR Automation 

### Other
- IIP-40375 get tunables code refactored change to class linuxproduct (undocumented)
- IIP-40418 Added a check to return when unconfiguring fencing on SFCFSHA configured cluster. SFCFSHA requires at least disabled fencing. Unconfiguring fencing is not a valid option.


## [2.7.0] - 2022-12-02
MD5 - 6abf46d30b6ae0b646fdf1470d9d19ac

### Added
- IIP-40137 Added the feature to set vcs, vxvm and vxfs tunables
- IIP-38560 Added support to set route and rules for subnet across availability zones on AWS
- IIP- 40138 Added support to get all the changed (not default) vcs, vxvm and vxfs tunables 

### Changed
- IIP-39876 Updated Release matrix

### Fixed                
- IIP-39645 Fixed multiple product patches on target nodes while installing InfoScale
- IIP-39897 Secure Cluster configuration fixes for AWS 

### Other
-None


## [2.6.1] - 2022-11-02
MD5 - 9e431fd1c3e49fc58b7b5a29d5d511dc 

### Added
- None

### Changed
- IIP-38772 Added EO Logging options for component configurations to enable and disable EO compliant logging
- IIP-39876 Updated Release matrix

### Fixed
- IIP-39750 GCO configuration fix for AWS - added AWSIP resource for VIP
- IIP-39658 VVR fixes for Azure - added azureAuth and azureIP resources for VIP
- IIP-39735 AWS_CLI fix needed for AWS platform

### Other
- None


## [2.6.0] - 2022-09-30
MD5 - 66f70b5692efec7c30c9fe2bf754865c

### Added
- IIP-39404 Provide support to enable and disable EO Logging

### Changed
- IIP-39494 Remove Passwordless SSH as the pre-requisite for Secure Cluster
- IIP-39643 Updated Release matrix 

### Fixed
- IIP-39276 Patch upgradation with InfoScale configured product 
- STESC-7352 InfoScale 7.4.1 for RHEL 8.6 Python 2.6
- IIP-39540 CVR configuration for 2 node primary and 2 node secondary site for Azure platform
- IIP-39547 Secondary could not get information about VVR setup due to timeout
- IIP-39522 GCO configuration fails on Azure for 2 node primary and 2 node secondary site

### Other
- IIP-39405 Enabled CVR for 2 node primary and 2 node secondary site on Azure


## [2.5.1] - 2022-09-02
MD5 - 3cb7a29cbf906fbe4958ce2df4b471f2

### Added
- IIP-37954 Display message and documentation link for using AWS agents since AWS CLI must be installed and configured on AWS machines.

### Changed
- IIP-39017+IIP-38803 Updating cloud identification to also support containerized environment
- IIP-39363 Seednode is optional and enabled support for FQDN/IP for start and stop service playbooks
- IIP-39361 Seednode is optional for secure cluster playbook
- IIP-39468 Updated release matrix

### Fixed
- IIP-38122 Race condition fix for secure cluster playbook      
- IIP-39485 Fixed VIP configuration playbook to avoid VIP configuration failure on provided NIC



## [2.5.0] - 2022-08-01

### Added
- IIP-38642 Added support to single private link on cloud (LLT/UDP)
- IIP-38674 Added support for deletion of master node and multiple nodes

### Changed
- IIP-38396 Added an option to create unformatted volume

### Fixed
