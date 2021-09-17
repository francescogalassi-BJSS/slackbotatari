from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    data = ""
    if request.method == 'POST':
        requestData = request.get_json()
        roomId = requestData["room_id"]
        organiser = requestData["organiser"]   
        
        #  Create booking
        with open('rooms.json') as json_file:
                data = json.load(json_file)
                booking = {
                    "organiser": organiser
                }
                
        # Updates data in the server    
        data["rooms"][roomId]["bookings"].append(booking)
        # Updates data in the file   
        file = open("rooms.json", "w")
        file.write(json.dumps(data))
        file.close()

        return data 
        
    else:
        return 'Access Forbidden'
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
