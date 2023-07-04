from data import question_data
from question_model import Question
from quiz_brain import Quizbrain


questin_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questin_bank.append(new_question)

quiz = Quizbrain(questin_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(questin_bank)}")