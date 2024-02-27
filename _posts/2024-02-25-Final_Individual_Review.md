---
toc: true
comments: false
layout: post
title: Rayyan Darugar Trimeser 2 Individual Review
description: Review of Trimester 2 CPT Project
type: tangibles
courses: { compsci: {week: 20} }
---

# Basic Project Description

TBFT: Turn Based Fantasty Tarkov:
- Simple strategy based game where the goal is to defeat an algorithm-controlled bot with smart attacks over multiple turns. You move to strategic positions and attack based on information you gain, like when the bot is attacking or moving and if you hit or miss. You can't see the enemy so you have to predict and attack effecvtively. You login, create a character based on set classes, and then play with it to defeat the enemy in royal court!

# My Feature

The feature I worked on was creating the backend database for character creation. I created the Character Class model which set the different stats for each class, and then made the Current Character model where it saves the character you are playing as and updates your stats as you lose health.

[Link to where I got the CB requirements](https://apcentral.collegeboard.org/media/pdf/ap-csp-student-task-directions.pdf)

# Component A: Program Code

| Collegeboard Requirements | My Feature |
|------------------|------------------|
| Instructions for input from one of the following: the user, a device, an online datas stream, a file.  | Our project, and specifically the backend takes data on the users choice of class, as well as a character name to append a character to their account for their game session. We take an input of their class (which contains their health, attack stats, and others), and append that to a SQL database. |
| Use of at least one list (or other collection type) to represent a collectino of data that is stored and used to manage program complexity and help fulfill the users purpose.  | An example of a collection of data that is stored is the database of characters and users stored in our backend, which saves stats like a users Health, Attack damage, and other skills they have. It helps fulfill our programs purpose as it allows us to use that data to track how many hits it takes them to defeat the enemy and how many times they can get hit by the enemy before they lose, making the game more strategic. I store all this collection data in a SQLite table in our backend through an API model, and take user input using post/put functions in our frontend page.: [![Screenshot-2024-02-27-at-12-11-31-AM.png](https://i.postimg.cc/RZCp07HX/Screenshot-2024-02-27-at-12-11-31-AM.png)](https://postimg.cc/56GS7FpC) |
| At least one procedure that contirubted to the program's intened purpose where you have defined: the name, return type, one or more parameters:  | This procedure appends a user's chosen class into the Current Character database so the game can adjust their stats mid game. Specifically, this PUT function (name) updates the character as the game goes on, like reducing its health when it gets hit. It gives out a return(response), and has parameters (self) which include the data on user health, classnames, etc.: [![Screenshot-2024-02-27-at-12-06-06-AM.png](https://i.postimg.cc/Z5PpB2rS/Screenshot-2024-02-27-at-12-06-06-AM.png)](https://postimg.cc/NKM5ZNJJ) |
| An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure  | This function shows the sequencing, selection, and iteration through all the classes in our Character Class database: [![Screenshot-2024-02-27-at-12-14-41-AM.png](https://i.postimg.cc/vZ6hT0m7/Screenshot-2024-02-27-at-12-14-41-AM.png)](https://postimg.cc/dhwrSmrD) |
| Calls to your student-developed prodcedure:  | calling initCharClasses: [![Screenshot-2024-02-27-at-12-16-26-AM.png](https://i.postimg.cc/g29RSmYR/Screenshot-2024-02-27-at-12-16-26-AM.png)](https://postimg.cc/5636jcQN) |
| Instructions for output (tactile, audible, visual, or ) based on input and program functionality  | This code is a function that gets all inputs necessary to add a user to the database, and then returns visual JSON data on the successfully created character: [![Screenshot-2024-02-27-at-12-21-41-AM.png](https://i.postimg.cc/zvsp5Qgc/Screenshot-2024-02-27-at-12-21-41-AM.png)](https://postimg.cc/N2xRkpb6). Underneath is a postman display of this: [![Screenshot-2024-02-27-at-12-24-25-AM.png](https://i.postimg.cc/qMmy8SqV/Screenshot-2024-02-27-at-12-24-25-AM.png)](https://postimg.cc/SJMn4ZcD) |


# Component B: Video

[Link to Video](https://drive.google.com/file/d/1rujjwfmllzVjMLzeJ1-4egG_ntPdlSX_/view?usp=sharing)


| Collegboard Requirements | My Video |
|------------------|------------------|
| Input to program  | Seen in video, uploading meme and entering text  |
| At least one aspect of the functionality of your program| The Gallery functionality which displays the database of memes  |
| Output produced by program:  | The meme being created but more specically for my feature being added into the gallery succesfully.  |
| My video does not have: | any distinguishing information and voice narration  |
| My video is | a .webmb, less than 1 minute in length, less than 30MB in file size.  |