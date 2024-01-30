from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from threading import Thread

attendence_script = Flask(__name__)

@attendence_script.route('/')
def home():
    return render_template('index.html')

@attendence_script.route('/open_url', methods=['POST'])
def open_url():
    url = request.json['url']
    Thread(target=open_in_browser, args=(url,)).start()
    return jsonify({'message': 'Opening URL: ' + url})

def open_in_browser(url):
    driver = webdriver.Chrome()  # Update with the correct path to your chromedriver
    driver.get(url)

if __name__ == '__main__':
    attendence_script.run(port=5000)
