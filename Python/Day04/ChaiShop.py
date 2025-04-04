from abc import ABC,abstractmethod
class Chai(ABC):
    def __init__(self,name,base_price,qty_in_stk):
        self.name = name
        self.base_price = base_price
        self.qty_in_stk = qty_in_stk

    @abstractmethod
    def calculate_price(self) :
        pass

    @abstractmethod
    def display_info(self) :
        pass

class MasalaChai(Chai) :
    def __init__(self, name, base_price, qty_in_stk):
        super().__init__(name, base_price, qty_in_stk) 
        self.spice_cost = 10

    def calculate_price(self):
        return self.base_price + self.spice_cost

    def display_info(self):
        print("Name : Masala Chai | Price per cup : ",self.calculate_price(),"Stock :",self.qty_in_stk)

class GingerChai(Chai) :
    def __init__(self, name, base_price, qty_in_stk):
        super().__init__(name, base_price, qty_in_stk) 
        self.spice_cost = 8

    def calculate_price(self):
        return self.base_price + self.spice_cost

    def display_info(self):
        print("Name : Ginger Chai | Price per cup : ",self.calculate_price(),"Stock :",self.qty_in_stk)
    
class ElachiChai(Chai) :
    def __init__(self, name, base_price, qty_in_stk):
        super().__init__(name, base_price, qty_in_stk) 
        self.spice_cost = 12

    def calculate_price(self):
        return self.base_price + self.spice_cost

    def display_info(self):
        print("Name : Elachi Chai | Price per cup : ",self.calculate_price(),"Stock :",self.qty_in_stk)

class ChaiInventory :
    def __init__(self):
        self.list_of_chai = []
    
    def add_chai(self,chaiObj) :
        self.list_of_chai.append(chaiObj)
    
    def show_inventory(self):
        for chai in self.list_of_chai :
            chai.display_info()
    
    def get_total_inventory_value(self) :
        total_price = 0
        for chai in self.list_of_chai :
            total_price += chai.calculate_price()*chai.qty_in_stk
        
        return total_price

inventory = ChaiInventory()

chai1 = MasalaChai("Masala Chai", 20, 50)
chai2 = GingerChai("Ginger Chai", 18, 40)
chai3 = ElachiChai("Elaichi Chai", 25, 30)

inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹", inventory.get_total_inventory_value())