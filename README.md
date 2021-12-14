# Overview
An Ansible playbook that installs Kubernetes.

Integrates nicely as a secondary step to https://github.com/markperdue/vm-vsphere-cloud-init


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

# TODO
1. clean up kubeadm worker node onboarding section. right now we generate the token three times. one for each worker node
