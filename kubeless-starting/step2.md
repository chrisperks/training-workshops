Load a function from a `.py` file

`kubeless function deploy upper --runtime python2.7 \
                              --handler upper.handler \
                              --from-file upper.py`{{execute}}

Keep checking for the function to come online

`kubeless function ls`{{execute}}

Take a look in the sample `upper.py` file

`cat upper.py`{{execute}}

Some facts while we wait: 

- Kubeless can execute code in `Python, Node.js, Ruby, PHP, Go, .NET, Ballerina`
- Once loaded, you can execute functions via `HTTP` calls or PubSub using `Kafka` triggers.