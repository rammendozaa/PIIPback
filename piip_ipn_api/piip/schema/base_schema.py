from marshmallow import Schema, post_load

from piip.models.database_setup import PIIPModel


class BaseSchema(Schema):
    __model__ = PIIPModel

    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)


class DataclassSchema(Schema):
    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)
