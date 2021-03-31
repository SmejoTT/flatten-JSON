import json
import sys

class JSONhandler():
    def __init__(self):
        self.flattened_json = {}

    def flatten(self,json_string):
        try:
            json_object = json.loads(json_string)
        except json.JSONDecodeError:
            raise ValueError("Provided file is not a valid JSON file.")
             
        self.__flatten_recursive(json_object)
        flattened_json_string = json.dumps(self.flattened_json, indent=4)
        self.flattened_json = {}
        return flattened_json_string
    
    def __flatten_recursive(self,json_dict,key_path=""):
        delimeter = "."
        if not isinstance(json_dict, dict):
            self.flattened_json[key_path] = json_dict
            return

        for key, value in json_dict.items():
            if len(key_path)>0:
                new_key_path = key_path + delimeter + key
            else:
                new_key_path = key_path + key    
            self.__flatten_recursive(value,new_key_path)

if __name__ == "__main__":
    json_string = sys.stdin.read()
    handler = JSONhandler()
    print(handler.flatten(json_string))
    



