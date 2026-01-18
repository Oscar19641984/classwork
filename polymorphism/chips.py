class USA:
    def chips(self):
        print("Thin slices of potatoes")

class UK:
    def chips(self):
        print("Thick-cut fries")

class Australia:
    def chips(self):
        print("Potato crisps")

class India:
    def chips(self):
        print("Potato wafers or snacks")

usa = USA()
uk = UK()
aus = Australia()
india = India()

for country in (usa, uk, aus, india):
    country.chips()