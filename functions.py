class Rules:

    # Atributes
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    # Methods
    def add(self):
        return self.number_1 + self.number_2

    def substract(self):
        return self.number_1 - self.number_2

    def multiply(self):
        return self.number_1 * self.number_2

    def divide(self):
        return self.number_1 / self.number_2

    def operations(self,user_decision):
       if user_decision == "+":
           return self.add()
       elif user_decision == "-":
           return self.substract()
       elif user_decision == "*":
           return self.multiply()
       elif user_decision == "/":
           return self.divide()





