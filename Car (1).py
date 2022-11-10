#Car.py
class Car():
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price 

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        if self.make < rhs.make:
            return False       
        if self.make == rhs.make:
            if self.model > rhs.model:
                return True
            if self.model < rhs.model:
                return False     
            if self.model == rhs.model:  
                if self.year > rhs.year:
                    return True
                if self.year < rhs.year:
                    return False     
                if self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
                    if self.price < rhs.price:
                        return False     
                    if self.price == rhs.price:
                        return False
           

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        if self.make > rhs.make:
            return False       
        if self.make == rhs.make:
            if self.model < rhs.model:
                return True
            if self.model > rhs.model:
                return False     
            if self.model == rhs.model:  
                if self.year < rhs.year:
                    return True
                if self.year > rhs.year:
                    return False     
                if self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
                    if self.price > rhs.price:
                        return False     
                    if self.price == rhs.price:
                        return False

    def __eq__(self, rhs):
        if (self.make == rhs.make) and (self.model == rhs.model) and (self.year == rhs.year) and (self.price == rhs.price):
            return True

    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make.upper(), self.model.upper(), self.year, self.price)
