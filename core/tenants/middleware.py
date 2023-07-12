# middleware.py
from django.db import connection


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Identify the tenant using the request (e.g., subdomain or URL parameter)
        tenant_identifier = request.get_host().split(':')[0].split('.')[0].lower()
        request.tenant = tenant_identifier  # Set the tenant identifier in the request context
        print(tenant_identifier)
        connection.settings_dict["NAME"] = request.tenant
        response = self.get_response(request)
        return response


# .split('.')[0]
 # connection['default'].database = tenant_identifier

        # print(connection['default'])
        # print(connection)