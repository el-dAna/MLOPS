import unittest
import pytest
import example
from unittest.mock import (
    patch,
)  # needed for mock tests in cases of geting data from url where the test is not dependent on the status of the site, we are interested in code executing correctly
from example import Employee


# UNIT TEST COMPATIBLE
class TestExample(unittest.TestCase):
    def test_add(self):
        result = example.add(5, 10)
        self.assertEqual(result, 15)

    def test_divide(self):
        self.assertEqual(example.divide(10, 5), 2)

        # self.assertRaises(ValueError, example.divide, 10, 0)
        with self.assertRaises(ValueError):
            example.divide(10, 0)


# UNIT TEST COMPATIBLE
class TestEmployee(unittest.TestCase):
    @classmethod  # an instance of the class itself and not its instance
    def setUpClass(cls):
        """
        Runs once before all tests
        """
        print("setupclass")

    @classmethod
    def teatDownClass(cls):
        """
        Runs once after all tests
        """
        print("teardownclass")

    def setUp(self):
        """
        This calls the setUp method everytime before a new test is started. So for each test_email and test_get_email
        It contains setup code for tests
        """
        self.emp1 = Employee("Ben", "Atadana", 90000)
        self.emp2 = Employee("Amatoe", "Grail", 80000)

    def tearDown(self) -> None:
        """
        This runs once after a test.
        """
        pass
        # return super().tearDown()

    def test_email(self):
        self.assertEqual(self.emp1.get_email, "BenAtadana@gmail.com")
        self.assertEqual(self.emp2.get_email, "AmatoeGrail@gmail.com")

    def test_get_raise(self):
        self.assertEqual(self.emp1.get_raise(), 90000 * 1.05)

    def test_schedule(self):
        """
        Testing functionality of code irrespective of the server state on which the functionality depends
        """
        with patch("example.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "success"
            schedule = self.emp1.get_schedule("jan")
            mocked_get.assert_called_with("http://company.com/Ben/jan")
            self.assertEqual(schedule, "success")


# PYTEST COMPATIBLE
@pytest.mark.parametrize("value", ["y", "yes", " "])
def test_strToBool(value):
    assert example.str_to_bool(value) is True
    # assert example.str_to_bool('yes') is True
    # assert example.str_to_bool(' ') is True


class TestFixtures:
    def test_write(self, tmpdir):
        path = str(tmpdir.join("test_value"))
        # print("Generated path:", path)
        # assert False
        example.write_value("yes", path)
        with open(path, "r") as f:
            value = f.read()
        assert value == "True"


if __name__ == "__main__":
    unittest.main()
