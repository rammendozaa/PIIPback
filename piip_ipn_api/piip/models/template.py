from piip.models.database_setup import PIIPModel

from sqlalchemy import (
    Column, 
    Text, 
    ForeignKey, 
    Integer, 
    String)
from sqlalchemy.orm import relationship
from piip.models.constants import DATABASE


class Template(PIIPModel):
    __tablename__ = "TEMPLATE"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    position = Column(Integer)


class TemplateActivity(PIIPModel):
    __tablename__ = "TEMPLATE_ACTIVITY"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    template_id = Column(Integer, ForeignKey(f"{DATABASE}.TEMPLATE.id"))
    activity_type_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_ACTIVITY_TYPE.id"))
    position = Column(Integer)
    external_reference = Column(Integer)

    template = relationship("Template", foreign_keys=[template_id])
    activity = relationship("DictActivityType", foreign_keys=[activity_type_id])
