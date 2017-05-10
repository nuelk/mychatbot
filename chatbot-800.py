print('hello i am chatbot-1')                 #print welcome banner

print('mind if i ask you a few questions?')   #Enquire to learn

dict = ['what is your course of study?','goodbye','i am in love with of you','yup']

reply = input('>>>')                            #user_input

if reply == ('ok'):                           #first_loop

    print(dict[0])
else:
    print(dict[1])
    exit ()
  
reply = input('>>>')

if reply == ('statistics'):

      print('alright,what level')
else:
    print('ok so?')
reply = input('>>>')

dict = ["welcome first years","how's it going?","300lvled meat bags"]

if reply == ('100'):

   print(dict[0])
else:
    print(dict[1])
    exit ()
print('what is your favorite topic in statistics')

reply = input('>>>')

print('thank you for your time?')
