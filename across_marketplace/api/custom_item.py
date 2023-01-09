import frappe
import json

# create a new quotation
@frappe.whitelist()
def createQuote(*args,**kwargs):
	
	frappe.errprint(json.loads(frappe.form_dict.item))
	doc=frappe.get_doc(json.loads(frappe.form_dict.item))
	doc.insert()
	frappe.db.commit()
	doc.submit()
	frappe.db.commit()
	
	
#create a new request for quotation
@frappe.whitelist()
def createRequestForQuote(*args,**kwargs):
	print("request for quote")
	doc=frappe.get_doc(json.loads(frappe.form_dict.rfq))
	doc.insert()
	frappe.db.commit()
	doc.submit()
	frappe.db.commit()
    
