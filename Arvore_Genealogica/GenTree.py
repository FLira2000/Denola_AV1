from Leaf import Member
import json

class GenTree:
    def __init__(self, name = None, file_path = None):
        if file_path != None:
            self.build_from_file(file_path)
        
    def dict_to_tree(self, obj):
        if list(obj.keys()) != []:
           return Member(obj['me'], self.dict_to_tree(obj['mother']), self.dict_to_tree(obj['father']))
        else:
            return {}

    def read_json(self, json_path):
        with open(json_path) as fl:
            return json.load(fl)

    def build_from_file(self, filepath):
        self.dct = self.read_json(filepath)
        self.root = self.dict_to_tree(self.dct)

    def export_to_file(self):
        with open(f'tree_{self.root}.json', 'w') as fl:
            fl.write(json.dumps(self.dct))

    def print_tree(self):
        pass
