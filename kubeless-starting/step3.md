Let's use the Kubeless CLI to call our function with some simple JSON

`kubeless function call upper --data '{"hello":"world"}'`{{execute}}

Now, more usefully, let's open a HTTP proxy on port 8080

`kubectl proxy --port 8080 &`{{execute}}

So, we can use `curl` to call our function

`curl --data '{"hello":"world"}' localhost:8080/api/v1/namespaces/default/services/upper:8080/proxy/ --header "Content-Type:application/json"`{{execute}}
