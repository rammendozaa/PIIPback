from marshmallow import fields, post_dump
from piip.schema.base_schema import BaseSchema
from piip.models.company_tracking import CompanyTracking, CompanyTrackingLinks


class CompanyTrackingLinksSchema(BaseSchema):
    __model__ = CompanyTrackingLinks

    id = fields.Integer(dump_only=True)
    company_tracking_id = fields.Integer(data_key="companyTrackingId")
    description = fields.String()
    url = fields.String()
    is_active = fields.Boolean()


class CompanyTrackingSchema(BaseSchema):
    __model__ = CompanyTracking

    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(data_key="userId", allow_none=True)
    company_id = fields.Integer(data_key="companyId", allow_none=True)
    status_id = fields.Integer(data_key="statusId", allow_none=True)
    application_url = fields.String(data_key="applicationURL", allow_none=True)
    interview_date = fields.String(data_key="interviewDate", allow_none=True)
    
    tracking_links = fields.List(fields.Nested(CompanyTrackingLinksSchema), data_key="trackingLinks")
    @post_dump
    def after_serialize(self, data, many, **kwargs):
        links = data["trackingLinks"]
        data["trackingLinks"] = list(filter(lambda x: x["is_active"] == True, links))
        return data
