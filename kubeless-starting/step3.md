`kubeless function call toy --data '{"hello":"world"}'`{{execute}}

`kubectl proxy --port 8080 &`{{execute}}

`curl --data '{"hello":"world"}' localhost:8080/api/v1/namespaces/default/services/toy:8080/proxy/ --header "Content-Type:application/json"`{{execute}}
