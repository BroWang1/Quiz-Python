class Question: # This is a class or bluebrint/format of a question
    def __init__(self, question, choices, answer, number): #They all will have a question, choices, and answer
        self.question = question
        self.choices = list(choices)
        self.answer =  [ans.lower() for ans in answer]
        self.number = number
    def ask_question(self): #This will ask the questions so the user can respond accordingly
        #print(self.answer) # This is to debug
        print(f"Question: {self.number}")
        while True:
            print(self.question + "\n")
            for choice in self.choices: # this is going through each item in the list
                print(choice)
            answer_input = input().strip().lower() #We use lower and strip becasue of potential spaces and want to normalize
            if answer_input in self.answer: # this is also to check if the answer input is in the list of answers
                print('Next Question...')
                break
            else:
                print("**Please Try Again**")


q1 = Question(
    question="What is my name?",
    choices=["A. I don’t know", "B. I forgot", "C. You never told me"],
    answer=["C", "You never told me"],
    number = 1
)

q2 = Question(
     question="What is my name?",
     choices=["A. I don’t know", "B. I forgot", "C. You never told me"],
     answer=["A", "I don’t know"],
     number = 2
 )

q3 = Question(
     question="What is my name?",
     choices=["A. I don’t know", "B. What is your name?", "C. You never told me"],
     answer=["B", "What is your name?"],
     number = 3
 )

q4 = Question(
     question="What is my name?",
     choices=["A. What is my name, how are you?", "B. Oh okay", "C. You never told me"],
     answer=["A. What is my name, how are you?", "B. Oh okay", "C. You never told me", "A", "B", "C"],
    number = 4
 )

q1.ask_question()
q2.ask_question()
q3.ask_question()
q4.ask_question()


