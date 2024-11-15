import os
import json

def read(filename):
    with open(os.path.realpath('Recursion/excercise/1_recursion_search/Assets' + filename)) as data:
        if 'json' in data.name:
            return json.load(data)
        
        return data.read

    
def load_groups(filename):
    
