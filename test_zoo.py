import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "error")
        self.assertEqual(self.zoo.get_ticket_price(1), 50)
        self.assertEqual(self.zoo.get_ticket_price(15), 100)
        self.assertEqual(self.zoo.get_ticket_price(54), 150)
        self.assertEqual(self.zoo.get_ticket_price(67), 100)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()