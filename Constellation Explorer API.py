# Constellation Explorer API
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample constellation data
constellations = [
    {'id': 1, 'name': 'Orion', 'hemisphere': 'Northern', 'main_stars': ['Betelgeuse', 'Rigel', 'Bellatrix'], 'area': 594, 'origin': 'Greek'},
    {'id': 2, 'name': 'Scorpius', 'hemisphere': 'Southern', 'main_stars': ['Antares', 'Shaula', 'Sargas'], 'area': 497, 'origin': 'Greek'},
    {'id': 3, 'name': 'Ursa Major', 'hemisphere': 'Northern', 'main_stars': ['Dubhe', 'Merak', 'Phecda'], 'area': 1280, 'origin': 'Greek'},
    {'id': 4, 'name': 'Cassiopeia', 'hemisphere': 'Northern', 'main_stars': ['Schedar', 'Caph', 'Ruchbah'], 'area': 598, 'origin': 'Greek'},
    {'id': 5, 'name': 'Crux', 'hemisphere': 'Southern', 'main_stars': ['Acrux', 'Mimosa', 'Gacrux'], 'area': 68, 'origin': 'Latin'},
    {'id': 6, 'name': 'Lyra', 'hemisphere': 'Northern', 'main_stars': ['Vega', 'Sheliak', 'Sulafat'], 'area': 286, 'origin': 'Greek'},
    {'id': 7, 'name': 'Aquarius', 'hemisphere': 'Southern', 'main_stars': ['Sadalsuud', 'Sadalmelik', 'Sadachbia'], 'area': 980, 'origin': 'Babylonian'},
    {'id': 8, 'name': 'Andromeda', 'hemisphere': 'Northern', 'main_stars': ['Alpheratz', 'Mirach', 'Almach'], 'area': 722, 'origin': 'Greek'},
    {'id': 9, 'name': 'Pegasus', 'hemisphere': 'Northern', 'main_stars': ['Markab', 'Scheat', 'Algenib'], 'area': 1121, 'origin': 'Greek'},
    {'id': 10, 'name': 'Sagittarius', 'hemisphere': 'Southern', 'main_stars': ['Kaus Australis', 'Nunki', 'Ascella'], 'area': 867, 'origin': 'Greek'}
]

# The first endpoint is completed for your reference. Some endpoints have hints,
# and you must complete the others from scratch. Use principles of Uniform Interface.

# 1. View all constellations
# GET /constellations
@app.route('/constellations', methods=['GET'])
def get_all_constellations():
    return jsonify(constellations)

# 2. View a specific constellation by name
# GET /constellations/<name> (Path Parameter)
@app.route('/constellations/<name>', methods=['GET'])
def get_constellation(name):
    # Add code to get the corresponding constellation
    return jsonify([])

# 3. Add a new constellation
# POST /constellations, JSON body contains the constellation details

# 4. Delete a constellation

# 5. Filter constellations by hemisphere and area (Query String)

# 6. View the main stars of a constellation specified by name

# 7. Partially update a constellation specified by name

# 8. For a constellation specified by name, view the image
# You might have to use an image generator API - try https://imagepig.com/

# 9. Add your own! Try to use query strings or path parameters.

# 10. Double check that all the endpoints return the appropriate status codes.
# For errors, display the status code using an HTTP Cat - https://http.cat/

if __name__ == '__main__':
    app.run(debug=True)