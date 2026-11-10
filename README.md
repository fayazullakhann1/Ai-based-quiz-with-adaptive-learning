# AI-Based Quiz System with Adaptive Learning and Performance Analytics

## Overview

The AI-Based Quiz System with Adaptive Learning is a web application developed to provide a personalized learning experience through adaptive quizzes. The system adjusts question difficulty based on the user's performance and provides detailed analytics to help learners understand their strengths and weaknesses.

The application includes user authentication, subject selection, level-based quizzes, timers, hints, skip options, performance tracking, and downloadable progress reports.

## Problem Statement

Traditional quiz systems provide the same set of questions to all learners regardless of their knowledge level. This approach does not support personalized learning and may lead to reduced engagement and ineffective assessment.

This project addresses the problem by introducing an adaptive learning mechanism that dynamically adjusts question difficulty according to the learner's performance.

## Objectives

* Develop an interactive quiz platform.
* Provide adaptive difficulty adjustment based on user performance.
* Prevent repeated questions during a quiz session.
* Track user progress and skill performance.
* Generate detailed performance analytics.
* Provide downloadable progress reports.
* Improve learning efficiency through personalized assessment.

## Features

* User Registration and Login
* Subject Selection
* Difficulty Levels (Easy, Medium, Hard)
* Adaptive Learning Mechanism
* Timer-Based Quiz
* Hint System
* Skip Questions
* No Repeated Questions
* Skill-Based Analysis
* Performance Analytics
* Downloadable PDF Reports
* User-Friendly Interface

## Technologies Used

### Front End

* HTML
* CSS
* JavaScript

### Back End

* Python (Flask Framework)

### Data Storage

* JSON File Storage

### Operating System

* Windows 10 / Windows 11

### IDE

* Visual Studio Code (VS Code)

## Project Flow

Login/Register

↓

Dashboard

↓

Subject Selection

↓

Level Selection

↓

Quiz Start

↓

Question with Timer

↓

Submit / Skip / Hint

↓

Adaptive Difficulty Adjustment

↓

Skill Update

↓

Feedback

↓

Progress Analytics

↓

Download Report

↓

Logout

## Adaptive Learning Mechanism

The system analyzes user responses during the quiz.

* If a learner answers questions correctly, the difficulty level increases.
* If a learner answers incorrectly, the difficulty level decreases.
* Skill scores are calculated based on performance in different topics.
* The system avoids repeating previously asked questions.

This adaptive behavior provides a personalized learning experience.

## AI Component

The AI component in this project is the Adaptive Learning Engine.

The system continuously monitors user performance and dynamically adjusts the quiz difficulty level. Based on correct and incorrect answers, it personalizes the learning path and generates skill-based performance analytics.

Although this version does not use advanced Machine Learning or Deep Learning models, it demonstrates intelligent decision-making through adaptive learning techniques.

## Future Enhancements

This project currently implements a basic adaptive quiz mechanism. In future versions, the system can be enhanced with advanced AI and Machine Learning features such as:

* Machine Learning-based difficulty prediction
* Personalized question recommendations
* Natural Language Processing (NLP) for descriptive answers
* AI-powered virtual tutor assistance
* Speech-based interaction
* Learning pattern analysis
* Real-time performance prediction
* Cloud database integration
* Leaderboards and gamification
* Mobile application support
* Multi-language support
* Advanced dashboards and visual analytics

## Folder Structure

AI-Based-Quiz-System/

├── app.py

├── students.json

├── requirements.txt

├── templates/

│ ├── home.html

│ ├── register.html

│ ├── login.html

│ ├── dashboard.html

│ ├── tutor.html

│ ├── feedback.html

│ └── progress.html

├── static/

│ ├── style.css

│ └── images/

├── screenshots/

└── README.md

## Installation

1. Clone the repository

git clone <repository-url>

2. Navigate to the project folder

cd AI-Based-Quiz-System

3. Install required packages

pip install -r requirements.txt

4. Run the application

python app.py

5. Open your browser

http://127.0.0.1:5000

## Conclusion

The AI-Based Quiz System with Adaptive Learning provides a personalized and engaging assessment environment. By adapting question difficulty according to learner performance and generating detailed analytics, the system enhances the learning experience. Future enhancements can transform this project into a fully AI-powered intelligent learning platform.

