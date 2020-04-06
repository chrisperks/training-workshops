
`kubectl create ns kubeless`{{execute}}

`kubectl create -f https://github.com/kubeless/kubeless/releases/download/v1.0.0/kubeless-v1.0.0.yaml`{{execute}}

`kubectl get pods -n kubeless`{{execute}}
