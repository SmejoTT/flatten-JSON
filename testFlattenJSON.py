import unittest
import json
import os
import platform
import subprocess
from flattenJSON import JSONhandler

class TestFlatten(unittest.TestCase):
    def testExample1(self):
        file = open("test/data/test1.json", mode='r')
        json_string = file.read()
        file.close()

        file = open("test/data/test1_target.json", mode='r')
        json_string_expected = file.read()
        file.close()

        handler = JSONhandler()
        test1_actual = json.loads(handler.flatten(json_string))
        test1_expected = json.loads(json_string_expected)
        self.assertDictEqual(test1_actual,test1_expected)

    def testExample2(self):
        file = open("test/data/test2.json", mode='r')
        json_string = file.read()
        file.close()

        file = open("test/data/test2_target.json", mode='r')
        json_string_expected = file.read()
        file.close()

        handler = JSONhandler()
        test2_actual = json.loads(handler.flatten(json_string))
        test2_expected = json.loads(json_string_expected)
        self.assertDictEqual(test2_actual,test2_expected)

    def testExample3(self):
        file = open("test/data/test3.json", mode='r')
        json_string = file.read()
        file.close()

        file = open("test/data/test3_target.json", mode='r')
        json_string_expected = file.read()
        file.close()

        handler = JSONhandler()
        test3_actual = json.loads(handler.flatten(json_string))
        test3_expected = json.loads(json_string_expected)
        self.assertDictEqual(test3_actual,test3_expected)

    def testExample4(self):
        file = open("test/data/test4.json", mode='r')
        json_string = file.read()
        file.close()

        file = open("test/data/test4_target.json", mode='r')
        json_string_expected = file.read()
        file.close()

        handler = JSONhandler()
        test4_actual = json.loads(handler.flatten(json_string))
        test4_expected = json.loads(json_string_expected)
        self.assertDictEqual(test4_actual,test4_expected)

class TestInvalidInput(unittest.TestCase):
    def testCatchException(self):
        file = open("test/data/test5.json", mode='r')
        invalid_json_string = file.read()
        file.close()
        handler = JSONhandler()
        with self.assertRaises(ValueError):
            handler.flatten(invalid_json_string)


class TestCLI(unittest.TestCase):
    def testPipe(self):
        system_type = platform.system()
        path = os.getcwd().replace("\\","/")
        if system_type == "Windows":
            subprocess.run("{}/test/scripts/test_cli.bat".format(path))
        else:
            subprocess.run("{}/test/scripts/test_cli.sh".format(path))
        
        file = open("actual_output.json", mode='r')
        actual_output = json.loads(file.read())
        file.close()

        file = open("test/data/test1_target.json", mode='r')
        expected_output = json.loads(file.read())
        file.close()

        self.assertDictEqual(actual_output, expected_output)
        os.remove("actual_output.json")



if __name__=="__main__":
    unittest.main()