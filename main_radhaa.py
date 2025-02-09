from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import operator
import time
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import instaloader
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
# import cv2
import random
from requests import get
import wikipedia 
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import pywikihow
import psutil
import speedtest
from matplotlib import pyplot as plt
import pandas as pd
import pygame
import subprocess
import openai
import turtle
from tkinter import filedialog
from tkinter import *

# from twilio.rest import Client
# from AppOpener import open
# from AppOpener import close


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #voice of david
# engine.setProperty('voice',voices[1].id)  #voice of zira 
# engine.setProperty('voice',voices[2].id)  #voice of mark

# engine.setProperty('rate',180-200) # speech rate of karen or say words/min and default is 180 - 200

# print(voices)
# print(voices[0].id)   ----> prints david's voice 
# print(voices[1].id)   ----> prints zira's voice (Note :- You using this voice)
# print(voices[2].id)   ----> prints mark's voice

####################TO FIND OUT VOICES OF SYSTEM#####################

# for voice in voices:
#     print(voice.id)
#     engine.setProperty('voice',voice.id)
#     engine.say("Hello sir, I am your virtual assistant")
# engine.runAndWait()


#text to speech
def speak(audio):

    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1    # The pause_threshold value is the number of seconds the system will take to recognize the voice after the user has completed their sentence.
        audio = r.listen(source,timeout=None,phrase_time_limit=7) # timeout--> for how many seconds jarvis can be on hold to listen & phrase time limit --> no. of seconds user can speak on mic
        # By assigning None to argument 'timeout' it can listen endlessly so if you want that mic shoud listen first 5 seconds then assign "5" to timeout 
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    
    hour = int(datetime.datetime.now().hour)
    currentTime = datetime.datetime.now().strftime("%I:%M:%S")  # .strftime("%H:%M:%S")-->gives 24 hour format ; for 12 hour format replace %H with %I

    if hour>=0 and hour<12:
        speak(f"Good Morning Anurag")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Anurag")

    else:
        speak(f"Good Evening Anurag")

    speak("I am Karen, how may I help you ")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anuragyamnurwar2003@gmail.com','anurag@123')
    server.sendmail('anuragyamnurwar2003@gmail.com',to,content)
    server.close()

# pdf reader
def pdf_reader():
    # os.startfile("C:\\Users\\DELL\\Downloads\\100PythonPracticeProblems.pdf")
    book = "C:\\Users\\DELL\\Desktop\\Jarvis\\eit.pdf"
    pdfReader = PyPDF2.PdfReader(book) #pip install pyPDF2
    pages = len(pdfReader.pages)
    speak(f"Total number of pages in this PDF is:{pages}")
    speak("Sir, please enter the page number you have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.pages[pg]
    text = page.extract_text()
    speak(text)

def search_wikihow(query, max_results=10,lang="en"):
    return list(pywikihow.search(query,max_results,lang))

def kbcgame():

    

    print("WELCOME TO KAUN BANEGA CROREPATI...LET'S PLAY")
    print("Hello", input("Enter Your Name:"))

    # total prize for each question 
    amount_won = [1000, 2000, 3000, 5000, 10000,
                20000, 40000, 80000, 160000,
                320000, 640000, 1250000, 2500000,
                5000000, 10000000, 70000000]
    # Options for 50:50 lifeline
    op1 = ['	 ', '	 ', ' ', 'Srinagar',
        '	 ', 'Cricket', '1920', '	 ', ' ',
        '	 ', ' ', 'Cricket', '	 ',
        'Kolkata', 'Wrestling', '		 ', '	 ',
        '	 ', 'China', 'Thar', '		 ', '	 ',
        'Israel', '	 ', '		 ', 'Arjan Singh',
        'Parliament of India', '	 ', '	 ',
        'Mohd Hamid Ansari ', ' ', 'Mahatma Gandhi',
        'Hanuman']

    op2 = ['AB De Villiers', '	 ', '9', '	 ',
        '	 ', ' ', '1928', '	 ', 'Cricket',
        'Yuvraj Singh', 'Cricket', 'Football', 'West Indies',
        'Mumbai', 'Swimming', '			 ', '	 ',
        '	 ', '	 ', 'Sahara', 'Mahishmati', '	 ',
        'Jordan', '	 ', 'Che Guevera', '			 ',
        '	 ', '	 ', '	 ', '	 ', ' ', ' ',
        '			 ']

    op3 = ['Shahid Afridi', 'Dishonest', ' ', 'Amritsar',
        'Sindhi', '	 ', ' ', 'Pakistan', '	 ',
        'MS Dhoni', ' ', '	 ', 'South Africa', ' ',
        '	 ', 'Henry Becquarrel', 'Tephrosia', 'Dermatitis',
        'Japan', ' ', '	 ', 'Bypass', '		 ',
        'Mridangam', '		 ', '			 ', '	 ',
        'darjeeling', 'Japanese Encephalitis ', 'Mohd Hidayatullah ',
        'Saina Nehwal', '	 ', 'Shiva']

    op4 = ['	 ', 'Miserly', '8', '	 ', 'English', 'Hockey',
        '	 ', 'Australia', 'Football', '	 ', 'Polo', '	 ',
        '	 ', '	 ', '	 ', 'None of these', 'Indigofera',
        'Cholera', '	 ', '	 ', 'Badami', 'Debridement',
        '	 ', 'Dafli', 'Vladimir Lenin', 'Aspy Engineer',
        'Mangalyaan', 'Kohima', 'Plague', '	 ', 'Jwala Gutta',
        'Mother Teresa', ' ']

    op = [op1, op2, op3, op4]

    # list of lifelines
    list_life = [1, 2, 3, 4]

    def lifeline(ran, opts, op):

        m = 1

        lifelines = ['Audience Poll', 'Fifty Fifty',
                    'Double dip', 'Flip the question']
        
        print(f"Lifelines are:\t{lifelines[0]},{lifelines[1]},{lifelines[2]},{lifelines[3]}\n")
        
        if list_life == []:
            print("You don't have lifelines remaining\t")
            return None
        
        print("Press 1 for audience,2 for 50:50, 3 for double dip or 4 for flip the question\t")

        while(m != 0):
            get = int(input())
            
            if get == 1:
                if get in list_life:
                    m = 0
                    list_life.remove(1)
                    great = audience(ran, opts)

                else:
                    print("You don't have audience poll\t")
            
            elif get == 2:
                if get in list_life:
                    m = 0
                    great = fifty(ran, op)
                    list_life.remove(2)

                else:
                    print("You don't have 50:50 \t")
            
            elif get == 3:
                if get in list_life:
                    m = 0
                    great = doubleDip(ran)
                    list_life.remove(3)
                else:
                    print("You don't have double dip\t")
            
            elif get == 4:
                if get in list_life:
                    m = 0
                    great = flip()
                    list_life.remove(4)
                else:
                    print("You don't have lifeline to flip the question\t")
            
            else:
                print("Choose correct option")

        return great


    def audience(ran, opts):

        # graphical audience poll using pandas
        print("According to audience\n")

        s = pd.Series([opt1[ran], opt2[ran], opt3[ran], opt4[ran]],
                    index=['1', '2', '3', '4'])

        s.plot.bar(figsize=(20, 10))
        plt.xlabel('Options')
        plt.ylabel('%')
        plt.title("Audience Poll")
        plt.show()

        print('1.', opts[0][ran], "%", '\t', '2.',
            opts[1][ran], "%", '\t', '3.', opts[2][ran],
            "%", '\t', '4.', opts[3][ran], "%", '\enter your choice\t')
        
        print("Would you like to take lifeline again,if yes then press 9 or Press 0 to Quit\t")
        
        choice = int(input())
        
        if choice == 9:
            great = lifeline(ran, opts, op)
            return great
        
        elif choice == answer[ran]:
            great = 1
            print("Correct answer,well done!..")
        
        elif choice == 0:
            great = -2
        
        else:
            great = 0
            print("Incorrect")
            print("Correct Answer is :", options[answer[ran]-1][ran])

        return great


    def fifty(ran, op):

        print("Q."+questions[ran])
        
        for num, option in enumerate(op):
            print(str(num+1)+"."+option[ran])
        choice_fifty = int(input("enter your choice \t"))

        if choice_fifty == answer[ran]:
            print("Correct Answer.....")
            great = 1
        
        else:
            great = 0
            print("wrong answer")
            print("Correct Answer is :", options[answer[ran]-1][ran])
        
        return great


    def doubleDip(ran):
        
        # double dip gives 2 chances
        print("Select two options\n")
        trial1 = int(input())
        
        if answer[ran] == trial1:
            great = 1
            print("Correct Answer,well done....")
        
        else:
            print("Your first trial is wrong, choose another\t")
            trial2 = int(input())
            
            if answer[ran] == trial2:
                great = 1
                print("Correct Answer\t")
            
            else:
                print("Your second trial is also wrong..Better luck next time..\t")
                print("Correct Answer is :", options[answer[ran]-1][ran])
                great = 0
        
        return great


    def flip():
        return -1

    def amount(correct_ans):
        print(amount_won[correct_ans-1])
        
        if amount_won[correct_ans-1] == 10000:
            print("Completed 1st stage")
        
        elif amount_won[correct_ans-1] == 320000:
            print("Completed 2st stage")
        
        elif amount_won[correct_ans-1] == 70000000:
            print("You have won Rs 7 CRORE")
        
        return amount_won[correct_ans-1]


    questions = [
    'In ODI Cricket, who created the record of scoring the \
    fastest century in just 31 balls ?',
    ' If you call someone ‘Makkhichoos’ then what are you \
    calling him ?',
    'How many players of a Kho-Kho team can play on the field\
    during the match ?',
    'Which of these Indian cities is closest to the Pakistani \
    city of Lahore ?',
    'The language spoken by the people by Pakistan is ?',
    'The term“Googly” is associated with ?',
    'India first took part in the olympic games in the year ?',
    'Who are Kangaroos ?',
    'Oval stadium in England is associated with ?',
    'In 2011 India won the World Cup. Who was adjudicated as the\
    man of the series in the tournament ? ',
    'Eden Gardens in Kolkata is ----- stadium.? ',
    'Ronaldo is associated with ? ',
    'Icc’s 2007, the World Cup Cricket was held in ? ',
    'Wankhede Stadium is at ? ',
    'World’s most ancient game is ? ',
    'Stethoscope was invented by ?',
    'A dye is prepared from ',
    'Which disease is caused by the fungi? ',
    'Which is the Land of the Rising Sun? ',
    'The desert that lies on the boundary between India and Pakistan \
    is ',
    ' In which kingdom is the story of the ‘Bahubali’ series of films\
    mainly set?',
    'What is the common name for surgery conducted on coronary arteries\
    that supply blood to the heart ?',
    ' In July 2017, Narendra Modi Become the first Indian Prime Minister\
    to visit which country ?',
    'Which of these musical instrument is held in one hand and played with\
    the other ?',
    ' On the last day of his life Bhagat Singh was reading a book about\
    the Ideology of which revolutionary ?',
    'Which Air force officer had the unique honour of leading the fly-post\
    over the Red fort in Delhi on 15 August 1947 ?',
    'Which image appears on the flip side of the new 2000 Rs Note, launched\
    in 2016?',
    'Which Indian hill station gets its name from the Tibetan words that mean\
    ‘land of the thunderbolt’?',
    'Which of these diseases is transmitted by mosquitoes?',
    'Who among these has served as the Ambassador of India to the United Nations?',
    ' Who was the first Indian to win the World Junior Badminton Championships?',
    'Which of the following is a recipient of the Nobel Peace Prize?',
    'The cave temples at the historical site of Elephanta are dedicated to which\
    God?'
    ]

    option1 = ['Corey Anderson', 'Evil', '10', 'Srinagar', 'Hindi',
            'Cricket', '1920', 'Bangladesh', 'polo', 'Virat Kohli',
            'Tennis', 'Cricket', 'Australia', 'Kolkata', 'Wrestling',
            'Bessemer', 'Sida', 'Polio', 'China', 'Thar', 'Magadh',
            'Cataract', 'Israel', 'Tabla', 'Antonio Gramsci ',
            'Arjan Singh', 'Parliament of India', 'Gangtok', 'Rabies',
            ' Mohd Hamid Ansari', 'P V Sindhu', 'Mahatma Gandhi', 'Hanuman']

    option2 = ['AB De Villiers', 'Humble', '9', 'Jaisalmer', 'Palauan',
            'Football', '1928', 'Kenya', 'Cricket', 'Yuvraj Singh',
            'Cricket', 'Football', 'West Indies', 'Mumbai', 'Swimming',
            'Rane Laennec', 'Tridax', 'Malaria', 'Taiwan', 'Sahara',
            'Mahishmati', 'Gastric', 'Jordan', 'Santoor', 'Che Guevera',
            'Pratap Chandra Lal', 'Tractor', 'Aizawl', 'Tetanus', ' I K Gujral',
            'Aparna Balan', 'Swami Vivekananda ', 'Vishnu']

    option3 = ['Shahid Afridi', 'Dishonest', '7', 'Amritsar', 'Sindhi',
            'Badminton', '1972', 'Pakistan', 'Hockey', 'MS Dhoni',
            'Hockey', 'Hockey', 'South Africa', 'Delhi', 'Boxing',
            'Henry Becquarrel', 'Tephrosia', 'Dermatitis', 'Japan',
            'Gobi', 'Kalinga', 'Bypass', 'Saudi Arabia', 'Mridangam',
            ' Leon Trotsky ', 'Subroto Mukarjee', 'Red Fort', 'darjeeling',
            'Japanese Encephalitis', 'Mohd Hidayatullah ', 'Saina Nehwal',
            'Rabindranath Tagore ', 'Shiva']

    option4 = ['Rohit Sharma', 'Miserly', '8', 'Udhampur', 'English', 'Hockey',
            '1976', 'Australia', 'Football', 'Zaheer Khan', 'Polo', 'Tennis',
            'India', 'Jaipur', 'Running', 'None of these', 'Indigofera',
            'Cholera', 'Australia', 'None of these', 'Badami', 'Debridement',
            'Qatar', 'Dafli', 'Vladimir Lenin', 'Aspy Engineer', 'Mangalyaan',
            'Kohima', 'Plague', 'Zakir Hussain', 'Jwala Gutta', 'Mother Teresa',
            'Kamadeva']

    options = [option1, option2, option3, option4]

    # answer key
    answer = [2, 4, 2, 3, 3, 1, 1, 4, 2, 2, 2, 2, 2, 2, 1,
            3, 4, 3, 3, 1, 2, 3, 1, 4, 4, 1, 4, 3, 3, 1,
            3, 4, 3]

    wrong = False

    # correct variable for total correct answer
    correct = 0
    total_amt = 0

    # option list for audience poll
    opt1 = [30, 24, 10, 0, 1, 72, 99, 0, 9, 2, 0, 2, 10, 1,
            100, 1, 0, 3, 2, 98, 21, 35, 50, 40, 45, 65, 50,
            48, 5, 70, 20, 30, 20]

    opt2 = [60, 32, 80, 0, 2, 5, 1, 1, 91, 94, 95, 87, 90, 96,
            0, 0, 2, 12, 13, 1, 60, 20, 30, 2, 0, 20, 0, 1, 10,
            12, 20, 20, 10]

    opt3 = [2, 4, 0, 100, 97, 0, 0, 1, 0, 2, 5, 11, 0, 3, 0, 99,
            2, 82, 82, 0, 18, 40, 10, 4, 1, 10, 0, 50, 70, 15,
            35, 10, 64]

    opt4 = [8, 40, 10, 0, 0, 23, 0, 98, 0, 2, 0, 0, 0, 0, 0, 0,
            96, 3, 3, 1, 1, 5, 10, 54, 54, 5, 50, 1, 15, 3, 25,
            40, 6]

    opts = [opt1, opt2, opt3, opt4]

    condition, ques_no = 1, 0

    while(wrong != True):
        ques_no += 1
        ran = random.randint(0, len(questions)-1)
        print("\n\nQ.", ques_no, ":-", end="")
        print(questions[ran])
        
        for num, option in enumerate(options):
            print(str(num+1)+"."+option[ran])

        print("Would you like to take lifeline, if yes, press 9\nChoose any option: or you can quit by pressing 0 \t\t")
        
        give_answer = int(input())
        
        if give_answer == 9:
        
            # condition variable is to count lifelines used
            if condition <= 4:
                condition += 1
                great = lifeline(ran, opts, op)
                
                if great == 0:
                    if total_amt < 10000:
                        total_amt = 0
                    elif total_amt < 320000:
                        total_amt = 10000
                    elif total_amt < 70000000:
                        total_amt = 320000
                    break
                
                elif great == -1:
                    ques_no -= 1
                    pass

                elif great == None:
                    print("Choose any option or press 0 to quit\t")
                    give_ansr = int(input())
                    if answer[ran] == give_ansr:
                        print("Correct answer, great")
                        correct += 1
                
                elif great == -2:
                    break
                
                else:
                    correct += 1
                    print("You have won Rs=", end="")
                    total_amt = amount(correct)
            
            else:
                print(
                    "You have used your all lifelines\t\n Choose any option: \
                    or you can quit by pressing 0\t\t")
                give_ans = int(input())
                key = answer[ran]
                
                if give_ans == 0:
                    total_amt = amount(correct)
                    break
                
                elif key == give_ans:
                    print("Correct, You have won Rs. =", end="")
                    correct += 1
                    total_amt = amount(correct)
                
                else:
                    print("Wrong Answer....")
                    print("Correct Answer is : ", options[answer[ran]-1][ran])
                    if total_amt < 10000:
                        total_amt = 0
                    elif total_amt < 320000:
                        total_amt = 10000
                    elif total_amt < 70000000:
                        total_amt = 32000
                    wrong = True

        else:
            key = answer[ran]
            
            if give_answer == 0:
                if correct != 0:
                    total_amt = amount(correct)
                break
            
            elif key == give_answer:
                print("Correct answer.., You have won Rs.=", end="")
                correct += 1
                total_amt = amount(correct)
            
            else:
                print("Wrong Answer...Better luck next time...")
                print("Correct Answer is :", options[answer[ran]-1][ran])
                if total_amt < 10000:
                    total_amt = 0
                elif total_amt < 320000:
                    total_amt = 10000
                elif total_amt < 70000000:
                    total_amt = 320000
                wrong = True
        
        if correct == 16: # total questions are 16
            break
            
        # delete previous question and its options from list
        del questions[ran]
        del option1[ran]
        del option2[ran]
        del option3[ran]
        del option4[ran]
        del answer[ran]
        del opts[0][ran]
        del opts[1][ran]
        del opts[2][ran]
        del opts[3][ran]
        del op[0][ran]
        del op[1][ran]
        del op[2][ran]
        del op[3][ran]
        options = [option1, option2, option3, option4]
        
    print("Your winning amount is Rs. ", total_amt)



def love_percentage_calculator():

    def love_percentage(boy_name, girl_name):
        boy_name = boy_name.lower()
        girl_name = girl_name.lower()
        total_letters = len(set(boy_name + girl_name))
        num_matches = 0
        for letter in set(boy_name):
            if letter in girl_name:
                num_matches += 1
        love_percent = round((num_matches / total_letters) * 100)
        return love_percent

    boy_name = input("Enter the name of the boy: ")
    girl_name = input("Enter the name of the girl: ")

    print("Love percentage: ", love_percentage(boy_name, girl_name), "%")

def random_1():
    def should_do_task():
        """Generate a random "yes" or "no" response."""
        response = random.choice(["Yes", "No"])
        return response
    speak("Enter the task or work you want to find whether you should do or not")
    task = input("Should I do this task? (yes or no): ")
    print("According to Jarvis:",should_do_task())

def myintro():
    

    speak("Anurag Anil Yamnurwar At Post Dhaba Ta. Gondpipari Dis.Chandrapur.")
    speak("Sir, I have also found a rap written by Anurag ; can I open it")
    ask = takecommand().lower()
    if "open" in ask or "yes" in ask:
        print('''
Verse 1:
Listen up, y'all, let me introduce
A young man with a drive to produce
His name is Anurag, born in '03
From Dhaba town, a place to be

Got his fam by his side, Anil and Ashwini
Sis Prachi too, yeah, they all got that hanga
School at Janta Vidhyalaya Dhaba Ljk Gp, never lost a beat
''')

    elif "no" in ask :
        speak("Okay")

def chatgpt():
    import openai
    import time

    # Set up OpenAI API credentials
    openai.api_key = "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"

    # Define a function to generate responses using the GPT-3 model
    def generate_response(prompt):
        # Set up the request parameters
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the response from the API result
        message = completions.choices[0].text.strip()
        return message

    # Define a function to handle user queries and generate responses
    def respond(query):
        # Generate a prompt using the user query
        prompt = f"User: {query}\nChanakya:"

        # Generate a response using the GPT-3 model
        response = generate_response(prompt)

        # Print the response and wait for a short period of time
        speak(f"Chanakya: {response}\n")
        time.sleep(1)

    # Define a function to get user input from the command line
    def get_input():
        return input("User: ")

    # Loop to continuously get user input and generate responses
    while True:
        speak("To exit from the GPT Mode; enter exit\nOr if you want to generate an AI image; enter image\n")  #This command asks user first to provide voice input
        query = get_input() #We can change from text input to voice input by replacing get_input() to takecommand().lower()
        if query == "exit":
            break
        elif query =="image":
            dall_e()
        else:
            respond(query)
         
def dall_e():

    openai.api_key = "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"
    openai.Model.list()

    res = openai.Image.create(
        
        prompt = input("What you want to generate:"),
        n = int(input("How many images you would like to generate:")),
        size = "512x512"
    )

    if __name__ == "__main__":
    
        print(res)
        speak("Sir,images has been generated")

def heart():

    wn = turtle.Screen()
    wn.setup(width=400, height=400)
    red = turtle.Turtle() # Assigning "Red" as name of the turtle

    def curve(): # Method to draw curve
        for i in range(200): # To draw the curve step by step
            red.right(1)
            red.forward(1)

    def heart():  # Method to draw full Heart
        red.fillcolor('red')
        red.begin_fill()
        red.left(140)
        red.forward(113)
        curve() # Left Curve
        red.left(120)
        curve() # Right Curve
        red.forward(112)
        red.end_fill()

    heart()
    red.ht() # Hiding Turtle
    turtle.done()

def mergePDF():
        
    # Get the number of PDFs to merge from the user
    num_pdfs = int(input("Enter the number of PDFs to merge: "))

    # Create a PDF Merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Loop through the number of PDFs and add them to the merger
    for i in range(num_pdfs):
        pdf_name = input(f"Enter the file name of PDF {i+1}: ")
        pdf_merger.append(pdf_name)

    # Ask the user for the output file name
    output_name = input("Enter the output file name: ")

    # Write the merged PDF to the output file
    with open(output_name, "wb") as f:
        pdf_merger.write(f)


    print("PDFs have been merged")

def folderpdfmerge():

    # Open a dialog box to allow user to select a directory
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    # Initialize a PDF file writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through all PDF files in the selected directory and merge them
    for filename in os.listdir(folder_selected):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_selected, filename)
            pdf_reader = PyPDF2.PdfReader(file_path)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    # Save the merged PDF file in the selected directory with a name of your choice
    output_filename = input("Enter the name for the merged PDF file: ")
    output_file_path = os.path.join(folder_selected, output_filename + ".pdf")
    with open(output_file_path, "wb") as output_file:
        pdf_writer.write(output_file)

def pdfEncryption():

    # ENCRYPTION OF PDF
    fn = input("Enter the filename of PDF you want to encrypt:")
    reader = PdfReader(fn)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:    
        writer.add_page(page)

    # Add a password to the new PDF
    password = input("Enter the encryption password for file:")
    writer.encrypt(password)

    # Save the new PDF to a file
    newFile = input("Enter the new filename of PDF:")
    with open(newFile, "wb") as f:
        writer.write(f)

def calculator():
    speak("Sir, what you want to calculate; example 20 multiply 6")
    math = str(takecommand().lower())#input("Enter querry:")
    ans = eval(math)
    speak(f"Sir, your answer is:{ans}")

def TaskExecution():

    wish()
    while True:
    # if 1:

        query = takecommand().lower()

        #commands for system apps

        if "open notepad" in query:
            speak("Opening notepad...")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath) 

        # elif "open camera" in query:
        #     speak("Opening Camera...")
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret , img = cap.read()
        #         cv2.imshow('webcam',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break;
        #     cap.release()
        #     cv2.destroyAllWindows()

        
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 5:
                music_dir = 'C:\\Users\\DELL\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

        elif "open command prompt" in query:
            speak("Opening Command Prompt...")
            os.system("start cmd")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code...")
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open intelligent' in query:
            speak("Opening IntelliJ Idea...")
            intePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.2.1\\bin\\idea64.exe"
            os.startfile(intePath)

        elif "show morris image" in query or "open morris image" in query:
            speak("Opening Virat's Image...")
            img_path = "C:\\Users\\DELL\\Downloads\\Morris"
            img = os.listdir(img_path)
            rd = random.choice(img)
            os.startfile(os.path.join(img_path,rd))

        elif "play music" in query:
            speak("Playing Music...")
            music_dir = "C:\\Users\\DELL\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
 
        elif "play legends of hanuman" in query:
            speak("Playing the legends of hanuman...")
            loh_dir = "D:\\Movies\\The legends of hanuman"
            vid = os.listdir(loh_dir)
            rd = random.choice(vid)
            os.startfile(os.path.join(loh_dir,rd))

        elif "play what if" in query:
            speak("Playing Marvel's What If...")
            wif_dir = "D:\\Movies\\What......If(Hindi)"
            vid = os.listdir(wif_dir)
            rd = random.choice(vid)
            os.startfile(os.path.join(wif_dir,rd))

        elif "switch the window" in query or "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
        
        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "volume unmute" in query or "unmute" in query:
            pyautogui.press("volumemute")

        elif "open whatsapp" in query or "whatsapp" in query:
            speak("Opening Whatsapp...")
            waPath = 'C:\\Users\\DELL\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            subprocess.Popen(waPath)


        # Server Applications Commands

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open("www.youtube.com")

        elif "search on youtube" in query:
            speak("Opening YouTube...")
            speak("Sir, what should I search on Youtube..")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "open facebook" in query:
            speak("Opening FaceBook...")
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            speak("Opening instagram...")
            webbrowser.open("www.instagram.com")

        elif "open stack overflow" in query:
            speak("Opening Stack Over Flow...")
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Opening Google...")
            speak("Sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open chrome" in query:
            speak("Opening Google Chrome...")
            webbrowser.open("www.google.com")

        elif "open mail" in query:
            speak("Opening G-mail...")
            webbrowser.open("https://mail.google.com/mail/u/0/")

        elif "open classroom" in query:
            speak("Opening Google Classroom...")
            webbrowser.open("https://classroom.google.com")

        elif "open lit" in query:
            speak("Opening Repl it..")
            webbrowser.open("www.replit.com")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            # print(results)

        elif "send message" in query:
            try:

                kit.sendwhatmsg("+918459210519", "hello anurag this is a testing message for python module pywhatkit",16,51, tab_close=True)
                speak("Message has been sent successfully")
            except Exception as e:
                speak(f"Sorry, some error occured , {e}")

        elif "play song on youtube" in query:
            speak("Sir, which song you would like to listen!")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "send email" in query:

            speak("Sir, what should I say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'anuraganilyamnurwar@gmail.com' #your email
                password = 'anurag@123aniL'
                send_to_email = 'anilkeshavyamnurwar@gmail.com'
                speak("Okay, what is the subject for this email")
                query = takecommand().lower()
                subject = query #subject in the email
                speak("and Sir, what is the message for this email")
                querry2 = takecommand().lower()
                message = querry2 # message in the email
                speak("Sir , please enter thr correct path of the file into the shell")
                file_location = input("Please enter the path here")

                speak("Please wait,I am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['subject'] = subject

                msg.attach(MIMEText(message,'plain'))


                #setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location,"rb")
                part = MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename = %s" % filename)


                # Attach the attachment to the MIMEMulipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmailcom',587)
                server.starttls()
                server.login(email,password)
                text = msg.as_string()
                server.sendmail(email,send_to_email,text)
                server.quit()
                speak("Email has been sent to Anurag")

            else:
                email = 'anuraganilyamnurwar@gmail.com' # your email
                password = 'anurag@123aniL' #your email account password
                send_to_email = 'anilkeshavyamnurwar@gmail.com'
                message = query # The message in the email

                server = smtplib.SMTP('smtp.gmail.com',587) #Connect to the server
                server.starttls() # Use TLS
                server.login(email,password) #Login to the email server
                server.sendmail(email,send_to_email,message)
                server.quit() #logout of the email server
                speak("Email has been sent to Anurag")

        elif "temperature" in query or "weather" in query:

            speak("Which city's temperature you want to find, sir")
            search = takecommand().lower()
            # search = f"temperature in {cm}"
            url = f"https://www.google.com/search?q=temperature in {search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current temperature in {search} is: {temp}")

        elif "activate how to do mode" in query:

            speak("How to do mode is activated!")
            while True:
                speak("Please tell me what you want to know")
                how = takecommand()
                try:
                    if "deactivate" in how or "close" in how:
                        speak("Okay sir, how to do mode is closed")
                        break
                    else:
                
                        max_results = 1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                
                except Exception as e:
                    speak("Sorry sir, I am not able to find this")


        #     speak("Please wait sir,fetching the latest news")
        #     news()

        #Commands to close system apps
        
        elif "close notepad" in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query:
            speak("Closing Command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif "close code" in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im Code.exe")

        elif "close intellient" in query:
            speak("Closing IntelliJ Idea")
            os.system("taskkill /f /im idea64.exe")

        elif "close chrome" in query:
            speak("Closing Google Chrome...")
            os.system("taskkill /f /im chrome.exe")

                 # To find my location using IP Address
        
        #location detector
        elif "where we are" in query:
            speak("Wait Sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'  #202.43.120.228
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir I am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry Sir, due to network issue I am not able to find where we are...")
                pass


                # To check a instagram profile

        #Instagram profile checker
        elif "instagram profile" in query or "profile on instagram" in query:

            speak("Sir, please enter the user name correctly!")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir, here is the profile of the user {name}")
            time.sleep(5)
            speak("Sir, would you like to download profile picture of this account!")
            condition = takecommand().lower()
            if "yes" in condition or "course" in condition:
                mod = instaloader.Instaloader() # pip install instaloader
                mod.download_profile(name,profile_pic=True)
                speak("I am done sir, profile picture is saved in our main folder; now I am ready for next command")
            else:
                pass   

        # take screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("Please Sir hold the screen for few seconds , I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is saved in our main folder and now I am ready for next command!")

        # To read pdf
        elif "read" in query:
            pdf_reader()

        #Check internet speed
        elif "internet speed" in query:

            st = speedtest.Speedtest()
            dl = st.download() #downloading speed in bits
            ul = st.upload()   #uploading speed in bits
            dlmb = dl/8000000  # downloading speed in mb 
            ulmb = ul/8000000  # uploading speed in mb
            speak(f"Sir, we have {dlmb} MB per second downloading speed and {ulmb} MB per second uploading speed")

        #Mathematical calculations using voice command
        # elif "do some calculations" in query or "can you calculate" in query:
        #     try:
        #         r = sr.Recognizer()
        #         with sr.Microphone() as source:
        #             speak("Say what you want to calculate, example 3 plus 3")
        #             print("listening...")
        #             r.adjust_for_ambient_noise(source)
        #             audio = r.listen(source)
        #         my_string = r.recognize_google(audio)
        #         print(my_string)
        #         def get_operator_fn(op):
        #             return{
        #                 '+' : operator.add, 
        #                 '-' : operator.sub,
        #                 'x' : operator.mul,
        #                 'divided' : operator.__truediv__,
        #             }[op]
        #         def eval_binary_expr(op1, oper, op2):
        #             op1,op2 = int(op1), int(op2)
        #             return get_operator_fn(oper)(op1, op2)
        #         speak("Your result is:")
        #         speak(eval_binary_expr(*(my_string.split())))

        #     except Exception as e:
        #         speak("Sorry, I didn't get that please say that again")

        elif "calculate" in query:
            calculator()

         #Commands for system functions
  
        #inbuilt system commands
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 30")

        elif "restart the system " in query:
            os.system("shutdown /r /t 30")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        #greetings commands
        elif "hello" in query or "hey" in query:
            speak("Hello Sir, may I help you with something!")

        elif "how are you" in query:
            speak("I am fine sir, what about you!")

        elif "also good" in query or "fine" in query:
            speak("Thats's great to hear from you!")

        # elif "thank you" in query or "thanks" in query:
        #     speak("It's my pleasure sir!")

        #My python projects 
        elif "open my project" in query or "open my projects" in query:
            speak("Sir, which project you would like to open;\n1.KBC Game\n2.Holi Project\n3.Love percentage Calculator\n4.Certainty\n5.My Heart\n6.My Webpage\n7.Jarvis Voice Conversation Automation\n8.Image Generator\n9.Merge PDF")
            print("To exit; say exit or close my projects")
            while True:
                options = takecommand().lower()

                if "kbc game" in options or "first project" in options or "1st project" in options:
                    speak("Opening Kaun Banega Crorepati Game...")
                    kbcgame()

                # elif "holi project" in options or "second project" in options or "2nd project" in options:
                #     speak("Opening Holi project...")
                #     holi()

                elif "love percentage calculator" in options or "third project" in options or "3rd project" in options:
                    speak("Opening Love Percentage Calculator...")
                    love_percentage_calculator()

                elif "certainty" in options or "fourth project" in options or "4th project" in options:
                    speak("Opening Should I do the task...")
                    random_1()

                elif "my heart" in options or "fifth project" in options or "5th project" in options:
                    speak("Showing your heart...")
                    heart()

                elif "my web page" in options or "sixth project" in options or "6th project" in options:
                    speak("Opening Anurag's Webpage...")
                    wpPath = "C:\\Users\\DELL\\Desktop\\anurag.html"
                    os.startfile(wpPath)

                elif " GPT voice automation" in options or "seventh project" in options or "7th project" in options :
                    speak("Activating Jarvis Conversational automation!...")
                    chatgpt()

                elif "image generator" in options or "eight project" in options or "8th project" in options:
                    speak("Sir , enter which type of image you want generate")
                    dall_e()

                elif "merge" in options or "Merge PDF" in options or "9th project" in options:
                    speak("Sir, how would you like to merge PDFs:\n1.Entire Folder's PDF\n2.By selecting specific PDFs")
                    pdf_ask = input("Enter (1) or (2) to proceed with respective methods: ")

                    if "1" in pdf_ask:
                        folderpdfmerge()
                        speak("Sir, PDFs have been merged!")
                    
                    elif "2" in pdf_ask:
                        speak("Sir, please enter the number of PDFs you want to merge followed by filename of PDFs:")
                        mergePDF()
                        speak("Sir, PDFs have been merged!")
                        speak("Sir, would you like to encrypt the PDF file:(Yes or No)")
                        encry = input("Enter (Yes/NO):")
                        if encry == "Yes" or encry == "yes":
                            speak("Sir, please enter the filename of PDF you want to encrypt and make sure that file should reside within this folder")
                            pdfEncryption()
                            speak("Sir, PDF has been encrypted with new file...")
                
                elif "exit" in options or "close" in options:
                    speak("Projects Section has been closed")
                    break

        elif "sleep" in query or "jarvis sleep" in query or "sleep jarvis" in query or "slip" in query:
            speak("Okay sir, I am going for a nap ;just say wake up to call me")
            while True:
                print("Say mute for silence and unmute to listen me")
                wake = takecommand().lower()
                if "wake up" in wake or "wake" in wake:
                    speak("Hello sir, I am back in the system")
                    break

                elif "jarvis mute" in wake or "mute" in wake:
                    pyautogui.press("volumemute")

                elif "jarvis unmute" in wake or "unmute" in wake:
                    pyautogui.press("volumemute")


        # #My introduction
        # elif "who is anurag yamnurwar" in query or "anurag yamnurwar" in query:
        #     speak("Searching....")
        #     time.sleep(1)
        #     myintro()


        # # Completion or termination command
        elif "no thanks" in query or "leave" in query or "bye" in query or "by" in query:
            speak("Thanks for using me, have a good day.")                 
            sys.exit()

        else:
            speak("Sorry, I didn't get it...")

        time.sleep(2)
        # speak("Would you like to accomplish any other tasks, sir")

#simple command for Karen that will start once the run command executed and exit after second

if __name__ == "__main__":
    TaskExecution()
