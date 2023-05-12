# import os
# from pywinauto.application import Application # import pywinauto
# # app = Application(backend='uia')
# # app.connect(title_re=".*Chrome.*")
# # element_name="Address and search bar"
# # dlg = app.top_window()

# # url = dlg.child_window(title=element_name, control_type="Edit").get_value() # get url from database
# # print(url)# print url
# # # -/\-/\-/\-/\-/\-/\-*** HAPPY CODING ***-/\-/\-/\-/\-/\-/\-/\-

# app = Application(backend="win32")
# # app.connect(path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', timeout=20)
# app.connect(title_re=".*Chrome", timeout=10, found_index=0)
# dialogs = app.windows()

# # app.Properties.print_control_identifiers()
# for d in dialogs:
# 	print(d)

import pywinauto
desktop = pywinauto.Desktop(backend="win32")
window = desktop.windows(title_re=".* Google Chrome$", control_type="Pane")
wrapper_list = window
print(window)
for wrapper in wrapper_list:
    print(wrapper.window_text())