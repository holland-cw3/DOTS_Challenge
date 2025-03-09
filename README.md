# PolkaDOTS


# The Problem
The University of Maryland Department of Transportation Services (DOTS) provides a full range of parking and transportation services to a diverse community of more than 50,000 students, faculty and staff in the Greater College Park area. Services include Shuttle-UM, parking management, transportation demand management, and other programs. The current system is not user friendly (in the form of a complicated PDF), and does not take into account special events (i.e. sporting events, and construction), and updates very consistently. We wanted to determine a solution that would allow visitors to accurately understand where they are allowed to park based on ever evolving restrictions.

# Our Solution
We decided that the best way to go about this was to design a mult-layer filtering system
that would take into account the current date/time, and the users list of permissions. 

In the information challenge, we were given multiple data sets describing when and where a user 
could park. This project was originally intended to make use of AI/ML, however the black and white nature
of the problem led us to determine that an algorithmic solution was a better approach.

![image](https://github.com/user-attachments/assets/9fd85c61-7381-4241-b340-4dc9070c99d3)

_General Structure of our Algorithm_

Our algorithm resulted in 0 false positives across 50 test cases provided by UMD's department of transportation, meaning users
would not be told they could park in locations that they actually could not park in.

# Frontend
Our frontend was made with JavaScript, React, Material UI, Axios, and the Google Maps API. Given user input, it places Polka Dots on
a map, signifying where a user may park (note the blue dots signify locations that have overlapping lots).
![image](https://github.com/user-attachments/assets/f77be13b-adbd-4b77-a0a5-5f6d0bb109ed)

# Backend
Our backend & algorithm was built with Python, Pandas, and Flask. 


