#made with love by HIMANSHU
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


states = [
   {'id':1,
    'state':'Andhra Pradesh',
    'capital':'Hyderabad/Amravati',
    'language':'telugu/tamil',
    },
   {'id':2,
    'state':'Arunachal pradesh',
    'capital':'Itanagar',
    'language':'7 languages!!',
    },
   {'id':3,
    'state':'Assam',
    'capital':'Dispur',
    'language':'Assamese',
    },
   {'id':4,
    'state':'Bihar',
    'capital':'Patna',
    'language':'Hindi',
    },
   {'id':5,
    'state':'Chattisgarh',
    'capital':'Naya Raipur',
    'language':'Hindi',
    },
   {'id':6,
    'state':'Goa',
    'capital':'Panaji',
    'language':'Konkani',
    },
   {'id':7,
    'state':'Gujrati',
    'capital':'Gandhinagar',
    'language':'Gujrati',
    },
   {'id':8,
    'state':'Haryana',
    'capital':'Chandigarh',
    'language':'Hindi',
    },
   {'id':9,
    'state':'Himachal Pradesh',
    'capital':'Shimla',
    'language':'Hindi/Pahari',
    },
   {'id':10,
    'state':'Mizoram',
    'capital':'Aizwal',
    'language':'Mizo/English',
    },
   {'id':11,
    'state':'Jharkhand',
    'capital':'Ranchi',
    'language':'Hindi',
    },
   {'id':12,
    'state':'Karnataka',
    'capital':'Bangalore',
    'language':'Kannad',
    },
   {'id':13,
    'state':'Kerala',
    'capital':'Tiruvananthapuram',
    'language':'Malyalam',
    },
   {'id':14,
    'state':'Madhya Pradesh',
    'capital':'Bhopal',
    'language':'Hindi',
    },
   {'id':15,
    'state':'Maharashtra',
    'capital':'Mumbai',
    'language':'Marathi',
    },
   {'id':16,
    'state':'Manipur',
    'capital':'Imphal',
    'language':'Manipuri',
    },
   {'id':17,
    'state':'Meghalya',
    'capital':'Shillong',
    'language':'Khasi/Jaintia/Garo',
    },
   {'id':18,
    'state':'Nagaland',
    'capital':'Kohima',
    'language':'6 languages!',
    },
   {'id':19,
    'state':'Odisha',
    'capital':'Bhubaneshwar',
    'language':'Qriya',
    },
   {'id':20,
    'state':'Punjab',
    'capital':'Chandigarh',
    'language':'Punjabi',
    },
   {'id':21,
    'state':'Rajasthan',
    'capital':'Jaipur',
    'language':'Rajasthan and Hindi',
    },
   {'id':22,
    'state':'Sikkim',
    'capital':'Gangtok',
    'language':'% languages!',
    },
   {'id':23,
    'state':'Tamil Nadu',
    'capital':'Chennai',
    'language':'Tamil',
    },
   {'id':24,
    'state':'Tripura',
    'capital':'Agartala',
    'language':'4 languages!',
    },
   {'id':25,
    'state':'Telangana',
    'capital':'Hyderabad',
    'language':'Telugu',
    },
   {'id':26,
    'state':'Uttart Pradesh',
    'capital':'Lucknow',
    'language':'Hindi',
    },
   {'id':27,
    'state':'Uttarakhand',
    'capital':'Dehradun',
    'language':'Hindi/Garhwali',
    },
   {'id':28,
    'state':'West Bengal',
    'capital':'Kolkata',
    'language':'Bengali',
    },
   {'id':29,
    'state':'Jammu and Kashmir',
    'capital':'Jammu,Srinagar',
    'language':'Hindi,Dogri',
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1><strong>STATE DATA</strong></h1>
<p>A simple REST-API that returns indian states,their capital and language.Hope you like it!
</p>'''


@app.route('/api/states/all', methods=['GET'])
def api_all():
    return jsonify(states)


@app.route('/api/states', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
       
    results = ['EMPTYT!!']

    for state in states:
        if state['id'] == id:
            results.append(state)
    return jsonify(results)

app.run()
