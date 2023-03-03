from flask import Flask, render_template, request
import openai

# 在下面输入的自己的密钥就可以了
openai.api_key = "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"
# 创建对话的主函数
app = Flask(__name__)

chat_log = []
message_ai = ""

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("chat.html", chat_log=chat_log)

@app.route("/send_message", methods=['GET', 'POST'])
def send_message():
    message_use = request.form.get("message")
    global message_ai
    respons = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个AI聊天机器人."},
            {"role": "user", "content": message_use},
            {"role": "assistant", "content": message_ai},
            {"role": "user", "content": message_use}
        ]
    )
    # 储存返回结果
    message_ai = ""
    print(respons.choices)
    for choice in respons.choices:
        message_ai += choice.message.content
    chat_log.append(("YOU", message_use))
    chat_log.append(("GPT", message_ai))
    # 在此处添加回答的逻辑，将回答添加到chat_log中
    return render_template("chat.html", chat_log=chat_log)

if __name__ == "__main__":
    app.run(debug=True)




