# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "silent_print"
app_title = "Silent Print"
app_publisher = "Roque Vera"
app_description = "Silent print using https://github.com/imTigger/webapp-hardware-bridge"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "roquegv@gmail.com"
app_license = "MIT"

# injected in desk.html
app_include_js = "assets/silent_print/js/silent_print.js"

page_js = {"point-of-sale" : "public/js/silent_print.js"}
