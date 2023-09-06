---
layout: post
title: PDF Text Splitter
toc: True
description: I developed a text splitter for pdfs converted to html so I could extract data without manually copy-pasting it.
courses: {'compsci': {'week': 3, 'categories': ['3.A', '5.B']}}
categories: ['C3.0', 'C3.1', 'C4.1']
type: hacks
---

<link rel = "stylesheet" href="index.css">

## Website to turn PDF into HTML

https://cloudconvert.com/pdf-to-html

## Coding the HTML Splitter


```python
html = open("pis.html").read()
```

## Removing all Useless HTML Data from file


```python
divs = html.split("<div")
divs[20]
```

## Splitting HTML Data into Bold Text (in this case PIs) and Plaintext (in this case the Definitions)


```python
import re
import csv

pattern = r'<span.*?>|</span>'

pi = ""
section = ""
lines = []

csvwriter = csv.writer(open("pis.csv","w"))

# 

for div in divs:
    cl, txt = div.split(">",1)[:2]
    txt = re.sub(pattern, '', txt)
    txt = txt.split("<")[0]
    if " h4 " in cl:
        # print(f"TEXT:{txt}")
        lines.append(txt)
    elif " h3 " in cl:
        if lines:
            print(f"PI:{pi}")
            print(" ".join(lines))
            print("\n")
            csvwriter.writerow([section, "", "", pi, " ".join(lines)])
            pi = txt
            lines = []
        else:
            pi = pi + " " + txt
        # print(f"PI:{txt}")
    elif " h5 " in cl:
        section = txt

        
csvwriter = None
```
