def handler(event, context):
   print event
   return uppercase(event['data'])

def uppercase(dict): 
   return {k:v.upper() for k, v in dict.items()}
