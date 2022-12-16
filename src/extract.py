import re
from custom_exceptions import InvalidFILEException

class Clippings:

    def __init__(self) -> None:
        self.main_dict={}
        self.highlights = []
        self.extracted_data=[]
        self.regex_exp = r'(?P<Book>.+) \((?P<Author>.+)\)\r*\n- Your (?P<type>Highlight|Note)(?:.+)\r*\n\r*\n(?P<content>.+)'
    
    def extract_data(self,file_path:str)->list:
        with open(file_path , 'r', encoding="utf-8-sig") as file:
            try:
                clippings_file = file.read()
                clippings_file = re.sub("\uFEFF", "", clippings_file)
            except Exception:
                raise InvalidFILEException
        
            iterator = re.finditer(self.regex_exp,clippings_file)
            for data in iterator:
                title = data.group('Book')
                author = data.group("Author")
                type_of_content = data.group("type")
                content = data.group("content")
                if type_of_content == "Highlight":
                    excerpt = (content, "highlight")
                else:
                    excerpt = (content, "note")
                flag = True
                not_duplicate  = True
                for text in self.extracted_data:
                    if text["title"] == title:
                        not_duplicate = False
                        for h in text["highlights"]:
                            if h[0] == excerpt[0]:
                                flag = False
                        if(flag):
                            text["highlights"].append(excerpt)
                if not_duplicate:
                    self.highlights.append(excerpt)
                    self.main_dict["title"] = data.group('Book')
                    self.main_dict["author"] = author
                    self.main_dict["highlights"] = self.highlights
                    self.extracted_data.append(self.main_dict)
                    self.highlights = []
                    self.main_dict  = {}
                    
        return self.extracted_data