import frappe



def get_context(context):
    context.user = frappe.session.user
    context.csrf_token = frappe.sessions.get_csrf_token()
    custom_items = frappe.get_list('Item',filters={'variant_of': 'coffee-variants'})
    context.custom_item = []
    for c in custom_items:
        item_name = c.name.split('-')
        region = item_name[2]
        origin = item_name[3]
        symbol = item_name[4]
        # item={"region":region,"origin":origin,"symbol":symbol}
        item = [region,origin,symbol]
        context.custom_item.append(item)
        print(context.custom_item)
  
    return context
    


