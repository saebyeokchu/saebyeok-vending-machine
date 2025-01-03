class VendingMachine :
    def __init__(self):
        self.beverages = {
            "Cola": {"price": 1100, "stock": 10},
            "Water": {"price": 600, "stock": 15},
            "Coffee": {"price": 700, "stock": 8}
        }
        self.accepted_cash = [100, 500, 1000, 5000, 10000]
        self.accpeted_payment_method = ['card','cash']

    def showMenus(self) :
        for name, info in self.beverages.items() :
            print(name, " : ", info["price"],"원")
    
    def showPaymentMethods(self) :
        for name in self.accpeted_payment_method :
            print(name)
    
    def checkChoice(self):
        self.showMenus()
        choice = input("\n Select the beverage with name : ").lower()
        
        if choice in self.beverages :
            if self.beverages[choice]["stock"] > 0:
                return choice
            else:
                print("\nOut of stock. Please choose another beverage.")
        else :
          print("\nNot a vaild beverage option. Please Try again.")  

    def checkPaymentMethod(self):
        self.showPaymentMethods()
        choice = input("\n Select the payment method with name : ").lower()
        
        if choice in self.accpeted_payment_method :
            return choice
        else :
            print("\nNot a vaild payment option. Please Try again.")
    
    def processCard(self,beverage):
        print("check if card is valid")
        print("Process payment with card")
    
    def processCash(self, beverage):
        total = 0
        price = self.beverages[beverage].price
        while total < price:
            try:
                amount = int(input(f"\nInsert cash (Accepted: {self.accepted_cash}): "))
                if amount in self.accepted_cash:
                    total += amount
                    print(f"Total inserted: {total} KRW")
                else:
                    print("Invalid amount of money. Try again.")
            except ValueError:
                print("Invalid input. Please insert cash.")
        change = total - price
        if change > 0:
            print(f"Change returned: {change} KRW")
        
    def dispense_beverage(self, beverage):
        print(f"\n{beverage} is dispensing...")
        self.beverages[beverage]["stock"] -= 1
        print("Enjoy your drink!")
    

    def dispense(self):
       print("Start the Vending Machine")
       while True:
            #step 1 check vaild input
            beverage = self.checkChoice()
            if beverage :
                payment = self.checkPaymentMethod()
            else :
                break
         
            #step2. process payment
            if payment == 'card' :
                self.processCard(beverage)
            elif payment == 'cash' : 
                self.processCash(beverage)
            else :
                break
                
            #step3. Dispense beverage
            self.dispenseBeverage(beverage)
            
            #step4. Check if user want to continue
            another = input("\nWould you like another beverage? (y/n): ").lower()
            if another != "y":
                print("\nOkay. We were happy to serve you. Bye.")
                break
         

machine = VendingMachine()
machine.dispense()
