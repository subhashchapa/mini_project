# mini_project
basic quiz application
It contain the functionalities like adding the questions,attempting quiz,getting score,exit
1.ADDING QUESTIONS
  here we add questions through 2 modes
    1.through console
    2.through file
    through console:
      we take question as a input from a user in the form of string along with options and answer
      copy the string into file qbank.txt
    through file
      we ask the user to enter the name of the file which contain questions and append these questions to qbank.txt
2.attempting the quiz
    we can ask the user to how many questions he want to attempt and then using sample function from random package we generate that many questions from qbank.txt and ask the user to enter the answer for the question. for every correct answer we increment the values of score based on the marks assigned to that question and decrement the score for every wrong answer
3.GET THE SCORE
  just display the square variable
4.exit
  we can exit from application using exit function
