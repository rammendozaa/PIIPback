from typing import List
from sqlalchemy.orm.relationships import RelationshipProperty
from piip.models.database_setup import PIIPModel

from sqlalchemy import (
    Column, 
    Text, 
    ForeignKey, 
    Integer, 
    String)
from sqlalchemy.orm import relationship
from piip.models.constants import DATABASE

class TemplateActivity(PIIPModel):
    __tablename__ = "TEMPLATE_ACTIVITY"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    template_section_id = Column(Integer, ForeignKey(f"{DATABASE}.TEMPLATE_SECTION.id"))
    activity_type_id = Column(Integer, ForeignKey(f"{DATABASE}.DICT_ACTIVITY_TYPE.id"))
    position = Column(Integer)
    external_reference = Column(Integer)

    template_section = relationship("TemplateSection", foreign_keys=[template_section_id], back_populates="activities")
    activity = relationship("DictActivityType", foreign_keys=[activity_type_id])


class TemplateSection(PIIPModel):
    __tablename__ = "TEMPLATE_SECTION"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    position = Column(Integer)
    template_id = Column(Integer, ForeignKey(f"{DATABASE}.TEMPLATE.id"))

    template = relationship("Template", foreign_keys=[template_id], back_populates="sections")
    activities : "RelationshipProperty[List[TemplateActivity]]" = relationship(
        "TemplateActivity", back_populates="template_section", lazy="dynamic"
    ) 


class Template(PIIPModel):
    __tablename__ = "TEMPLATE"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    position = Column(Integer)

    sections : "RelationshipProperty[List[TemplateSection]]" = relationship(
        "TemplateSection", back_populates="template", lazy="dynamic"
    ) 

