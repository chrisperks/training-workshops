Load a function from a `.py` file

`kubeless function deploy formatter --runtime python2.7 \
                              --handler formatter.handler \
                              --from-file upper.py`{{execute}}

Keep checking for the function to come online

`kubeless function ls`{{execute}}

Take a look in the sample `formatter.py` file

`cat formatter.py`{{execute}}

Some facts while we wait: 

- Kubeless can execute code in `Python, Node.js, Ruby, PHP, Go, .NET, Ballerina`
- Once loaded, you can execute functions via `HTTP` calls or PubSub using `Kafka` triggers.