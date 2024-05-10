import yaml
import unittest
from calculator import Calculator

global testcases
global calculator

with open("testcases.yaml") as stream:
    try:
        testcases = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def create_test_function(unitname, description, input, output):
    def test(self):
        try:
            calculator = Calculator()
            func = getattr(calculator, unitname)
            result = func(*input)
        except AttributeError:
            print("method not found")

        self.assertEqual(result, output, description)
    return test


class TestCalculator(unittest.TestCase):
    longMessage = True

if __name__ == '__main__':
    for unit in testcases['suite']:
        for test in unit['tests']:
            test_func = create_test_function(unit['name'], test['description'], test['input'], test['output'])
            setattr(TestCalculator, 'test_{0}_{1}'.format(unit['name'], test['description'].replace(" ", "_")), test_func)

    unittest.main()