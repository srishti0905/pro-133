# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Srishti Grover" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    father_name = "Vipin Kumar"  
    father_age = "41"   

    return render_template('father.html', name=father_name, age=father_age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    mother_name = "Seema Rani"  
    mother_age = "39"   

    return render_template('mother.html', name=mother_name, age=mother_age)

# define the route to friends webpage
@app.route("/friends")
def friends():
    friend_names ="dudo" 
    friend_ages = "12"

    return render_template('friends.html', names=friend_names, ages=friend_ages)

# add other routes, if you want

# run the file
if __name__ == '__main__':
    app.run(debug=True)
