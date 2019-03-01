#coding=utf-8
import os
import sys

import django


########################不启用django服务而使用django###########################
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
os.chdir(dir_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")
django.setup()
##########################################################################