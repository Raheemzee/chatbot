#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections


# In[8]:


app = Flask(__name__)


# In[9]:


pairs = [
    ['hi|hello', ['Hi there!', 'Hello', 'Hey!']],
    ['how are you', ['I am doing well, thank you!', 'I am great!']],
    ['GOOD morning', ['Morning!']],
    ['Good afternoon', ['Afternoon!']],
    ['Good evening', ['Evening!']],
    ['Good bye|Bye',['Bye!','Bye-bye!']],
    ['.*\\byour name\\b.*',[' I do not have a name yet but I was built by Abdulraheem Akinola']],
    ['.*\\bcontact him\\b.*|.*\\bcontact Abdulraheem\\b.*', ['You can contact him on Whatsapp at +2347085496411 or email at abdulraheemakinola06@gmail.com']],
    ['.*\\bold is he\\b.*|.*\\bhis age\\b.*', ['He is 20 years old']],
    ['.*\\bhis favorite food\\.*',['He told me that all delicious food are his favorite😉']],
    ['.*\\bhis favorite color\\b.*', ['He told me his favorite color is blue']],
    ['.*\\bThank\\b.*|.*\\bThanks\\b.*', ['You are welcome💜']],
    ['(.*)', ['He did not tell me anything about that😌']]
]


chatbot = Chat(pairs, reflections)


# In[10]:


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    chatbot_response = chatbot.respond(user_message)
    return jsonify({'chatbot_response': chatbot_response})


# In[11]:


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')


# In[ ]:




