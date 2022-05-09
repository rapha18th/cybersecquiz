import random
import re
import os
import argparse

WIDTH = 1280
HEIGHT = 720

#message_box1 = Rect(0, 0, 395, 165)
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 395, 165)
answer_box2 = Rect(0, 0, 395, 165)
answer_box3 = Rect(0, 0, 395, 165)
answer_box4 = Rect(0, 0, 395, 165)
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
#message_box1.move_ip(470, 280)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 30

q1 = ["In which of the following, a person is constantly followed/chased by another person or group of several peoples?",
      "Phishing", "Bulling" ,"Stalking", "Identity theft", 3]
q2 = ["Which one of the following can be considered as the class of computer threats?",
      "Dos Attack", "Phishing", "Soliciting", "Both A and C", 1]
q3 = ["Which of the following is considered as the unsolicited commercial email?",
      "Virus", "Spam", "Malware", "All of the above", 2]
q4 = ["Which of the following usually observe each activity on the internet of the victim, gather all information in the background, and send it to someone else?",
      "Malware", "Spyware", "Adware", "All of the above", 2]
q5 = ["What is a software program or a hardware device that filters all data packets coming through the internet, a network?",
      "Antivirus", "Cookies", "Firewall", "Malware", 3]

q6 = ["Which of the following refers to stealing one's idea or invention of others and use it for their own benefits?",
      "Piracy", "Plaigarism", "Intellectual Property Rights", "All Of The Above", 1]
q7 = ["Which of the following refers to the violation of the principle if a computer is no more accessible?",
      "Access Control", "Confidentiality", "Avalaibility", "Both A and C", 3]
q8 = ["Which one of the following refers to the technique used for verifying the integrity of the message?",
      "Digital Signature", "Decryption algorithm", "Protocol", "Message Digest", 4]
q9 = ["Which one of the following usually used in the process of Wi-Fi-hacking?",
      "Aircrack-NG", "Wideshark", "McAfee", "None of the Above", 1]
q10 = ["Which of the following port and IP address scanner famous among the users?",
       "Cain and Abel", "Angry IP Scanner", "Snort", "Ettercap", 2]

q11 = ["In system hacking, which of the following is the most crucial activity?",
      "Information Gathering", "Gathering Facts", "Cracking Passwords", "None Of The Above", 3]
q12 = ["Which one of the following is actually considered as the first computer virus?",
      "Creeper", "Blaster", "Sasser", "Both A and C", 1]
q13 = ["To protect the computer system against the hacker and different kind of viruses, one must always keep _________ on in the computer system",
      "Antivirus", "Firewall", "Wifi", "Script", 2]
q14 = ["Which of the following can be considered as the elements of cyber security?",
      "Application Security", "Network Security", "Operation Security", "All Of the Above", 4]
q15 = ["Which of the following are famous and common cyber-attacks used by hackers to infiltrate the user's system?",
      "DDos and Derive-by downloads", "Phishing and Password attacks", "Malware and Malvertising", "All of the above", 4]

q16 = ["Which one of the following is also referred to as malicious software?",
       "Maliciousware", "Badware", "Ilegalware", "Malware", 4]
q17 = ["In Wi-Fi Security, which of the following protocol is more used?",
      "WPA", "WPA2", "WPS", "Both A and C", 2]
q18 = ["The term 'TCP/IP' stands for_____",
       "Transmission Contribution protocol/ internet protocol", "Transmission Control Protocol/ internet protocol", "Transaction Control protocol/ internet protocol", "Transmission Control Protocol/ internet protocol", 1]
q19 = ["Which of the following statements is correct about the firewall?",
       "It is a device installed at the boundary of a company to prevent unauthorized physical access", "It is a device installed at the boundary of an incorporate to protect it against the unauthorized access.", "It is a kind of wall built to prevent files form damaging the corporate.", "None Of Above", 2]
q20 = ["When was the first computer virus created?",
      "1970", "1971", "1962", "1980", 2]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16, q17, q18, q19, q20]
question = questions.pop(0)


def scramble(word):
    foo = list(word)
    random.shuffle(foo)
    return ''.join(foo)


def draw():


      screen.fill("dim grey")
      screen.draw.filled_rect(main_box, "sky blue")
      screen.draw.filled_rect(timer_box, "sky blue")
      #screen.draw.filled_rect(message_box1, "sky blue")
      for box in answer_boxes:
          screen.draw.filled_rect(box, "lavender")

      screen.draw.textbox(str(time_left), timer_box, color=("black"))
      screen.draw.textbox(question[0], main_box, color=("black"))

      index = 1
      for box in answer_boxes:
          screen.draw.textbox(question[index], box, color=("black"))
          index = index + 1

def game_over():
      global question, time_left
      message = "Game over. You got %s percent of questions correct" % str((score/20)*100)
      question = [message+". Run pgzrun cybersec.py to play again", "", "", "", "", 5]
      time_left = 0

def correct_answer():


      global question, score, time_left
      score = score + 1
      if questions:
          question = questions.pop(0)
          time_left = 30
      else:
          print("End of questions")

          game_over()

def wrong_answer():


      global question, score, time_left
      score = score
      if questions:
          question = questions.pop(0)
          time_left = 30
      else:
          print("End of questions")

          game_over()


def on_key_up(key):
      global score
      if key == keys.SPACE:
            score = score -1
            correct_answer()



def on_mouse_down(pos):


      index = 1
      for box in answer_boxes:
          if box.collidepoint(pos):
              print("Clicked on answer " + str(index))
              if index == question[5]:
                  print("You got it correct!")
                  correct_answer()
              else:
                  print("You got that one wrong!")
                  wrong_answer()

          index = index + 1

def update_time_left():


      global time_left
      if time_left:
          time_left = time_left - 1
      else:
          game_over()

clock.schedule_interval(update_time_left, 1.0)
