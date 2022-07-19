print("Welcome to our translator!!")

keepgoing = True
while keepgoing:
  phrase = input('Enter phrase here: ')
  
  list = []
  for letter in phrase:
    try: # errror handling
      translation = int(phrase)
      translation = bin(translation)
      translation = translation.replace("b", "")
      list.append(translation)
      break
    except:
        translation = 0
        translation = int(translation) + ord(letter)
        translation = bin(translation)
        translation = translation.replace("b", "")
        list.append(translation)
  print(phrase, "in binary is", ' '.join(list))
  
  switch = True
  while switch:
    userchoice = input("Enter another phrase?").upper()
    if userchoice == "Y":
      keepgoing = True
      switch = False
    elif userchoice == "N":
      print("Thanks for using our translator.")
      keepgoing = False
      switch = True
    else:
      print("Try again (Y or N)")
      switch = True
      
