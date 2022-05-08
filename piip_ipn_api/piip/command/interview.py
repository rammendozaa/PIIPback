from piip.services.database.setup import session
from piip.models.template import TemplateActivity
from piip.query.user import (
    update_user_template_activity_by_id,
)
from piip.models.interview import Interview
from piip.models.user import UserTemplateActivity


def update_interview(user_id, interview_id, interview_changes, role):
    interview = (
        session.query(Interview)
        .get(interview_id)
    )
    if not interview:
        return False
    interview.chosen_date = interview_changes.chosen_date
    interview.comment = interview_changes.comment
    if role != "user":
        interview.interview_url = interview_changes.interview_url
        interview.interview_code = interview_changes.interview_code
        interview.feedback = interview_changes.feedback
        interview.is_confirmed = interview_changes.is_confirmed
        if interview_changes.feedback is not None:
            user_activity = (
                session.query(UserTemplateActivity)
                .join(
                    TemplateActivity, 
                    TemplateActivity.id == UserTemplateActivity.template_activity_id
                )
                .filter(
                    UserTemplateActivity.user_id == user_id,
                    TemplateActivity.activity_type_id == 5,
                    TemplateActivity.external_reference == interview_id,
                )
                .first()
            )
            interview.is_active = False
            if user_activity:
                update_user_template_activity_by_id(user_activity.id, 4)
    session.add(interview)
    session.commit()
    return True


def get_interviews(admin_id=None, interview_id=None):
    if interview_id is not None:
        return (
            session.query(Interview).get(interview_id)
        )
    if admin_id is not None:
        return (
            session.query(Interview)
            .filter(
                Interview.admin_id == admin_id,
                Interview.is_active == True,
            )
            .order_by(
                Interview.chosen_date.desc()
            )
            .all()
        )
    return session.query(Interview).all()