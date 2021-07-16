# simple-rasa-hotel-chatbot

Welcome to the assignment! In this assignment, we will try to build a simple chatbot for a hotel.
We will be using the Rasa framework for this assignment. Do not worry if you have no experience in ML or in using Rasa. All that is required for this assignment can be gleaned from the Rasa tutorial or Rasa docs. 

This assignment is intended to test your learning ability and problem-solving skills together with basic coding skills.

Expected time: 4 days

We hope that you have fun learning a new framework and building the chatbot!

# Objective - 
To build a simple chatbot for a hotel.
The chatbot should be able to respond to and handle the following basic functionalities
- Book room
- Request Room Cleaning
- Handle FAQs
- Handle Greetings

Example flows for these functionalities are described in detail in the Flows section.

# Installation

`python 3.6.8` is recommended for use with Rasa!

We highly recommend that you use a fresh virtual environment with python 3.6.8

Rasa 1.8 is the only requirement for this project. Please follow the Rasa installation instructions listed at [https://rasa.com/docs/rasa/user-guide/installation/](https://rasa.com/docs/rasa/user-guide/installation/)

Note) If you are facing trouble installing the rasa dependencies on your local computer you can make use of the Rasa Docker Environment. [https://rasa.com/docs/rasa/user-guide/docker/building-in-docker/](https://rasa.com/docs/rasa/user-guide/docker/building-in-docker/)

# Instructions

We suggest that you use the [Rasa framework](https://rasa.com/) to build this bot. Rasa is an open-source bot-building platform that will enable you to easily implement the functionalities required for this project.

You can check out this simple [Rasa tutorial](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/) to get an idea of how to approach the problem.

We will also recommend that you go through episodes 1, 2, 3, 5, 6 of the [Rasa Masterclass](https://www.youtube.com/watch?v=rlAQWbhwqLA&list=PL75e0qA87dlHQny7z43NduZHPo6qd-cRc) to familiarize yourself with how to use the different aspects of Rasa.

Once you have an understanding of the framework you can start designing your chatbot! In this repo we have added some Rasa boilerplate files. You can add your designed stories and intents and commit them in this repo. 

You can use the rasa framework to train a chatbot on your stories and use their interactive tool to chat with your chatbot. This is highlighted in the Masterclass videos.

Once you are finished you can let us know and we will test how well your chatbot is able to respond to the flows given below. You will be graded based on the number of correctly handled conversations.

# Flows

Please note that the flows below are only meant as examples to demonstrate functionalities. We would expect the bot to also handle questions having the same meaning but posed in different ways.

For eg. in our Book Room example, we have the user say "I want to book a room". In this case, the bot should also be able to direct the user to this flow if he says something along the lines of "I would like to book a room", "I want to book a room for my stay" etc.

Please add at least 5 training examples for each intent so that the bot is able to handle.

## Book Room

User: I want to book a room.

Bot: How many rooms would you like to book?

User: 2 rooms

Bot: What type of room would you want to book?
- Button1 - Simple 
- Button 2 - Deluxe

User: (Clicks on Button 1)

Bot: You have chosen to book 2 simple rooms

(Clicking on button 2 should be handled similarly)

## Clean room

### Schedule cleaning right away -

User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone right now?

Bot: Sure, I will send someone to your room right away.

### Schedule cleaning using relative time -

User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone after 2 hours?

Bot: Sure, I have scheduled a cleaning for 5 pm today.

The above two flows are the only multi-step flows. The flows should adapt themselves according to the user input. For eg., if the user says "I want to book a room for 2 people", the bot should not ask "How many rooms would you like to book?".

## FAQs

### Check-in timings -
User: What are your check-in timings?

Bot: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

### Check-out timings -
User: What are your check-out timings?

Bot: Check-out time is 11 AM. Please contact the reception for late checkout requests.

### Cancel Reservation -
User: How do I cancel a reservation?

Bot: To cancel a reservation, select the “Reservations” link from the homepage.

Bot: On the Reservations page, under the heading ‘View, Change or Cancel a Reservation,’ enter your confirmation number, and either the last name on the reservation or the last four digits of the credit card used to make the reservation.

### Cancellation Policy -
User: What is your cancellation policy?

Bot: The booking deposit is refundable if the cancellation occurs at least 15 days before arrival. For cancellations made after this limit, a penalty will be imposed based on the cancellation policy.

### Restaurant -
User: Does the hotel have a restaurant?

Bot: Yes, the hotel has a restaurant called the Zephyr Bar. With our menu we strive to reflect the historic art and the spirit of our neighborhood by offering a glimpse into what makes our area unique.

### Breakfast Availability -
User: Does the hotel offer breakfast?

Bot: The hotel provides its guests with a free made-to-order breakfast each morning.

### Breakfast timings -
User: What are the breakfast timings?

Bot: Monday through Friday breakfast is 6 am to 9 am. On Saturday and Sunday, we are open from 7 am to 10:30 am.

### Restaurant timings -
User: What are the timings of your restaurant?

Bot: Our restaurant serves a dazzling 24-hour menu.

---

Usage of git to iteratively build your code will be much appreciated. It will help us get a good idea about your progress.

Please let us know if you are getting stuck somewhere. Open communication is key! We can discuss stuff related to this assignment on a merge request.

Hope that this would be a fun experience for you and you learn something interesting. Happy coding!
