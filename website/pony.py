from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder='website', static_folder='images')

IMAGES_DIR = os.path.abspath('C:/Users/sanan/images')
print(f"IMAGES_DIR: {IMAGES_DIR}")

@app.route('/images/<filename>')
def serve_image(filename):
    image_path = os.path.join(IMAGES_DIR, filename)
    print(f"Requested image: {filename}, full path: {image_path}")
    return send_from_directory(IMAGES_DIR, filename)

IMAGE_FILENAMES = {
    0: ['3.1.png', '3.2.png', '3.3.png', '3.4.png', '3.5.png'],
    1: ['8.1.png', '8.2.png', '8.3.png', '8.4.png', '8.5.png'],
    2: ['13.1.png', '13.2.png', '13.3.png', '13.4.png', '13.5.png'],
    3: ['24.1.png', '24.2.png', '24.3.png', '24.4.png', '24.5.png'],
    4: ['35.1.png', '35.2.png', '35.3.png', '35.4.png', '35.5.png'],
    5: ['37.1.png', '37.2.png', '37.3.png', '37.4.png', '37.5.png']
}

def get_points_from_list():
    return [
        {'lat': 29.588923, 'lon': -95.121474},
        {'lat': 29.972433, 'lon': -95.402044},
        {'lat': 29.973457, 'lon': -95.39556},
        {'lat': 29.652162, 'lon': -95.135733},
        {'lat': 29.966124, 'lon': -95.582761},
        {'lat': 29.524217, 'lon': -95.51683}
    ]

def generate_dems(lat, lon):
    points = get_points_from_list()
    index = next((i for i, p in enumerate(points) if p['lat'] == lat and p['lon'] == lon), None)
    
    print(f"Index found: {index}")

    if index is not None and index in IMAGE_FILENAMES:
        filenames = IMAGE_FILENAMES[index]
        dem_paths = [f"/images/{filename}" for filename in filenames]
        print(f"Generated DEM paths: {dem_paths}")
        return dem_paths
    return []

@app.route('/')
def home():
    aoi_points = get_points_from_list()
    return render_template('index2.html', aoi_points=aoi_points)

@app.route('/directions')
def directions():
    return render_template('directions.html')

@app.route('/confirm_aoi', methods=['POST'])
def confirm_aoi():
    selected_points = request.json['points']
    if selected_points:
        lat = selected_points[0]['lat']
        lon = selected_points[0]['lon']
        dem_paths = generate_dems(lat, lon)
        print(f"DEM paths: {dem_paths}")
        return jsonify({'success': True, 'dem_paths': dem_paths})
    return jsonify({'success': False})

@app.route('/dem_model')
def dem_model():
    dem_paths = request.args.getlist('dem_path')
    print(f"Dem paths received: {dem_paths}")
    return render_template('dem_model.html', dem_paths=dem_paths)

if __name__ == '__main__':
    app.run(debug=True)
