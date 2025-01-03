Class VendingMachine:
    def __init__(self):
        self.beverages = {
            "Cola": {"price": 1100, "stock": 10},
            "Water": {"price": 600, "stock": 15},
            "Coffee": {"price": 700, "stock": 8}
        }
        self.accepted_cash = [100, 500, 1000, 5000, 10000]
        self.accpeted_payment_method = ['card','cash']

    def showMenus() :
        for name, info in self.beverages.items() :
            print(name, " : ", info["price"],"원")
    
    def checkChoice():
        choice = input("\n Select the beverate")
    

    def dispense(self):
       print("Start the Vending Machine")
       While True:
           self.showMenus()
         
            #step 1 check vaild input
            choice = self.checkChoice()
            payment = self.checkPaymentMethod()
         
            #step2. process 
            if payment == 'card' :
                self.processCard()
            else : 
                self.processCash()
                
            #step3. Dispense beverage
            self.dispenseBeverage()
            
            #step4. Check if user want to continue
            another = input("\nWould you like another beverage? (y/n): ").lower()
            if another != "y":
                print("\nOkay. We were happy to serve you. Bye.")
                break
         

  

machine = VendingMachine()
machine.dispense()
