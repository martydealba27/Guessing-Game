from question import Question

#this is an array of all the question prompts that will be in the quiz
question_prompts = [
    "What color are apples? \n (a) Red \n (b) Purple \n (c) Orange \n\n",
    "What color are bananas? \n (a) Orange \n (b) Green \n (c) Yellow \n\n", 
    "What color are strawberries? \n (a) Pink \n (b) White \n (c) Red \n\n",
    "Are you good at golf? \n (a) Yes \n (b) You are the best in the world. \n (c) No \n\n"
]
#this is another array called questions and they have objects that are getting passed into the 
#we are creating three questions.  The number inside the [] is getting indexed from the array above
#the array above is question_prompts.
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"), 
    Question(question_prompts[3], "b")
]

#next we need to create a function that will run our test.
#we need to prompt the user for a input / ask a question
#we also need to check if the answer is correct. 

#questions, the array above, is going to get passed through this function
def run_test(questions):
    '''we are creating a variable called score.  we will incriment score up by one in the event we get a right answer.'''
    score = 0
    #for each question object inside the array, we are telling function to perform an action
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You received " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)

