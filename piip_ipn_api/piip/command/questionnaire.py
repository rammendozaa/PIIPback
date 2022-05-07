from piip.models.questionnaire import Questionnaire
from piip.models.questionnaire import QuestionnaireQuestion
from piip.services.database.setup import session
from piip.models.question import SoftSkillQuestion

def insert_questionnaire(create_questionnaire):
    questionnaire = Questionnaire(
        title=create_questionnaire.title,
        description=create_questionnaire.description,
        total_questions=len(create_questionnaire.questions),
    )
    session.add(questionnaire)
    session.commit()
    questions = create_questionnaire.questions
    for question in questions:
        options = question["answerOptions"]
        incorrect_options = []
        answer = None
        for option in options:
            if option["isCorrect"]:
                answer = option["answerText"]
            else:
                incorrect_options.append(option["answerText"])
        option_1 = incorrect_options[0]
        option_2 = incorrect_options[1]
        option_3 = incorrect_options[2]
        new_question = QuestionnaireQuestion(
            questionnaire_id=questionnaire.id,
            question=question["questionText"],
            answer=answer,
            option_1=option_1,
            option_2=option_2,
            option_3=option_3,
        )
        session.add(new_question)
        session.commit()
    return questionnaire


def create_soft_skill_question(soft_skill_question_to_add):
    session.add(soft_skill_question_to_add)
    session.commit()
    return soft_skill_question_to_add


def get_all_soft_skill_questions():
    return (
        session.query(SoftSkillQuestion)
        .filter(SoftSkillQuestion.is_active == True)
        .all()
    )


def get_soft_skill_question(question_id):
    return (
        session.query(SoftSkillQuestion).get(question_id)
    )