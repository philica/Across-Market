#created by philica 
# created at sep-23-2022

from logging import exception
import frappe
from frappe.core.doctype.user_permission.user_permission import UserPermission
from frappe.utils import pretty_date


# attach user role to the newly created user 
@frappe.whitelist()
def grant_customer_role(email):
    frappe.errprint(email)
    user = frappe.get_doc("User",email)
    user.db_set('role_profile_name',"Customer")
    frappe.db.commit()
    user.save(ignore_permissions=True)
    frappe.db.commit()
    