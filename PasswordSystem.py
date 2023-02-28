# !!!! This Project is protected under the MIT license !!!!
# !!!! Charlie Ward 2023 !!!!

# Importing Sleep Function
import time

# Setting Up the Default Accounts
baseUsernames = ["Default", "Admin"]
basePasswords = ["Default", "Admin"]

# Setting up the clear variable
clear = "\n" * 100

# Setting the loop to activate
mainLoop = True

# Clearing the console
print(clear)

while mainLoop == True:
    # Setting variables to be correct
    leaveLoop = False
    LogInDone = False
    confirmed = False
    finishedReg = False
    while leaveLoop == False:
        print("MAIN MENU")
        print("Please choose from the options below")
        print("[0] Login [1] Register [2] Shut Down")
        mainMenuChoice = input("")
        if mainMenuChoice == "0":
            print(clear)
            print("Please enter your username")
            inUsername = input("")
            # Checking if username entered is in the username array
            if inUsername in baseUsernames:
                print("Username Correct")
                time.sleep(1)
                print(clear)
                location = baseUsernames.index(inUsername)
                print("Please enter your password")
                inPassword = input("")
                # Checking if the password is correct for the username
                if inPassword == basePasswords[location]:
                    print("Password Correct")
                    time.sleep(1)
                    print(clear)
                    print("Login Success")
                    time.sleep(1)
                    print(clear)
                    LogInDone = True
                    leaveLoop = True
                else:
                    print("Password Incorrect")
                    time.sleep(1)
                    print(clear)
            else:
                print("Username Incorrect")
                time.sleep(1)
                print(clear)
        elif mainMenuChoice == "1":
            print("Hello and Welcome to register please fill out the form below")
            time.sleep(1)
            print(clear)
            while finishedReg == False:
                print("Please enter a username")
                regUsername = input("")
                print(clear)

                print("Please enter a password")
                regPassword = input("")
                print(clear)

                print("Please confirm password")
                regPasswordConfirm = input("")
                print(clear)

                # Checking if password is the same
                if regPassword != regPasswordConfirm:
                    print("Password not the same")
                    print("Restarting the process")
                    time.sleep(1)
                    print(clear)
                else:
                    confirmed = False
                    while confirmed == False:
                        print(f'Username: {regUsername}')
                        print(f'Password: {regPassword}')
                        print("Is this correct?")
                        print("[0] Yes [1] No")
                        # Asking user to confirm
                        confirm = input("")
                        if confirm == "0":
                            # Adding to database
                            baseUsernames.append(regUsername)
                            basePasswords.append(regPassword)
                            print("Registration Complete")
                            time.sleep(1)
                            confirmed = True
                            finishedReg = True
                            print(clear)
                        elif confirm == "1":
                            print("Restarting the process")
                            time.sleep(1)
                            print(clear)
                            confirmed = True
                        else:
                            print("Invalid Input")
                            time.sleep(1)
                            print(clear)
        elif mainMenuChoice == "2":
            leaveLoop = True
        elif mainMenuChoice == "AdminBypass":
            LogInDone = True
            leaveLoop = True
            location = 4
            print(clear)
            time.sleep(1)
        else:
            print("Invalid Input")
            time.sleep(1)
            print(clear)

    # If user has logged in
    if LogInDone == True:
        inLoginHome = True
        while inLoginHome == True:
            correctPassword = False
            print(f'Welcome {baseUsernames[location]}')
            print("Please choose from the options below")
            print("[0] View Account Info [1] Change Account Password [2] Logout")
            # Only accessed if account is admin
            if baseUsernames[location] == "Admin":
                print("As user is admin you also have access to view all accounts")
                print("[3] View all accounts")
            logInChoice = input("")
            if logInChoice == "0":
                print(clear)
                print("ACCOUNT INFORMATION")
                print(f'Username: {baseUsernames[location]}')
                print(f'Password: {basePasswords[location]}')
                time.sleep(1)
                print("Please press enter to return to the member menu")
                goHome = input("")
                print(clear)
            elif logInChoice == "1":
                print(clear)
                print("CHANGE PASSWORD")
                print("Please input your current password")
                currentPassword = input("")
                if currentPassword == basePasswords[location]:
                    correctPassword = True
                    while correctPassword == True:
                        print(clear)
                        print("Password Correct")
                        print("Please input your new password")
                        newPassword = input("")
                        print(clear)
                        print("Please confirm your new password")
                        newPasswordConfirm = input("")
                        # Checking passwords match
                        if newPassword == newPasswordConfirm:
                            print(clear)
                            print("Passwords are the same")
                            # Updating password
                            basePasswords[location] = newPassword
                            print(f"Your new password is {basePasswords[location]}")
                            time.sleep(1)
                            print("Please press enter to return to the member menu")
                            goHome = input("")
                            correctPassword = False
                            print(clear)
                        else:
                            print(clear)
                            print("Passwords are not the same please try again")
                            time.sleep(2)
                            print(clear)
                else:
                    print(clear)
                    print("Password Incorrect")
                    print("Returning to the memeber home page")
                    print("Please press enter to return to the member menu")
                    goHome = input("")
                    print(clear)
            elif logInChoice == "2":
                print(clear)
                print("Logged Out")
                inLoginHome = False
                reRunShutDown = True
                while reRunShutDown == True:
                    print("Please choose an option from below")
                    print("[0] Return to main menu [1] Shut down system")
                    logOutChoice = input("")
                    if logOutChoice == "0":
                        reRunShutDown = False
                        print(clear)
                        print("Returning to main menu")
                        time.sleep(1)
                        print(clear)
                        leaveLoop = False
                    elif logOutChoice == "1":
                        reRunShutDown = False
                        print(clear)
                        print("Shutting Down...")
                        time.sleep(1)
                        print(clear)
                    else:
                        reRunShutDown = True
                        print("Invalid Input")
                        time.sleep(1)
                        print(clear)
            elif logInChoice == "3":
                print(clear)
                print("All users accounts")
                time.sleep(1)
                count = 0
                # Repeating around all usernames
                for i in baseUsernames:
                    print("\n")
                    print(f'Username: {baseUsernames[count]}')
                    print(f'Password: {basePasswords[count]}')
                    count = count + 1
                    time.sleep(1)
                print("\n")
                print("List Completed")
                print("Press enter to return to member home page")
                returnHome = input()
                time.sleep(1)
                print(clear)
            else:
                print("Invalid Input")
                time.sleep(1)

    else:
        print("Shutting Down...")
        time.sleep(1)
        print(clear)

    if leaveLoop == True:
        # This is to stop the program actually stopping which would lose all database additions
        print("System currently sleeping. Please press enter to awake it")
        sleepInput = input("")
        print(clear)
        leaveLoop = False
