import re
myfile = "test.txt"
lines_list = []
regex_exp = r'(?P<Book>.+) \((?P<Author>.+)\)\r*\n- Your (?P<type>Highlight)(?:.+)\r*\n\r*\n(?P<content>.+)'
with open(myfile , 'r', encoding="utf8") as file:
    try:
        f = file.read()
    except Exception as e:
        raise e 

    
    iterator = re.finditer(regex_exp,f)
    # final_string = "".join(matched_string)
    for i in iterator:
        print(i.group('Book'))