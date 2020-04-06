def handler(event, context):
   print event
   return lowercase(event['data'])

def lowercase(dict): 
   return {k:v.lower() for k, v in dict.items()}
