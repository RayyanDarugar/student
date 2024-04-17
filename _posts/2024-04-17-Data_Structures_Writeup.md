---
toc: True
comments: True
layout: post
title: Data Structures Writeup Rayyan
description: Writeup for the combined Data Structures project of Trimester 3
type: tangibles
courses: {'compsci': {'week': 30}}
---

# Rayyan Darugar Data Structures Writeup

## Collections
- [ ] From VSCode using SQLite3 Editor, show your unique collection/table in database, display rows and columns in the table of the SQLite database.
<img width="1139" alt="Screenshot 2024-04-16 at 11 02 00 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/e1259022-b940-4281-9922-47f38f9effb7">
- [ ] From VSCode model, show your unique code that was created to initialize table and create test data.
<img width="1149" alt="Screenshot 2024-04-16 at 11 02 35 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/bcff6ddc-8397-4a14-93e0-ef1a8e5f4e10">

## Lists and Dictionaries
- [ ] In VSCode using Debugger, show a list as extracted from database as Python objects.
- [ ] In VSCode use Debugger and list, show two distinct example examples of dictionaries, show Keys/Values using debugger.
<img width="1440" alt="Screenshot 2024-04-16 at 11 06 31 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/79c683be-d2c1-4a51-ba3c-2b7179d93192">
<img width="1440" alt="Screenshot 2024-04-16 at 11 07 45 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/662a5725-3111-419a-a7c3-4e1777afb24c">

## APIs and JSON
- [ ] In VSCode, show Python API code definition for request and response using GET, POST, UPDATE methods. Discuss algorithmic condition used to direct request to appropriate Python method based on request method.
<img width="1127" alt="Screenshot 2024-04-16 at 11 08 50 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/9c58d3de-57eb-4fee-ab2d-bd9dccdfbeee">
- discussion: directs to the correct python request method via JSON data passed through and the correct frontend post. gets items individually and updates info accordingly.

- [ ] In VSCode, show algorithmic conditions used to validate data on a POST condition.
<img width="1032" alt="Screenshot 2024-04-16 at 11 12 39 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/b2cb7d8c-107c-4d95-a8b8-49536d0f992f">
<img width="971" alt="Screenshot 2024-04-16 at 11 15 08 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/5b0bebe5-2735-497a-985f-799f4679b646">

- [ ] In Postman, show URL request and Body requirements for GET, POST, and UPDATE methods.
- [ ] In Postman, show the JSON response data for 200 success conditions on GET, POST, and UPDATE methods.
- [ ] In Postman, show the JSON response for error for 400 when missing body on a POST request.
- [ ] In Postman, show the JSON response for error for 404 when providing an unknown user ID to a UPDATE request.
<img width="1314" alt="Screenshot 2024-04-16 at 11 16 59 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/360f95f6-cb7b-43c1-a10b-11e643c5a757">
<img width="1348" alt="Screenshot 2024-04-16 at 11 17 29 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/b41bb2c5-fa99-4e6a-a619-5d09810efd58">
<img width="1348" alt="Screenshot 2024-04-16 at 11 18 31 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/726e7f65-75b0-49e5-ac13-f12a604f63e3">



## Frontend
- [ ] In Chrome inspect, show response of JSON objects from fetch of GET, POST, and UPDATE methods.
- [ ] In the Chrome browser, show a demo (GET) of obtaining an Array of JSON objects that are formatted into the browsers screen.

<img width="1440" alt="Screenshot 2024-04-16 at 11 19 22 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/0f176aff-1c3b-4f5e-855a-9e469c6fb5ca">


- [ ] In JavaScript code, describe fetch and method that obtained the Array of JSON objects.
- [ ] In JavaScript code, show code that performs iteration and formatting of data into HTML.

<img width="1069" alt="Screenshot 2024-04-16 at 11 20 29 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/086b1fb6-d302-4f61-9402-01ac02879f25">


- [ ] In the Chrome browser, show a demo (POST or UPDATE) gathering and sending input and receiving a response that show update. Repeat this demo showing both success and failure.

<img width="1440" alt="Screenshot 2024-04-16 at 11 26 30 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/9c8274e2-9f1d-4c25-a4eb-6e56e61313fe">

<img width="1440" alt="Screenshot 2024-04-16 at 11 26 45 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/77e37162-f193-482f-91c3-befdb361be93">

- [ ] In JavaScript code, show and describe code that handles success. Describe how code shows success to the user in the Chrome Browser screen.

<img width="726" alt="Screenshot 2024-04-16 at 11 28 46 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/7da909fb-3ed5-4eb8-a95b-82a4885c7002">

- discuss: code, if no errors logging in, routes user to the game screen where they can play games from our site in chrome.

- [ ] In JavaScript code, show and describe code that handles failure. Describe how the code shows failure to the user in the Chrome Browser screen.

<img width="820" alt="Screenshot 2024-04-16 at 11 28 37 PM" src="https://github.com/RayyanDarugar/student/assets/63976232/3b499ac1-c96b-4341-8397-c3477236b853">

- discuss: code, if errors logging in, routes user to a 403 error page telling them their credentials are incorrect and asking them to try again in the chrome browser.