from flask import Flask, render_template, make_response, request, send_file
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import os, shutil

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('driver/chromedriver',chrome_options=chrome_options)

app = Flask(__name__, static_url_path="")

screen_folder = 'screen/'
result_folder = 'runs/detect/exp/'
delete_folder = 'runs'

@app.route("/")
def index():
    return render_template("index.html", path="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

@app.route('/url', methods=['POST'])
def url():
    url = request.form.get('url')

    if url is None:
        return make_response("Url is null", 400)

    print(url)
    file_name = url.split("//")[1] + ".png"
    file_name = file_name.replace("/","-")
    folder = 'screen/'
    try:
        driver.get(url)
    except Exception:
        return make_response("Cannot open website", 503)
    width = 1920
    height = 1080
    driver.set_window_size(width, height)
    if os.path.isdir(delete_folder):
        shutil.rmtree(delete_folder)
    path = screen_folder + file_name
    
    try:
        driver.save_screenshot(path)
        print("Saved png for " + url)
    except Exception:
        return make_response('Error with save picture',503)

    os.system(f"python3 YOLO/detect.py --weights YOLO/elements-model/best.pt --img 1920 --source {path} ")

    os.remove(path)
    proccessed_image = result_folder + file_name
    new_result_folder = "static/results/"
    os.rename(proccessed_image, new_result_folder+file_name)

    return "/results/"+file_name
    

