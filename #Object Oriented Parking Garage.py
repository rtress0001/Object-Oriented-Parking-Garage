#Object Oriented Parking Garage
#Unknown user
#
#Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP).
class Parking_Garage():
    #you will need a few attributes as well:
    #- tickets -> list
    #- parkingSpaces -> list
    #- currentTicket -> dictionary
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5]
        self.parkingSpaces = [1, 2, 3, 4, 5]
        self.currentTickets = {"Paid": False}

        #Your parking gargage class should have the following methods:

    def takeTicket(self):
        #- takeTicket
        #- This should decrease the amount of tickets available by 1
        #- This should decrease the amount of parkingSpaces available by 1
        takenticket = int(input("Please enter your parking space number: "))
        if takenticket in self.parkingSpaces:
            if takenticket in self.tickets:
                self.parkingSpaces.pop(takenticket)
                self.tickets.pop(takenticket)
            else:
                print("We are out of spaces sorry for inconvenience:")
        else: 
            print("We are out of spaces sorry for inconvenience:")
        print(f"your ticket is {takenticket} which is in space {takenticket}")
        


    def payForParking(self):
        #- payForParking
        #- Display an input that waits for an amount from the user and store it in a variable
        #- If the payment variable is not empty then -> display a message to the user that their ticket has been paid and they have 15mins to leave
        # - This should update the "currentTicket" dictionary key "paid" to True
        if  self.currentTickets['Paid'] == False:
            flag = True
            while flag:
                takenticket = int(input("Please enter your parking space number: "))
                paidforticket = int(input("Please enter an 15 to pay for parking: "))
                if paidforticket == 15:
                    print("you have paid for parking and have 15 minutes to leave")
                    self.currentTickets["Paid"]=True
                    flag = False
                    self.parkingSpaces.append(takenticket)
                    self.tickets.append(takenticket)
                else:
                    print("Incorrect amount for payment please try again:")
        



    def leaveGarage(self):
        #-leaveGarage
        #- If the ticket has been paid, display a message of "Thank You, have a nice day"
        #- If the ticket has not been paid, display an input prompt for payment
        #- Once paid, display message "Thank you, have a nice day!
        #- Update parkingSpaces list to increase by 1
        #- Update tickets list to increase by 1
        if self.currentTickets["Paid"]:
            print("Thank you, have a nice day")
        else:
            takenticket = int(input("Please enter your parking space number: "))
            flag = True
            while flag:
                paidforticket = int(input("Please enter an 15 to pay for parking: "))
                if paidforticket == 15:
                    print("Thank you, have a nice day")
                    self.currentTickets["Paid"]=True
                    flag = False
                else:
                    print("Incorrect amount for payment please try again:")
            self.parkingSpaces.append(takenticket)
            self.tickets.append(takenticket)
            self.currentTickets["Paid"]=False

alphaparking = Parking_Garage()
alphaparking.takeTicket()
alphaparking.payForParking()
alphaparking.leaveGarage()