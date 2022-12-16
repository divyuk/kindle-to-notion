from extract import Clippings
from logger import logging
from utilis import get_pageid,create_page,create_block,get_blockid,put_data,get_paragraphs

myfile = "test.txt"
my_clips = Clippings()
extracted_data=my_clips.extract_data(myfile)
for book in extracted_data:
    title = book["title"]
    highlights = book["highlights"]
    author = book['author']   
    pageid = get_pageid(title)
      
    if pageid is None:
        create_page(title=title, author=author)
        logging.info(f"📄 Page created!")
        pid = get_pageid(title)
        logging.info(f"📄 The page id for book {title} is = {pageid}")
        bid = create_block(pid)
        logging.info(f"Block created! 🔲 ")
        logging.info(f"Writing Highlights/Notes! 📜🖋")
        put_data(bid,highlights)
        logging.info(f"📜🖋")
        logging.info(f"----Done----")
    else:
        bid = get_blockid(pageid)
        if bid !="":
            notes = get_paragraphs(bid)
            new_notes = []
            for note in highlights:
                if note not in notes:
                    new_notes.append(note)
            logging.info(f"New Note : {new_notes} ")
            logging.info(f" 🚀 Syncing Highlights/Notes! 📜🖋")
            put_data(bid, new_notes)
            logging.info(f"🌌----Done----🌌")