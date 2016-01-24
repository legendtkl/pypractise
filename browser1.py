import webbrowser, os

url = 'file://' + os.path.abspath('page.html')
webbrowser.open(url)
