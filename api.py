import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
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


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
       

    # Create an empty list for our results
    results = ['EMPTYT!!']

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
