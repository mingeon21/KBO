# KBO
## Demo

* url: https://fdf6-39-118-39-230.ngrok-free.app/status/statistics

### Overview 
My project is centered on using the past 20 years of baseball statistics from the Korean Baseball Association. By utilizing graphical methods and the vast data, I aim to display players' performances on a yearly basis, transforming statistical data into a user-friendly graphical model, which displays the correlations of different baseball statistical values. This service aims to provide a more engaging understanding of baseball statistics for both existing fans and newcomers to the sport. My appreciation for baseball and its rich statistical depth and story drove my interest. While baseball's statistics offered an intricate perspective on players' performances, the decreasing popularity of the Korean Baseball League provoked my desire to emulate successful U.S. baseball prediction websites. I aspire to introduce Korean fans to the captivating realm of baseball predictions, merging my passion for the sport with a solution for a prevailing gap in the Korean baseball community.
### Data
* url: https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx
* Descritpion: I have used the pitching data from 2003 to 2023 for the graphical display
### Development Environment 
* OS: MacOS Ventura 13.4.1
* Programming Language: Python3.11, HTML, CSS, Javascript
* Framework: Django 4.2.2
### Run
``` python
cd KBO/demo/kbo_demo
python3.11 manage.py runserver ${PORT} 
```
### Results
<img width="1904" alt="Screenshot 2023-10-04 at 22 35 48" src="https://github.com/mingeon21/KBO/assets/87740901/2cf58774-78ec-4869-b88e-594607d78ea8">

Adjusting the 3 tabs at the top left corner, users can alter the x and y statistics and the year of which the users want to analyze. The according graph will be displayed below the tabs. Below the graph will be a display of a table, where the chosen x and y statistics and the team and name of the player who has the smallest and the largest x-axis statistic value

## Machine Learning
* Approach: Linear Regression
### DEMO
* url: https://fdf6-39-118-39-230.ngrok-free.app/status/ml

### Overview 
By leveraging machine learning algorithms, more specifically, Linear Regression, I aim to predict players' performances on a yearly basis, transforming statistical data into a user-friendly prediction model, especially since the Korean Baseball Organization lacks such a platform. The primary goal is to bridge the gap in Korea's baseball analytics by creating a user-friendly baseball prediction service using machine learning algorithms.

### Data
* url: https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx
* Descritpion: I have used the pitching data from 2003 to 2023 to conduct supervised training for my machine learning algorithms
* Data Amount: 4580
### Development Environment 
* OS: MacOS Ventura 13.4.1
* Programming Language: Python3.11, HTML, CSS, Javascript
* Framework: Django 4.2.2
### Run
``` python
cd KBO/modeling
python3.11 predict.py 
```
### Results
<img width="438" alt="Screenshot 2023-10-04 at 22 52 39" src="https://github.com/mingeon21/KBO/assets/87740901/d97137bb-29cb-4f67-8225-1bbb93b4bc58">

The machine learning tab only fixed number of statistical values. IP, ERA, and WHIP. When the user inputs the value of IP, machine learning algorithm will output the most likely values of ERA and WHIP for pitchers who threw inputed amount of IP. 
