'''
A) Create a parent class called Property that has the following attributes: 
Property_name — the name of the property 
Property_address — the address of the property 
Owner_name — the owner of the property 
Property_Type Type of property. Is it rent or sale? 
Price- the price to rent or purchase property 
The class should have a method called display_property_info() that displays the property’s name, address, and owner. 
B) Create a subclass called PropertyToRent that inherits from the Property class. This class should have additional attributes: 
renter_name 
date_rented 
lease_duration 
It should have a method called display_rental_details() that displays all property details along with the renter’s name, date rented, and duration of the lease. 
C) Create another subclass called PropertyForSale that also inherits from the Property class. 
This class should have additional attributes: 
buyer_name 
date_sold 
It should have a method called display_sale_details() that displays the property’s name, buyer’s name, and the date it was sold. 
Task: Develop a class diagram to guide the program development phase. Follow the link to complete this. 
'''

#class
class Property:
    def __init__(self, propertyName, propertyAddress, ownerName, propertyType, price):
        self.propertyName = propertyName
        self.propertyAddress = propertyAddress
        self.ownerName = ownerName
        self.propertyType = propertyType
        self.price = price
    
    def displayPropertyinfo(self):
        print(f"The property's name is {self.propertyName}.\nThe address is {self.propertyAddress}.\nThe owners name is {self.ownersName}.\nThe property type is {propertyType}.\nThe price is {price}.")

class propertytoRent(Property):
    def __init__(self, propertyName, propertyAddress, ownerName, propertyType, price, renterName, dateRented, leaseDuration):
        super().__init__(self, propertyName, propertyAddress, ownerName, propertyType, price, renterName, dateRented, leaseDuration)
        self.renterName = renterName
        self.dateRented = dateRented
        self.leaseDuration = leaseDuration
    
    def displayRentaldetails(self):
        print(f"The renters name is {self.renterName}.\nThe date it was rented is {self.dateRented}.\nThe lease lasts for {self.leaseDuration}.")

class propertyforSale(Property):
     def __init__(self, propertyName, propertyAddress, ownerName, propertyType, price, buyerName, dateSold):
        super().__init__(self, propertyName, propertyAddress, ownerName, propertyType, price)
        self.buyerName = buyerName
        self.dateSold = dateSold
     
     def displaySaledetails(self):
        print(f"The renters name is {self.buyerName}.\nThe date it was rented is {self.dateSold}.")

#main
rentalProperty1 = propertytoRent("byron", "64", "oscar", "house", "£1", "oscar", "12/06/09", "5 years")
buyProperty1 = propertyforSale("shelley", "67", "noonan", "flat", "£1,000,000,000", "noonan", "14/11/25")

rentalProperty1.displayPropertyinfo()
rentalProperty1.displayRentaldetails()

buyProperty1.displayPropertyinfo()
buyProperty1.displaySaledetails()