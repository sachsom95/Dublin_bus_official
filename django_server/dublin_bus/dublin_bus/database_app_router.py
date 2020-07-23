#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# class DatabaseAppsRouter(object):
#     def db_for_read(self,model,**hints):
#         if model._meta.app_label == 'dublin_bus':
#             return 'dublin_bus'
#         else:
#             return None
#
#     def db_for_write(self,model,**hints):
#         if model._meta.app_label == 'dublin_bus':
#             return 'dublin_bus'
#         else:
#             return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'dublin_bus':
#             return db == 'dublin_bus'
#         else:
#             return None