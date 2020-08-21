import unittest
class TestCase(unittest.TestCase):
	def setUp(self):
		self.input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
		self.output_value = {'I': {'deserve': {'to': {'be': 'hired'}}}}
	def test_nested_reverse(self):
		self.assertEqual(nested_reverse(self.input_value),self.output_value)
	def test_is_dict(self):
		self.assertTrue(is_dict(self.input_value))
	def tearDown(self):
		self.input_value.clear()
		self.output_value.clear()

def is_dict(p): 
	return isinstance(p, dict)

def nested_reverse(mylist, result={}):
	for k, v in mylist.items():
		if is_dict(v): #is last?
			if result=={}: #first data
				for k2, v2 in v.items():
					result={k2:k}
					result=nested_reverse(v2, result)
			else: #middle data 
				result={k:result}
				result=nested_reverse(v, result)
		else: #last data
			if result=={}: #first and last data
				result={v:k}
			else: #last data
				result={k:result}
				result={v:result}
	return result

if __name__ == '__main__':
    unittest.main()
