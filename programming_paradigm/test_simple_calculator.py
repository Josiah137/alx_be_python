import unittest  
from simple_calculator import SimpleCalculator  

class TestSimpleCalculator(unittest.TestCase):  

    def setUp(self):  
        """Set up the SimpleCalculator instance before each test."""  
        self.calc = SimpleCalculator()  

    def test_addition(self):  
        """Test the addition method with various inputs."""  
        self.assertEqual(self.calc.add(2, 3), 5)  
        self.assertEqual(self.calc.add(-1, 1), 0)  
        self.assertEqual(self.calc.add(-1, -1), -2)  
        self.assertEqual(self.calc.add(0, 0), 0)  

    def test_subtraction(self):  
        """Test the subtraction method with various inputs."""  
        self.assertEqual(self.calc.subtract(5, 2), 3)  
        self.assertEqual(self.calc.subtract(-1, -1), 0)  
        self.assertEqual(self.calc.subtract(0, 0), 0)  
        self.assertEqual(self.calc.subtract(3, 7), -4)  

    def test_multiplication(self):  
        """Test the multiplication method with various inputs."""  
        self.assertEqual(self.calc.multiply(3, 3), 9)  
        self.assertEqual(self.calc.multiply(-1, 1), -1)  
        self.assertEqual(self.calc.multiply(-1, -1), 1)  
        self.assertEqual(self.calc.multiply(0, 5), 0)  

    def test_division(self):  
        """Test the division method with normal and edge cases."""  
        self.assertEqual(self.calc.divide(10, 2), 5)  
        self.assertEqual(self.calc.divide(-20, 5), -4)  
        self.assertEqual(self.calc.divide(0, 5), 0)  
        self.assertIsNone(self.calc.divide(10, 0))  # Check division by zero  

if __name__ == "__main__":  
    unittest.main()
