---
layout: post
comments: True
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

# Removing all Useless HTML Data from file


```python
divs = html.split("<div")
divs[20]
```

# Splitting HTML Data into Bold Text (in this case PIs) and Plaintext (in this case the Definitions)

NOTE: Chat GPT was used to teach me how to create this code via reviewing it and instructing me on how Regular Expressions work. (key to cleaning up the cluttered HTML data)


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

# Hacks Showcases From All Previous Lessons

Here I showcase JS Tables, Python Emojis, Make use of Linux and show all completed coding prerequisites, and throughout the rest of this code I demonstrate python knowledge, webpage integration, and HTML management. I've also added a comment section with a breakdown of how I developed the tool.


```python
%%html

<h3>PI Data Table Draft</h3>

<!-- Body contains the contents of the Document -->
<body>
    <table class="table">
        <thead>
            <tr>
                <th>Section</th>
                <th>Performance Indicator</th>
                <th>Definition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Business Law</td>
                <td>Describe the United States judicial system</td>
                <td>The judicial branch of the federal government interprets, applies, and administers the laws of the US. It is  a network of courts at all levels  of government. Federal courts include district courts, federal courts of appeals, and the U.S.  Supreme Court. The state court system also includes a state Supreme Court, associate circuit courts, city or municipal courts, small claims courts,  juvenile courts, and probate courts.</td>
            </tr>
            <tr>
                <td>Business Law</td>
                <td>Determine the relationship between government and business</td>
                <td>The government serves as both a protector and a regulator of business in a free market economy. It serves to protect business property, enforce  contracts and settle disagreements through the courts, and collect taxes on the products businesses sell. As a regulator, the government enacts  and enforces laws to prohibit certain behaviors, control business activities, and require certain standards. Examples of such laws include laws to control monopolies, set product safety standards, and regulate prices</td>
            </tr>
            <tr>
                <td>Business Law</td>
                <td>Explain unfair labor practices</td>
                <td>Actions taken by employers or unions that are illegal under the National Labor Relations Act (NLRA) and other labor laws. (Unfair treatment because of race, religion, gender, etc.)</td>
            </tr>
            <tr>
                <td>Entreprenuership</td>
                <td>What is the nature and scope of entrepreneurship</td>
                <td>Entrepreneurship is a self-motivated activity, which helps the entrepreneur to bring changes in the process of production, innovation in  production, new usage of materials, creator of market etc. It is a mental attitude to foresee risk and uncertainty and do something new in  an effective manner to achieve certain goals.</td>
            </tr>
        </tbody>
    </table>
</body>
```



<h2>PI Data Table Draft</h2>

<!-- Body contains the contents of the Document -->
<body>
    <table class="table">
        <thead>
            <tr>
                <th>Section</th>
                <th>Performance Indicator</th>
                <th>Definition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Business Law</td>
                <td>Describe the United States judicial system</td>
                <td>The judicial branch of the federal government interprets, applies, and administers the laws of the US. It is  a network of courts at all levels  of government. Federal courts include district courts, federal courts of appeals, and the U.S.  Supreme Court. The state court system also includes a state Supreme Court, associate circuit courts, city or municipal courts, small claims courts,  juvenile courts, and probate courts.</td>
            </tr>
            <tr>
                <td>Business Law</td>
                <td>Determine the relationship between government and business</td>
                <td>The government serves as both a protector and a regulator of business in a free market economy. It serves to protect business property, enforce  contracts and settle disagreements through the courts, and collect taxes on the products businesses sell. As a regulator, the government enacts  and enforces laws to prohibit certain behaviors, control business activities, and require certain standards. Examples of such laws include laws to control monopolies, set product safety standards, and regulate prices</td>
            </tr>
            <tr>
                <td>Business Law</td>
                <td>Explain unfair labor practices</td>
                <td>Actions taken by employers or unions that are illegal under the National Labor Relations Act (NLRA) and other labor laws. (Unfair treatment because of race, religion, gender, etc.)</td>
            </tr>
            <tr>
                <td>Entreprenuership</td>
                <td>What is the nature and scope of entrepreneurship</td>
                <td>Entrepreneurship is a self-motivated activity, which helps the entrepreneur to bring changes in the process of production, innovation in  production, new usage of materials, creator of market etc. It is a mental attitude to foresee risk and uncertainty and do something new in  an effective manner to achieve certain goals.</td>
            </tr>
        </tbody>
    </table>
</body>



# Showcase of Python Tricks with Emojis


```python
import emoji
print(emoji.emojize("DECA is an International Business Education organization :money_bag:"))
print(emoji.emojize("PI's, or Performance Indicators, are ways that students are judged in competition and graded. :speaking_head: "))
```

    DECA is an International Business Education organization 💰
    PI's, or Performance Indicators, are ways that students are judged in competition and graded. 🗣️ 


# Defining DECA via Wikipedia


```python
import wikipedia 
from IPython.display import display, Markdown # add for Jupyter

terms = ["DECA(organization)", "Performance Indicator"]
for term in terms:
    # Search for a page 
    result = wikipedia.search(term)
    # Get the summary of the first result
    summary = wikipedia.summary(result[0])
    print(term) 
    # print(summary) # console display
    display(Markdown(summary)) # Jupyter display
```

    DECA(organization)



DECA Inc., formerly Distributive Education Clubs of America, is a 501(c)(3) not-for-profit career and technical student organization (CTSO) with more than 224,000 members in all 50 U.S. states, Washington, DC; Canada, China, Germany, Poland, Guam, Mexico, Puerto Rico and Spain. The United States Congress, the United States Department of Education and state, district and international departments of education authorize DECA's programs.
DECA is organized into two unique student divisions each with programs designed to address the learning styles, interests, and focus of its members. The High School Division includes over 173,000 members in 3,200 schools. The Collegiate Division (formerly Delta Epsilon Chi) includes over 4,000 members in 200+ colleges and universities.The organization's mission statement is as follows:

DECA prepares emerging leaders and entrepreneurs in marketing, finance, hospitality and management in high schools and colleges around the globe. The four components of the organization's Comprehensive Learning Program are that DECA integrates into classroom instruction, applies learning, connects to business, and promotes competition. DECA prepares the next generation to be academically prepared, community-oriented, professionally responsible, experienced leaders.Dr. Ed Davis served as executive director from 1992 to 2014. Paul Wardinski served as executive director from 2014 to 2018. Lou DiGiola served as the executive director in 2018. Nicole Rodrigues formerly served as president. Frank Peterson is currently serving as the executive director since 2020. Lori Hairston is currently serving as president.


    Performance Indicator



A performance indicator or key performance indicator (KPI) is a type of performance measurement. KPIs evaluate the success of an organization or of a particular activity (such as projects, programs, products and other initiatives) in which it engages. KPIs provide a focus for strategic and operational improvement, create an analytical basis for decision making and help focus attention on what matters most.Often success is simply the repeated, periodic achievement of some levels of operational goal (e.g. zero defects, 10/10 customer satisfaction), and sometimes success is defined in terms of making progress toward strategic goals. Accordingly, choosing the right KPIs relies upon a good understanding of what is important to the organization. What is deemed important often depends on the department measuring the performance – e.g. the KPIs useful to finance will differ from the KPIs assigned to sales.
Since there is a need to understand well what is important, various techniques to assess the present state of the business, and its key activities, are associated with the selection of performance indicators. These assessments often lead to the identification of potential improvements, so performance indicators are routinely associated with 'performance improvement' initiatives. A very common way to choose KPIs is to apply a management framework such as the balanced scorecard.
The importance of such performance indicators is evident in the typical decision-making process (e.g. in management of organisations). When a decision-maker considers several options, they must be equipped to properly analyse the status quo to predict the consequences of future actions. Should they make their analysis on the basis of faulty or incomplete information, the predictions will not be reliable and consequently the decision made might yield an unexpected result. Therefore, the proper usage of performance indicators is vital to avoid such mistakes and minimise the risk.




# Understanding how the Wikipedia Summarize Function works


```python
import inspect 
from wikipedia import summary
print(inspect.getsource(summary))
```

    @cache
    def summary(title, sentences=0, chars=0, auto_suggest=True, redirect=True):
      '''
      Plain text summary of the page.
    
      .. note:: This is a convenience wrapper - auto_suggest and redirect are enabled by default
    
      Keyword arguments:
    
      * sentences - if set, return the first `sentences` sentences (can be no greater than 10).
      * chars - if set, return only the first `chars` characters (actual text returned may be slightly longer).
      * auto_suggest - let Wikipedia find a valid page title for the query
      * redirect - allow redirection without raising RedirectError
      '''
    
      # use auto_suggest and redirect to get the correct article
      # also, use page's error checking to raise DisambiguationError if necessary
      page_info = page(title, auto_suggest=auto_suggest, redirect=redirect)
      title = page_info.title
      pageid = page_info.pageid
    
      query_params = {
        'prop': 'extracts',
        'explaintext': '',
        'titles': title
      }
    
      if sentences:
        query_params['exsentences'] = sentences
      elif chars:
        query_params['exchars'] = chars
      else:
        query_params['exintro'] = ''
    
      request = _wiki_request(query_params)
      summary = request['query']['pages'][pageid]['extract']
    
      return summary
    

