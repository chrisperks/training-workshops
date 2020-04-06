Let's take a look at the logs for our function

`kubeless function logs formatter`{{execute}}

And at any point, we can view a description:

`kubeless function describe formatter`{{execute}}

If we want to update a function, we can specify a new file: 

`kubeless function update formatter --from-file lower.py`{{execute}}

And re-call the function to view the new results:

`kubeless function call formatter --data '{"HeLlO":"WoRlD"}'`{{execute}}