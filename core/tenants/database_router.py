# # database_router.py
#
# class TenantDatabaseRouter:
#     def db_for_read(self, model, **hints):
#         if hasattr(model, 'tenant_id'):
#             # Read from the tenant-specific database based on the request context
#             tenant_identifier = getattr(model, 'tenant_id', None)
#             if tenant_identifier:
#                 return f'tenant_{tenant_identifier}'
#         return 'default'
#
#     def db_for_write(self, model, **hints):
#         if hasattr(model, 'tenant_id'):
#             # Write to the tenant-specific database based on the request context
#             tenant_identifier = getattr(model, 'tenant_id', None)
#             if tenant_identifier:
#                 return f'tenant_{tenant_identifier}'
#         return 'default'
