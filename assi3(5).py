class Calculator:
    def __init__(self, initial_value=0):
        self._value = initial_value  

    def add(self, number):
        """Add a number to the current value."""
        self._value += number

    def subtract(self, number):
        """Subtract a number from the current value."""
        self._value -= number

    def get_value(self):
        """Return the current value."""
        return self._value

    def set_value(self, new_value):
        """Set a new value for the calculator."""
        self._value = new_value

if __name__ == "__main__":
    calc = Calculator()  

    calc.add(10)
    print("After adding 10:", calc.get_value())  

    calc.subtract(5)
    print("After subtracting 5:", calc.get_value()) 

    calc.set_value(100)
    print("After setting value to 100:", calc.get_value())  
    