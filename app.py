class Menu:
  # menu constructor
  def __init__(self, name, items, start_time, end_time):
    self.items = items
    self.name = name
    self.start_time = start_time
    self.end_time = end_time
  # string representation
  def __repr__(self):
    return f"{self.name} menu: available {self.start_time}-{self.end_time}."
  # add bill calculation method
  def calculate_bill(self, purchased_items):
    # ['pancakes', 'home fries', 'coffee']
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"Address: {self.address}"

  def available_menus(self, time):
    avail_menus = []
    for menu in self.menus:
      if time in range(menu.start_time, menu.end_time+1):
        avail_menus.append(menu)
    return avail_menus



##### brunch objects
#create first brunch object
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
# brunch object
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)


# calculate brunch bill
purchases = ['pancakes', 'home fries', 'coffee']
brunch_bill = brunch_menu.calculate_bill(purchases)

#creat second menu object
early_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
eb_menu = Menu('Early_bird', early_items, 1500, 1800)
eb_order = ['salumeria plate', 'mushroom ravioli (vegan)']
eb_bill = eb_menu.calculate_bill(eb_order)


 #create third menu object
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

#create kids menu object
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('Kids', kids_items, 1100, 2100)

# # # # # # # # #     
#### franchise objects
all_menus = [brunch_menu, eb_menu, dinner_menu, kids_menu]

flagship_store = Franchise('1232 West End Road', all_menus)

new_installment = Franchise('12 East Mulberry Street', all_menus)

available_menus = new_installment.available_menus(1100)
print(available_menus)


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# create business object

stores = [flagship_store, new_installment]

business_1 = Business('Basta Fazoolin with my Heart', stores)


arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

arepa_business = Business('Take a Arepa', arepas_place)






