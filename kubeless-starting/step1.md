Create a Kubernetes namespace to hold our Kubeless cluster

`kubectl create ns kubeless`{{execute}}

Use a Kubernetes manifest to install Kubeless to our cluster

`kubectl create -f https://github.com/kubeless/kubeless/releases/download/v1.0.0/kubeless-v1.0.0.yaml`{{execute}}

Show the pods created during our installation

`kubectl get pods -n kubeless`{{execute}}

Show the state of our latest deployment

`kubectl get deployment -n kubeless`{{execute}}

#### Further reading

- [How Kubernetes deployments work](https://www.youtube.com/watch?v=mNK14yXIZF4)
- [Organizing Kubernetes with Namespaces](https://www.youtube.com/watch?v=xpnZX3if9Tc)