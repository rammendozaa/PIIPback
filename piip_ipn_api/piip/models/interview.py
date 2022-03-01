from piip.database_setup import PIIPModel

class Interview(PIIPModel):
    __tablename__ = "INTERVIEW"


class InterviewRequest(PIIPModel):
    __tablename__ = "INTERVIEW_REQUESTS"


class InterviewStatus(PIIPModel):
    __tablename__ = "INTERVIEW_STATUS"
