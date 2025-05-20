from django.db.backends.postgresql import base, features, operations, schema
from django.utils import timezone

class DatabaseWrapper(base.DatabaseWrapper):
    def get_connection_params(self):
        params = super().get_connection_params()
        params['options'] = params.get('options', '') + ' -c timezone=UTC'
        return params

    def get_connection(self):
        conn = super().get_connection()
        # Désactive la vérification stricte UTC
        conn.tzinfo_factory = lambda offset: timezone.utc
        return conn

class DatabaseFeatures(features.DatabaseFeatures):
    pass

class DatabaseOperations(operations.DatabaseOperations):
    pass

class DatabaseSchemaEditor(schema.DatabaseSchemaEditor):
    pass