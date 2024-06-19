from flask import Flask,render_template,request
import google.generativeai as palm
import os
from dotenv import load_dotenv

load_dotenv()

palm_api_key=os.environ["PALM_API_KEY"]
palm.configure(api_key=palm_api_key)

#set up flask app

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot",methods=["POST"])

def chatbot():
    user_input=request.form["message"]
    
    models=[m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model=models[0].name
    
    prompt=f"User:{user_input}\n PaLM Bot:"
    
    response = palm.generate_text(
      model=model,
      prompt=prompt,
      stop_sequences=None,
      temperature=0,
      max_output_tokens=1000
    )
    bot_response= response.result
  
    chat_history=[]
    chat_history.append(f"User:{user_input} \n PaLM Bot: {bot_response}")
    return render_template(
        "index.html",
        user_input=user_input,
        bot_response=bot_response,
        chat_history=chat_history
    )
if __name__=="__main__":
    app.run(debug=True)


