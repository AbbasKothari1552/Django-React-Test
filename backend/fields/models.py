from django.db import models
from django.core.exceptions import ValidationError
from products.models import Product
from categories.models import Category

class Field(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.field_name

class ProductFieldValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    field_value = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_field_value(self):
        field_value = self.field_value
        field_type = field_value.get('type')
        value = field_value.get('value')
        
        if field_type == 'integer':
            return int(value)
        elif field_type == 'decimal':
            return float(value)
        elif field_type == 'boolean':
            return bool(value)
        elif field_type == 'string':
            return str(value)
        elif field_type == 'json':
            return value  # Assuming nested JSON
        else:
            return value  # Default case, return as is

    def clean(self):
        field_value = self.field_value
        field_type = field_value.get('type')
        value = field_value.get('value')
        
        if field_type == 'integer' and not isinstance(value, int):
            raise ValidationError('Value must be an integer')
        elif field_type == 'decimal' and not isinstance(value, (int, float)):
            raise ValidationError('Value must be a decimal')
        elif field_type == 'boolean' and not isinstance(value, bool):
            raise ValidationError('Value must be a boolean')
        elif field_type == 'string' and not isinstance(value, str):
            raise ValidationError('Value must be a string')
        elif field_type == 'json' and not isinstance(value, dict):
            raise ValidationError('Value must be a JSON object')
        else:
            raise ValidationError(f'Unknown field type: {field_type}')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} - {self.field}'

