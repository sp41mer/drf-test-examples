# Cluster deployment
Deployment to cluster via Kubernetes

## Set-up master node
```sudo kubeadm init --pod-network-cidr=10.244.0.0/16```
```kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml```

## Add node to cluster
1. Create token at master node:
```kubeadm token create --print-join-command```

2. Join node with command:
Example: ```kubeadm join 77.244.214.196:6443 --token 7zhikb.zjhm7sf2yz3owzjd --discovery-token-ca-cert-hash sha256:9ca2c0bf3e0440a349a2c40ce57aca23acf3841d28522087b969b59efe41b980```

## Update image version
1. via console editor:
```KUBE_EDITOR="nano" kubectl edit deployment django-deployment```
2. via Dashboard: connect to `77.244.214.196:30170`, then just change image parameter

## Remove node from cluster
1. At worker node:
```kubeadm reset```
2. At master node:
```kubectl delete node <NODE_NAME>}```