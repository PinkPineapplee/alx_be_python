class Calculator:
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition of two numbers.
        Static methods do not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication of two numbers.
        Class methods can access class-level data using 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
