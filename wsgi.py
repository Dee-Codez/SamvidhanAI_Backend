from flask import Flask,jsonify,request
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('chatnbx_api_key')


app = Flask(__name__,static_url_path='/')
CORS(app)

@app.route('/', methods=['POST','GET'])
def api(request):
    if request.method == 'POST':
        return predict(request)
    else:
        return hello()


def predict(request):
    data = request.get_json()
    prompt = data['prompt']
    from langchain.llms import OpenAI
    from langchain.chat_models import ChatOpenAI
    chat_model = ChatOpenAI(
        openai_api_key=API_KEY,
        openai_api_base="https://chat.nbox.ai/api/",
        model_name="llama-2-chat-13b-4k"
    )
    out = chat_model.predict(prompt)
    return jsonify({"answer": out})
    
def hello():
    return jsonify({"answer":"This is a Law Based Chatbot"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, port=10000)