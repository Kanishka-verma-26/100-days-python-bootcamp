students=['kanishka','Alex',"Beth",'Caroline','Devansh','Aashish',"Dave",'Anu',"Rashi","Gursharan","Eddie","Paras",'Harshita']

import random

student_scores = {name : random.randint(1,100) for name in students }
print(student_scores)