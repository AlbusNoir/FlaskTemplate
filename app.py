from flask import Flask, render_template

# APP SETTINGS
app = Flask(__name__)

# ROUTES
@app.route('/')
def index():
    return render_template('index.html')
    # return index because base is just a template holding reuseable code like the navbar. Index is your actual entrypoint


# RUN
if __name__ == '__main__':
    app.run()
    # set debug=True if you need debug. DON'T DO THIS IN PRODUCTION
    '''
    Some common run params:
    host=0.0.0.0
    port=#### (default port for flask is 5000, change here if needed)
    Ex: app.run(host='0.0.0.0', port=8000) -> this will run the app on the local machine and advertise it at http://this.machine.ip.address:8000 
    Default is http://127.0.0.1:5000
    '''