import webview
import random
import string

random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def custom_logic(window):
    window.evaluate_js(f'document.getElementById("randomPass").innerText = "{random_password}";')

def say_hello_to(name):
    print(name)

window = webview.create_window('Kilit Ekranı', 'index.html', fullscreen=True, js_api=custom_logic)

webview.start(say_hello_to, window)
