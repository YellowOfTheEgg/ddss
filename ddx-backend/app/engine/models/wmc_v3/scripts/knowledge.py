import csv
import re
from decimal import Decimal

#based on this class an python object will be created which contains structured information of knowlegdegraph.csv
class Knowledge():
    def __init__(self):

        self.file_path='app/engine/models/wmc_v3/scripts/resources/DerivedKnowledgeGraph_final.csv'      
        self.data=self.read_file()
        self.knowledge=self.create_knowledge_dict()

    def read_file(self):
        with open(self.file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)
            data = []
            for row in csv_reader:
                data.append(row)
            return data


    def create_knowledge_dict(self):
        res = {}
        for line in self.data:
            symptoms = []
            for symptom_str in line[1].split(", "):
                symptom_name = re.sub(
                    r" \(.*\)", "", symptom_str
                )  # .replace(" ","_").replace("-","_")
                symptom_weight = Decimal(
                    symptom_str[symptom_str.find("(") + 1 : symptom_str.find(")")]
                )
                symptoms.append((symptom_name, symptom_weight))
            res[line[0]] = symptoms
        return res

    def get_weight_rows(self):
        res=[]
        for line in self.data:
            for symptom in line[1].split(', '):
                symptom_name = re.sub(
                    r" \(.*\)", "", symptom
                )  # .replace(" ","_").replace("-","_")
                weight = Decimal(
                    symptom[symptom.find("(") + 1 : symptom.find(")")]
                )
                res.append((line[0],symptom_name,weight))        
        return res


    def get_entry_list(self):
        diseases_and_symptoms = list(self.knowledge.keys())    
        for arr in self.knowledge.values():
            for tpl in arr:
                symptom_name = tpl[0]  # .replace(" ","_")#.replace('-','_')
                diseases_and_symptoms.append(symptom_name)
        return set(diseases_and_symptoms)


    
