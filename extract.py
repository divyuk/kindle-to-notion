import re
import json

myfile = "test.txt"
flag = True
extracted_data = []
my_dict=dict()
highlights = []
regex_exp = r'(?P<Book>.+) \((?P<Author>.+)\)\r*\n- Your (?P<type>Highlight)(?:.+)\r*\n\r*\n(?P<content>.+)'
with open(myfile , 'r', encoding="utf-8-sig") as file:
    try:
        f = file.read()
        f = re.sub("\uFEFF", "", f)
    except Exception as e:
        raise e 
  
    iterator = re.finditer(regex_exp,f)
    for i in iterator:
        for j  in extracted_data:
            if j["title"] == i.group('Book') : 
                j["highlights"].append(i.group("content"))
                flag = False
                break
        if flag:
            my_dict["title"] = i.group('Book')
            my_dict["author"] = i.group("Author")
            highlights.append(i.group("content"))
            my_dict["highlights"] = highlights
            extracted_data.append(my_dict)
        my_dict={}
        highlights=[]
        flag = True
    d = []
    for k in extracted_data:
       k["highlights"]= list(set(k["highlights"]))
        

print(extracted_data)
with open('data.json', 'w',  encoding="utf-8") as f:
    json.dump(extracted_data, f, ensure_ascii = False) 