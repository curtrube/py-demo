from survey import AnonymousSurvey

# Define a question and make a survey
question = "What is your favorite programming language?"
my_survey = AnonymousSurvey(question)

# Show the question and store the responses
my_survey.show_question()
print("Enter 'q' to quit.")

while True:
    response = input("Progamming Language: ")
    if response == "q":
        break

    my_survey.store_response(response)

# Show the survey results
my_survey.show_results()
