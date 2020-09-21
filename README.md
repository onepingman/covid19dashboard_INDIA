## CS50 Final Project: Covid - 19 Dashboard for India

### I have made my Dashboard live and it can be accessed from anywhere, to do so please click on this [link](https://indiacov19-ralphmachado.herokuapp.com/) .

### Brief description about my Web APP
I wanted to create an application which is easy-to-use and practical, that can be used by any common Indian individual. Since I had learnt
many new things from the past CS50 projects I felt I need to use these skills and create a web-app that many people actually want to see
and benefit from it. As my country India is world's 2nd most severely hit country due to COVID-19 I decided to create a Dashboard summarizing
the COVID-19 cases in the whole county and also in every Indian state. There were already many such dashboards out there but I found they 
had some shortcomings in them. To overcome these shortcomings, I have created my own COVID-19 tracker/dashboard and it has the following features:
1. My Web-app is mobile responsive.
2. It shows the **Total Confirmed Cases, Total Recovered Cases, Total Deaths and Active Cases** in the entire country as well as its 36 states 
and union territories.
3. The Dashboard has an interactive map of my country India, whenever any state in the map is clicked or hovered on with the mouse cursor, 
it will show the active cases in that state. These states on this map are filled with shades of red, where the state with the darkest 
shade of red means it is the most severely affected and the state with the lightest shade means it is least affected. If the active cases 
increase above certain defined values than the filled colour of that state also changes respectively.
4. The Dashboard has a chart which shows the countrywide **Daily New Cases, Daily Recovered Cases and Daily Deaths** on Y-Axis and the date on X-Axis.
5. If any state's name in the table which shows the **Total Confirmed Cases, Total Recovered Cases, Total Deaths and Active Cases** in all the 36 states 
is clicked then the end-user will be taken at the bottom of the page where a chart will appear that shows **Daily New Cases, Daily Recovered Cases and 
Daily Deaths** in that particular state.
6. I have configured the database in such a way that it will store only 2 months of historical data. Any data older than 2 months will be deleted and
simultaneously new data will be added everyday incrementally into the database.
7. My backend function that requests the API, runs automatically every 1 hr therefore in a day the API can be requested 24 times. On any day, if
the database gets updated once or at the time of the first API request then it wont be updated again until the next day. Only if there is any error
while updating the database the server will log **"Something went wrong"** and will try to update the database during the next API request i.e after
1 Hr.   
- **Other existing dashboards did not show **Daily New Cases, Daily Recovered Cases and Daily Deaths** of the whole country and state-wide in one chart 
and this is what I wanted to achieve with my dashboard. For end-users who would view this dashboard I wanted them to get an idea of the rate at which 
the number of people getting infected daily and recovering daily.**

### To create this project I used following things:-
1. Python Django Framework at the backend server side.
2. Pure Javascript, HTML, CSS and bootstrap at the frontend and styling.
3. I used of [Datamaps](https://datamaps.github.io/) library in Javascript for rendering India's map.
4. I used [ApexCharts](https://apexcharts.com/) library in Javascript for rendering the Daily trend charts.
5. The source of my COVID-19 data is an API called [COVID-19 INDIA](https://rapidapi.com/fsolutions-fsolutions-default/api/covid-19-india2/details) 
from [RapidAPI](https://rapidapi.com/) .

### Challenges involved in creating this project
1. Rendering the MAP and charts inside one single page app was really a tough job. 
2. Making the MAP and charts mobile responsive was also a challenge.
3. On the backend I wanted to create an algorithm in such a way that once I deploy this App I wont need to come back again and again to manually,
update or delete the database, therefore I created the app standalone which will work fine without my intervention.
4. In my Final project I made use of existing knowledge learnt so far in CS50 and  also used libraries that were not thought earlier in this
course.
5. Before I began with this course I had very limited programming knowledge and I had thought that I would want to built something that people 
will use. The projects that I created earlier were also challenging but there are similar products which are far better already available for use. 
Therefore I feel my final project is practical and distinct than the other projects I have done so far.