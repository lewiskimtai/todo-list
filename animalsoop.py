class Animal:
    weight = 23
    days_growing = 198
    growth_rate = 12  # expressed in percentage
    food_need = "Low"
    water_need = "Normal"
    status = "Healthy"
    type = "Mammal"
    name = "Animal"

    _report = f"""
     Water need: {water_need}
     Food need:  {food_need}
     Status: {status}
     Weight: {weight}kg
    """

    def needs(self):
        needs = f'Water: {self.water_need}, food: {self.food_need}'
        print(needs)

    def report(self):
        print(self._report)

    def grow(self):
        print(f'{self.days_growing+1} days old')

    def update_status(self, status):
        self.status = status
        print(f'{self.name} is currently: {status}')

    def change_animal_type(self, _type):  # changes animal type
        self.type = _type
        print(f'The animal is of type: {self.type}')


class Cow(Animal):
    def grow(self):
        self.days_growing += 129
        super(Cow, self).grow()


class Sheep(Animal):
    def grow(self):
        self.days_growing += 234
        super(Sheep, self).grow()


c = Cow()
c.name = "Cow"
print(f"The {c.name} is currently: {c.status}")
c.grow()
c.report()
c.change_animal_type("For beef.")
print("============================")

s = Sheep()
s.name = "Sheep"
s.update_status("Sick")
s.grow()
c.change_animal_type("For wool")