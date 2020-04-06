# This is a standard python file
# We can use this file for our Kubeless function

def handler(event, context):
   print event
   return uppercase(event['data'])

# A silly function to apply upper() to each value in a dictionary
def uppercase(dict): 
   return {k:v.upper() for k, v in dict.items()}
