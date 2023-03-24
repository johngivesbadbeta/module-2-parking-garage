class parkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    # paying now or later for ticket
    def payForParking(self):
        self.currentTicket = {}
        self.purchased_ticket = input("Would you like to pay $15 for parking now? yes/no ")
        if self.purchased_ticket == 'yes':
            print('Please take ticket. You have 15min to leave.')
            self.currentTicket['paid'] = True
            self.takeTicket()
        elif self.purchased_ticket == 'no':
            print('Please take ticket and pay when leaving.')
            self.currentTicket['paid'] = False
            self.takeTicket()

    #  taking ticket after paying
    def takeTicket(self):
        self.tickets -= 1
        self.parkingSpaces -= 1
        print(str(self.tickets) + " tickets left.")
        print(str(self.parkingSpaces) + " spaces left.")
        self.leaveGarage()

    # leaving garage
    def leaveGarage(self):
        exit = input("Exit the Garage? yes/no ")
        if exit.lower() == 'yes':
            if self.currentTicket['paid'] == True:
                print("Thank you, have a nice day.")
                self.tickets += 1
                self.parkingSpaces += 1
                print(str(self.tickets) + " tickets left.")
                print(str(self.parkingSpaces) + " spaces left.")
            elif self.currentTicket['paid'] == False:
                exit_payment = input("Please pay $15 now. yes/no ")
                if exit_payment.lower() == 'yes':
                    print("Thank you have a nice day.")
                    self.tickets += 1
                    self.parkingSpaces += 1
                    print(str(self.tickets) + " tickets left.")
                    print(str(self.parkingSpaces) + " spaces left.")
                if exit_payment == 'no':
                    self.leaveGarage()
        if exit.lower() == "no":
            print("No overnight parking. Please leave by 10pm or face a fine.")
            self.leaveGarage()
            



        
occupancy = parkingGarage(50, 50, {})

def purchaseTicket():
    while True:
        response = input("Would you like to the enter the parking garage? yes/no ")
        if response.lower() == 'yes':
            occupancy.payForParking()
        elif response.lower() == 'no':
            print('Then go away! I mean thanks for stopping by.')
        break

purchaseTicket()