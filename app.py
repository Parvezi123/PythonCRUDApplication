from movies import *

#Display All Movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movie.get_all_movies()})

#Display movie By ID
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

# route to add new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    Movie.add_movie(request_data["title"], request_data["year"],
                    request_data["genre"])
    response = Response("Movie added", 201, mimetype='application/json')
    return response

# route to update movie with PUT method
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'],                                      request_data['genre'])
    response = Response("Movie Updated", status=200, mimetype='application/json')
    return response

# route to delete movie using the DELETE method
@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete movie from our database'''
    Movie.delete_movie(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response

# Dummy method to display
@app.route('/', methods=['GET'])
def displayMessage():
    return "<h1><br> <br> <br> <br> <br> <br> <br> <center>  S  H  I  T &nbsp; &nbsp; &nbsp;  API  -  Not at root level ... </centre> </h1>"

# Dummy method to display
@app.route('/1', methods=['GET'])
def displayMessage1():
    return "<h1><br> <br> <br> <br> <br> <br> <br> <center>  <big><big>S</big></big><small>orry</small>  <big><big>H</big></big><small>it</small>  <big><big>I</big></big><small>n</small>  <big><big>T</big></big><small>he</small> &nbsp; &nbsp; &nbsp;  API  -  Not at root level ... </centre> </h1>"

if __name__ == "__main__":
    app.run(port=1234, debug=True)