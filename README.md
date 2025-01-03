##Mechanism diagram document

**The vending machine operates through the following steps**
1. User Input : User select beverage and payment method among card and cash
  1.1 Error handling : check invalid payment method, out of stock beverage, insufficent amount of payment for beverage
2. Process payment : Process payment method
  2.1 If cash
    2.1.1 Validate the change of vending machine
      2.1.1.1 If not return with internal error
  2.2 If card : 
    2.2.1 Validate the card if it is chargable
      2.2.1.1 If not return with internal error
3. Process beverage : Check if required beverage dispensible
  3.1 If cash : Return any change if applicable
  3.2 If card : Process the payment
4. Dispense beverage : Dispense the beverage and update the inventory

![image](https://github.com/user-attachments/assets/e0c52491-5a8d-435e-b243-998f590152d9)
