from functools import total_ordering


@total_ordering
class Article:
    def __init__(self, link, price):
        self.price = price
        self.link = link

    def __eq__(self, other):
        return (self.price, self.link) == (other.price, other.link)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self):
        return " Price = " + str(self.price)+" € link to Item = "+self.link

    def __add__(self, other):
        if type(other) == type(self):
            return self.price + other.price
        else:
            return self.price + other

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
