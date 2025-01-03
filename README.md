## Mechanism diagram document

**The vending machine operates through the following steps**
1. User Input : User select beverage and payment method among card and cash
```
  1.1 Error handling : check invalid payment method, out of stock beverage
```
2. Process payment : Process payment method
  ``` 
  2.1 If cash
  
    2.1.1 Validate the change of vending machine
    
      2.1.1.1 If not return with internal error
      
  2.2 If card : 
  
    2.2.1 Validate the card if it is chargable
    
      2.2.1.1 If not return with internal error
 ```

3. Dispense beverage : Dispense the beverage and update the inventory

![image](https://github.com/user-attachments/assets/4813cb07-a810-4465-b862-cae34cddbdb2)
