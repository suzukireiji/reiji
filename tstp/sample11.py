import re

text = "The ghost that says boo haunts the loo"

text2 = re.findall(".oo", text)
print(text2)
