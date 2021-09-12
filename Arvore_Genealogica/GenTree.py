from Leaf import Member
import json

class GenTree:
    def __init__(self, name = None, file_path = None):
        if file_path != None:
            self.dict_to_tree(self.read_json(file_path)))
        
    def dict_to_tree(self, obj):
        
    
    def read_json(self, json_path):
        with open(json_path) as fl:
            return json.load(fl)
