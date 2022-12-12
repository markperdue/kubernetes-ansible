# Overview
An Ansible playbook that installs Kubernetes.

A guide for using this repo to spin up a Kubernetes cluster is available at [Installing your Kubernetes homelab cluster in minutes with Ansible](https://perdue.dev/installing-your-kubernetes-homelab-cluster-in-minutes-with-ansible/)


# Features
- containerd
- calico for pod networking

# Quickstart
```
ansible -i inventory/dev all -m ping

ansible-playbook -i inventory/dev playbooks/k8s_all.yaml

# reboot might be required after installation
ansible -i inventory/dev all -a "/sbin/reboot" --become
```
