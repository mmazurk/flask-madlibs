from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

new_story = Story(["noun", "verb", "adjective"], "There once lived a unicorn that sat around all day thinking aobut his favorite {noun}. He thought about it so much he felt {adjective} so he decided to {verb}.")

field_list = new_story.prompts

@app.route('/')
def submit_form():
    return render_template("index.html", fields = field_list)

@app.route('/stories', methods = ['POST'])
def process_post():

    noun = request.form["noun"]
    adjective = request.form["adjective"]
    verb = request.form["verb"]

    story_content = new_story.generate({"noun": noun, "adjective": adjective, "verb": verb})
    return render_template("stories.html", story = story_content)
    

