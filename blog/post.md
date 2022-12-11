Walkthrough for installing Kubernetes as a 1 control-plane and 3 worker node cluster using Ansible.

This is part 3 of a multi-part series where we continue building off of the previous parts. To catch up to where we are at check out the previous walkthroughs:
 1. [Using VMWare ESXi 8 and vCenter 8 in your homelab for free](https://perdue.dev/using-vmware-esxi-8-and-vcenter-8-in-your-homelab-for-free/) - part 1
 1. [Creating VMs for Kubernetes using Terraform and VMWare vSphere](https://perdue.dev/creating-vms-for-kubernetes-using-terraform-and-vmware-vsphere/) - part 2

# The goal of this series
This series is for you if you are interested in making management of your homelab something more turn-key. It is also for you if you are looking for something to help get hands-on experience to move from hobby tinkering to tools used in the workplace for managing infrastructure like Kubernetes clusters.

The series is an end-to-end walkthrough from installing ESXi on bare metal up to having homelab tools (Jenkins, Kubernetes dashboard) running in a Kubernenetes cluster using infrastructure as code practices to allow you to spin up and manage this whole setup through terraform and ansible.

The end-state Kubernetes cluster we will be creating will have some developer-focused tools deployed which will be described in more detail in part 4. All tools are deployed from code.<br/>
![homelab_tools-1](https://perdue.dev/content/images/2022/12/homelab_tools-1.png)


## Series Notes
To keep this series managable, I will skip over basics of why and how to use tools like terraform and ansible - this series will jump right in using the tools. If you are coming without a basic understanding of those tools, I would suggest running through some tutorials. There are fantastic write ups for those elsewhere.

This is a walkthrough that is meant to be adapted to your network design and hardware. It is best suited for those that have a single homelab machine where ESXi will be installed directly on the hardware and a vCenter instance will be started up within the ESXi host. Also, it should go without needing to say it, but this is not production grade - things like valid tls certificates are not included.

# This guide
At the end of this guide, we will have 4 Ubuntu virtual machines created through the vSphere provider. To keep things defined as code, we will be using [cloud-init](https://cloudinit.readthedocs.io/en/latest/) in [Ubuntu cloud images](https://cloud-images.ubuntu.com/) to allow us to pass in configuration like our OS user accounts, hostname, ssh keys, and storage mount points. For an overview of the hardware we are using, please see [Infrastructure Overview](https://perdue.dev/using-vmware-esxi-8-and-vcenter-8-in-your-homelab-for-free/#infrastructure-overview) from part 1.

All this configuration will be managed through terraform templates. Let's get started.


# Guide
1. [Get companion code](#get-companion-code)
1. [Wrap Up](#wrap-up)


# Get companion code
The code this guide uses is available at [https://github.com/markperdue/kubernetes-ansible](https://github.com/markperdue/kubernetes-ansible). Clone the companion code repo to have the best experience following along.


# TIP
ssh-keyscan -H -t rsa c1-cp1.lab >> ~/.ssh/known_hosts
ssh-keyscan -H -t rsa c1-node1.lab >> ~/.ssh/known_hosts
ssh-keyscan -H -t rsa c1-node2.lab >> ~/.ssh/known_hosts
ssh-keyscan -H -t rsa c1-node3.lab >> ~/.ssh/known_hosts

# Wrap Up
And with that, we now have a Kubernetes cluster! In the final guide, we will install tools into the cluster like Jenkins and a Kubernetes dashboard. We will also have Jenkins spin up with a pipeline that will deploy a sample go app to our cluster and expose the service using a load balancing tool called [MetalLB](https://metallb.universe.tf/)

Continue to part 4 at TODO_ONCE_PUBLISHED
