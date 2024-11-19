# Constellation Explorer API
from flask import Flask, request, jsonify, request, redirect
import requests

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
def get_constellation_by_name(name):
        for constellation in constellations:
            if constellation["name"].lower() == name.lower():
                return jsonify(constellation)

# 3. Add a new constellation
# POST /constellations, JSON body contains the constellation details
@app.route('/constellations', methods=['POST'])
def add_constellation():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Invalid input"}), 400
    new_constellation = {
        "name": request.json['name'],
        "stars": request.json.get('stars', [])
    }
    constellations.append(new_constellation)
    return jsonify(new_constellation), 201



# 4. Delete a constellation
@app.route('/constellations/<name>', methods=['DELETE'])
def delete_constellation(name):
    for constellation in constellations:
        if constellation["name"].lower() == name.lower():
            constellations.remove(constellation)
            return jsonify({"result": True})
    return jsonify([])

# 5. Filter constellations by hemisphere and area (Query String)
@app.route('/constellations/filter', methods=['GET'])
def filter_constellations():
    result = constellations
    if 'hemisphere' in request.args:
        hemisphere = request.args['hemisphere']
        result = [constellation for constellation in result if constellation['hemisphere'].lower() == hemisphere.lower()]
    if 'area' in request.args:
        try:
            area = int(request.args['area'])
            result = [constellation for constellation in result if constellation['area'] > area]
        except ValueError:
            return jsonify({"error": "Invalid area value"}), 400
    return jsonify(result)

# 6. View the main stars of a constellation specified by name
@app.route('/constellations/<name>/stars', methods=['GET'])
def get_main_stars(name):
    for constellation in constellations:
        if constellation["name"].lower() == name.lower():
            return jsonify(constellation.get('main_stars', []))
    return jsonify([])

# 7. Partially update a constellation specified by name
@app.route('/constellations/<name>', methods=['PATCH'])
def update_constellation(name):
    for constellation in constellations:
        if constellation["name"].lower() == name.lower():
            constellation.update(request.json)
            return jsonify(constellation)

# 8. For a constellation specified by name, view the image
# You might have to use an image generator API - try https://imagepig.com/

@app.route('/constellations/<name>/image', methods=['GET'])
def get_constellation_image(name):
    api_url = "https://api.imagepig.com/v1/images"  # Updated URL for image generation

    api_key = "4de1176d-7ca1-4465-8d09-01908c3b9eb7"  # Replace with your actual API key

    # Check if constellation exists in the list
    for constellation in constellations:
        if constellation["name"].lower() == name.lower():
            try:
                # Make a request to the ImagePig API
                response = requests.post(  # Changed GET to POST as per ImagePig documentation
                    api_url,
                    json={"prompt": f"{name} constellation"},  # Updated data format
                    headers={"Authorization": f"Bearer {api_key}"}
                )

                # Debugging logs (optional)
                # print("Status Code:", response.status_code)
                # print("Headers:", response.headers)
                # print("Response Text:", response.text)

                # Check the API response
                if response.status_code == 200:
                    # Parse JSON response (might need adjustment based on ImagePig's response format)
                    image_data = response.json()
                    image_url = image_data.get("url")  # Assuming "url" key holds the image URL
                    if image_url:
                        return jsonify({"image_url": image_url})
                    else:
                        return jsonify({"error": "Image URL not found in response"}), 500
                else:
                    return jsonify({"error": f"API error: {response.status_code} - {response.text}"}), response.status_code
            except requests.exceptions.RequestException as e:
                return jsonify({"error": f"Request failed: {str(e)}"}), 500

    # If no matching constellation is found
    return jsonify({"error": "Constellation not found"}), 404

# 9. Add your own! Try to use query strings or path parameters.
@app.route('/constellations/area', methods=['GET'])
def get_constellation_area():
    result = []
    if 'area' in request.args:
        try:
            area = int(request.args['area'])
            result = [constellation for constellation in constellations if constellation['area'] > area]
        except ValueError:
            return jsonify({"error": "Invalid area value"}), 400
    return jsonify(result)

# 10. Double check that all the endpoints return the appropriate status codes.
# For errors, display the status code using an HTTP Cat - https://http.cat/
@app.errorhandler(404)
def not_found_error(error):
    return redirect("https://http.cat/404")

if __name__ == '__main__':
    app.run(debug=True)