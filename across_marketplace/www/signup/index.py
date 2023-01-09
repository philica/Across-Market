import frappe

no_cache=1

def get_context(context):
  context.csrf_token = frappe.sessions.get_csrf_token()
  print ("***********************************************************************" +"from index.py / signup")
  print("\n\n\n\n")
  
  print (context.csrf_token)

  print("\n\n\n\n")
  print ("**********************************************")