from marshmallow import fields, post_dump

from piip.models.company_tracking import CompanyTracking, CompanyTrackingLinks
from piip.models.dictionary import DictCompany
from piip.schema.base_schema import BaseSchema
from piip.services.database.setup import session


class CompanyTrackingLinksSchema(BaseSchema):
    __model__ = CompanyTrackingLinks

    id = fields.Integer(dump_only=True)
    company_tracking_id = fields.Integer(data_key="companyTrackingId", allow_none=True)
    description = fields.String(allow_none=True)
    url = fields.String(allow_none=True)
    is_active = fields.Boolean(allow_none=True)


class CompanyTrackingSchema(BaseSchema):
    __model__ = CompanyTracking

    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(data_key="userId", allow_none=True)
    company_id = fields.Integer(data_key="companyId", allow_none=True)
    status_id = fields.Integer(data_key="statusId", allow_none=True)
    application_url = fields.String(data_key="applicationURL", allow_none=True)
    interview_date = fields.String(data_key="interviewDate", allow_none=True)

    tracking_links = fields.List(
        fields.Nested(CompanyTrackingLinksSchema), data_key="trackingLinks"
    )

    @post_dump
    def after_serialize(self, data, many, **kwargs):
        links = data.get("trackingLinks", None)
        if links:
            data["trackingLinks"] = list(
                filter(lambda x: x["is_active"] == True, links)
            )
        else:
            data["trackingLinks"] = []
        company = session.query(DictCompany).get(data["companyId"])
        if company:
            data["companyName"] = company.name
        else:
            data["companyName"] = "Facebook"
        return data
