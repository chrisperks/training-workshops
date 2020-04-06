`kubeless function deploy toy --runtime python2.7 \
                              --handler toy.handler \
                              --from-file toy.py`{{execute}}

`kubeless function ls`{{execute}}

`cat toy.py`{{execute}}

`kubectl get pods`{{execute}}
