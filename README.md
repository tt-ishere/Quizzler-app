# Quizzler-app
 This is a user-friendly quiz application
By using OOP method, this code imports three modules: Question class from question_model, question data from data, and the QuizBrain and QuizInterface classes from quiz_brain and ui, respectively. The code then creates a question_bank list by looping through the question_data and appending each question to the question_bank list as a Question object.

The QuizBrain constructor is then called with the question_bank list as its argument, creating a new quiz instance. Finally, the QuizInterface constructor is called with the quiz object as its argument, creating a graphical user interface for the quiz.

This code allows the user to take a quiz with multiple-choice questions. The question data is stored in question_data, which is a list of dictionaries, with each dictionary containing the question and its answer choices. The Question class is defined in question_model to create a question object that stores the question text and correct answer.

The QuizBrain class in quiz_brain handles the quiz logic, such as checking the user's answer and keeping track of the score. The QuizInterface class in ui creates the graphical user interface for the quiz, displaying the questions, answer choices, and current score.

Overall, this code provides a user-friendly quiz application by importing necessary modules, processing question data, creating a QuizBrain instance with the questions, and creating a graphical interface for the quiz with the QuizInterface class.