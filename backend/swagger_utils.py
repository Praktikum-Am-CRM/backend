from drf_yasg.generators import OpenAPISchemaGenerator


class SchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https"]
        return schema
