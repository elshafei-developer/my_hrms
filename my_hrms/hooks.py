app_name = "my_hrms"
app_title = "My Hrms"
app_publisher = "hassan hussein mohammed"
app_description = "this app will edit on app hrms for frappe HR"
app_email = "hassanhusseinmohammed.as@gmail.com"
app_license = "mit"
# required_apps = []



# ME to record custom doctype
fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/my_hrms/css/my_hrms.css"
# app_include_js = "/assets/my_hrms/js/employee/employee.js"

# include js, css files in header of web template
# web_include_css = "/assets/my_hrms/css/my_hrms.css"
# web_include_js = "/assets/my_hrms/js/my_hrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "my_hrms/public/scss/website"

# include js, css files in header of web form
# {"Employee": "public/js/employee/employee.js"}
# webform_include_js = {"Employee": "public/js/employee/employee.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Employee": "overrides/employee/employee.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "my_hrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "my_hrms.utils.jinja_methods",
# 	"filters": "my_hrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "my_hrms.install.before_install"
# after_install = "my_hrms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "my_hrms.uninstall.before_uninstall"
# after_uninstall = "my_hrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "my_hrms.utils.before_app_install"
# after_app_install = "my_hrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "my_hrms.utils.before_app_uninstall"
# after_app_uninstall = "my_hrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "my_hrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Employee": "my_hrms.overrides.employee.employee.CustomEmployee"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"my_hrms.tasks.all"
# 	],
# 	"daily": [
# 		"my_hrms.tasks.daily"
# 	],
# 	"hourly": [
# 		"my_hrms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"my_hrms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"my_hrms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "my_hrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "my_hrms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "my_hrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["my_hrms.utils.before_request"]
# after_request = ["my_hrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["my_hrms.utils.before_job"]
# after_job = ["my_hrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"my_hrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

