from admin import Admin
from login import User

info = Admin('balance', 'fulfudesfinest')
info.req_login_info()
info.group.admin_privilege()
info.show_privileges()
