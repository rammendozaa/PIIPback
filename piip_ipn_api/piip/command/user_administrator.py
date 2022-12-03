from piip.command.company_tracking import getInterviewData
from piip.models import UserAdministrator
from piip.services.database.setup import session


def getMyStudents2(_user_id):
    activeUsers = (
        session.query(UserAdministrator)
        .filter_by(administrator_id=_user_id, is_active=1)
        .all()
    )
    cntAccepted = 0
    cntRejected = 0
    cntNever = 0
    for student in activeUsers:
        studentId = student.user_id
        interviewsData = getInterviewData(studentId)

        cntAcceptedTmp = 0
        cntRejectedTmp = 0

        for interview in interviewsData:
            if interview.status_id == 5:
                cntAcceptedTmp += 1
            elif interview.status_id == 6 or interview.status_id == 4:
                cntRejectedTmp += 1

        if cntAcceptedTmp == 0 and cntRejectedTmp == 0:
            cntNever = 0
        else:
            if cntAcceptedTmp > 0:
                cntAccepted += 1
            else:
                cntRejected += 1
    return {
        "cntAccepted2": cntAccepted,
        "cntRejected2": cntRejected,
        "cntNever2": cntNever,
    }


def getMyStudents(_user_id):
    activeUsers = (
        session.query(UserAdministrator).filter_by(administrator_id=_user_id).all()
    )
    cntAccepted = 0
    cntRejected = 0
    cntNever = 0
    for student in activeUsers:
        studentId = student.user_id
        interviewsData = getInterviewData(studentId)

        cntAcceptedTmp = 0
        cntRejectedTmp = 0

        for interview in interviewsData:
            if interview.status_id == 5:
                cntAcceptedTmp += 1
            elif interview.status_id == 6 or interview.status_id == 4:
                cntRejectedTmp += 1

        if cntAcceptedTmp == 0 and cntRejectedTmp == 0:
            cntNever = 0
        else:
            if cntAcceptedTmp > 0:
                cntAccepted += 1
            else:
                cntRejected += 1
    return {
        "cntAccepted": cntAccepted,
        "cntRejected": cntRejected,
        "cntNever": cntNever,
    }


def getNumberOfLosers(_user_id):
    activeUsers = (
        session.query(UserAdministrator)
        .filter_by(administrator_id=_user_id, is_graduate=0, is_active=0)
        .count()
    )
    return activeUsers


def getNumberOfGraduatedStudents(_user_id):
    activeUsers = (
        session.query(UserAdministrator)
        .filter_by(administrator_id=_user_id, is_graduate=1)
        .count()
    )
    return activeUsers


def getNumberOfActiveUsers(_user_id):
    activeUsers = (
        session.query(UserAdministrator)
        .filter_by(administrator_id=_user_id, is_active=1)
        .count()
    )
    return activeUsers
