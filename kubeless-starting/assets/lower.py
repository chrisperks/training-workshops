# This is a standard python file
# We can use this file for our Kubeless function

def handler(event, context):
   print event
   return lowercase(event['data'])

# A silly function to apply lower() to each value in a dictionary
def lowercase(dict): 
   return {k:v.lower() for k, v in dict.items()}
