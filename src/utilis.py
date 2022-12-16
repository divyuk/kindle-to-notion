import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

database_ID = os.environ.get("database_ID")
secret_Key = os.environ.get("secret_Key")

def get_pageid(title):
    url = f"https://api.notion.com/v1/databases/{database_ID}/query"
    payload = {
        "page_size": 100,
        "filter": {
            "property": "Name",
            "rich_text": {
                "equals": title
            }
        }
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)
    if len(data['results']) == 0:
        return None
    page_id = data['results'][0]['id']
    return page_id

def create_page(title, author):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {
            "type": "database_id",
            "database_id": database_ID
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                                "content": title
                        }
                    }
                ]
            },
            "Author": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": author
                        }
                    },
                ]
            },
             "Source": {
                    "select": {
                    "name": "Kindle"
                    }
            },
            "Type": {
                "select": {
                "name": "Book"
                }
            }
        }
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.post(url, json=payload, headers=headers)
    
def create_block(page_id):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    main_block=[]
    main_block.append(
        {
            "type": "heading_3",
            "heading_3": {
                "rich_text": [{
                "type": "text",
                "text": {
                    "content": "Book highlights and Notes",
                    "link": None
                }
                }],
                "color": "default",
                "is_toggleable": True
            },
            "has_children":True
        }
    )
    payload = {
        "children": main_block
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }

    response = requests.patch(url, json=payload, headers=headers)
    data = json.loads(response.text)
    block_id = data['results'][0]['id']
    return block_id

def get_blockid(page_id):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Authorization": f"Bearer {secret_Key}"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    block_id = ""
    for d in data["results"]:
        block_id = d['id'] if 'heading_3' in d and d['heading_3']['rich_text'][0]['text']['content'] == "Book highlights and Notes" else ""
    return block_id


def put_data(block_id,paragraph_list):
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    children_list = []
    for text in paragraph_list:
        if text[1] == "highlight":
            children_list.append(
                {
                    "type": "quote",
                    "quote": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content":text[0],
                            },
                        }],
                        "color": "default"
                    }
                }
            )
        else:
            children_list.append(
                {
                    "type": "callout",
                    "callout": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content":text[0],
                            },
                        }],
                        "icon": {
                            "emoji": "📝"
                        },
                        "color": "default"
                    }
                }
            )
    payload = {
        "children": children_list 
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret_Key}"
    }
    response = requests.patch(url, json=payload, headers=headers)
    
def get_paragraphs(block_id):
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Authorization": f"Bearer {secret_Key}"
    }
    response = requests.get(url, headers=headers)

    paragraphs = []
    excerpt = ()
    data = json.loads(response.text)
    for item in data['results']:
        if data['results'][0]['parent']['block_id'] == block_id:
            if 'quote' in item.keys():
                for words in item['quote']['rich_text']:
                    excerpt = (words['plain_text'], "highlight")
            elif 'callout' in item.keys():
                for words in item['callout']['rich_text']:
                    excerpt = (words['plain_text'], "note")

        paragraphs.append(excerpt)
        

    return paragraphs