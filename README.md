# Si507-FinalProject
# Introduction
This is a final project for SI507. The program web scrapes top movies' information from IMDB website. It then stores the data into a question tree that asks users about their preferences and provides recommendations based on their choices. 

# Required Packages
- Flask
- Flask-Session
- Plotly
- pandas
- requests
- BeautifulSoup

# Instructions
Run the "execution.py" file and enter http://127.0.0.1:5000/ in your web browser to interact with the program. After opening the webpage, follow the instructions and answer the questions shown on the page. You will be able to view the results fulfill the requirements. If there are more than ten available results, it will only show the top ten with the highest ratings. And if there are fewer than ten results, all the results will be shown. The results are also sorted by imdb ratings. By choosing the movie from the available results you are interested in, you could view more details about the movie. 

# Data Structure
The movies were stored into a tree. The leaves of the tree are the lists of the movies which fulfill the requirements. And other nodes are several questions that help users to find the movies they would like to watch. The structure of the tree is like the tree from the tree project. According to the structure of the binary tree, each movie should only belong to one list.