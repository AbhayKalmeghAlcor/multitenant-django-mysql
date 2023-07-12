from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TenantModel(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'tenant_model'  # Use the same table name for all tenants


class Product(TenantModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

