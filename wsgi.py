from flask import Flask,jsonify,request
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('chatnbx_api_key')


app = Flask(__name__,static_folder='./dist',static_url_path='/')
CORS(app)

@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json()
    prompt = data['prompt']
    from langchain.schema import HumanMessage, SystemMessage
    from langchain.chat_models import ChatOpenAI
    chat_model = ChatOpenAI(
        openai_api_key=API_KEY,
        openai_api_base="https://chat.tune.app/api/",
        model_name="mixtral-8x7b-inst-v0-1-32k",
    )
    messages=[
            SystemMessage(
                content="You are SamvidhanAI, An AI Assistant referring to the Indian Constitution."
            ),
            HumanMessage(
                content=prompt,
            ),
    ]

    out = chat_model(messages)
    return jsonify({"answer": out.content})

    # from chainfury.components.tune import ChatNBX, chatnbx
    # out = chatnbx(
    # chatnbx_api_key=API_KEY,
    # model = "mixtral-8x7b-inst-v0-1-32k",
    # messages = [
    #     ChatNBX.Message(role = "system", content = "You are SamvidhanAI, An AI Assistant referring to the Indian Constitution."),
    #     ChatNBX.Message(role = "user", content = prompt),
    # ])
    # return jsonify({"answer": out})
    
@app.route('/', methods=['GET'])
def hello():
    return jsonify({"answer":"This is a Law Based Chatbot"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, port=5000)