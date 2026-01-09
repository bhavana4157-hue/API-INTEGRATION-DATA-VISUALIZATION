# API-INTEGRATION-DATA-VISUALIZATION

*COMPANY NAME*: CODTECH IT SOLUTIONS PRIVATE LIMITED

*NAME*: BHAVANA S

*INTERN ID*: CTIS0245

*DOMAIN*: PYTHON PROGRAMMING

*DURATION* 4 WEEKS

*MENTOR*: NEELA SANTHOSH

**API INTEGEATION AND DATA VISUALIZATION:

This project is a Python-based Weather Visualization Web Application designed to fetch and display live climate data for any city around the world. The application integrates backend server logic with a dynamic frontend interface to give users a simple way to explore real-time weather conditions.

At its core, the project uses Python and Flask to manage the backend and connect with the OpenWeatherMap public API. When the user enters a city name in the browser, the backend sends a live request to the weather API. This request retrieves critical information such as temperature, humidity, wind speed, and the city name. Flask then formats this data into JSON and returns it to the browser where it becomes visible instantly without refreshing the page.

The frontend is designed using HTML, CSS, and JavaScript. HTML structures the page layout, CSS creates an attractive gradient background, card blocks, buttons, and a modern UI look. JavaScript is responsible for sending the request to the backend, extracting data from the returned JSON, and updating the browser screen with real-time information. This makes the site interactive and user-friendly.

A major highlight of this project is visual data representation. Instead of only displaying plain numbers, weather values are plotted into a pie chart using Chart.js, which is integrated through a CDN link. The chart visually compares Temperature, Humidity, Feels-like values, and Wind speed, simplifying weather patterns and helping users quickly understand climate conditions.

The logic is powered entirely through Python. Flask handles routing using @app.route(). The / route loads the main HTML page, while /weather is the API endpoint that receives the city input and returns weather data. Error handling is also included, which displays a meaningful message if a city is not found or if no city name is entered.

This project clearly demonstrates essential web development concepts:

Frontend & Backend Communication – using fetch requests and JSON

Consuming Public APIs – real-time data from OpenWeatherMap

Data Visualization – converting values into a graphical chart

User Interaction – dynamic updates without refreshing

Python Application Deployment – running and testing on localhost

Overall, the project serves as a strong example of full-stack development using Python as the primary programming language. It showcases how Python can work beyond command-line execution and power real-time web applications. Students working with this project gain experience in multiple important skills: APIs, JSON parsing, frontend DOM manipulation, and data plotting. This makes the application both educational and practical to demonstrate in interviews, assessments, or resumes.

TOOLS USED:

Python 3 – Programming language

Flask – Backend micro web framework

Requests – To call OpenWeatherMap API

HTML5 – Page structure and layout

CSS – Styling and UI design

JavaScript – Dynamic browser updates

Chart.js – Graph visualization

VS Code – Development environment

OpenWeatherMap API – Live data source

 SOURCE:

OpenWeatherMap API
Provides realtime weather data
(public API)



