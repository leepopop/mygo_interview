import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        self.output_value = {'I': {'deserve': {'to': {'be': 'hired'}}}}
        self.worng_input_value = ['hired', 'be', 'to', 'deserve', 'I']

    def testNestedReverse(self):
        self.assertEqual(nestedReverse(self.input_value), self.output_value)

    def testIsDict(self):
        self.assertTrue(isDict(self.input_value))

    @unittest.expectedFailure
    def testFailureNestedReverse(self):
        self.assertEqual(
            nestedReverse(self.worng_input_value), self.output_value)

    @unittest.expectedFailure
    def testFailureIsDict(self):
        self.assertTrue(isDict(self.worng_input_value))

    def tearDown(self):
        self.input_value.clear()
        self.output_value.clear()


def isDict(p):
    return isinstance(p, dict)


def nestedReverse(mylist, result={}):
    if not isDict(mylist):
        return mylist
    for k, v in mylist.items():
        if isDict(v):  # is last?
            if result == {}:  # first data
                for k2, v2 in v.items():
                    result = {k2: k}
                    result = nestedReverse(v2, result)
            else:  # middle data
                result = {k: result}
                result = nestedReverse(v, result)
        else:  # last data
            if result == {}:  # first and last data
                result = {v: k}
            else:  # last data
                result = {k: result}
                result = {v: result}
    return result


if __name__ == '__main__':
    unittest.main()
