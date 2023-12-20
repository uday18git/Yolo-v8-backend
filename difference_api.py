from flask import Flask, request, jsonify
import cv2
import numpy as np
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

def generate_heatmap(image1, image2):
    # Convert images to grayscale
    target_size = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
    image1_resized = resize_image(image1, target_size)
    image2_resized = resize_image(image2, target_size)

    gray1 = cv2.cvtColor(image1_resized, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)

    # Compute absolute difference
    diff = cv2.absdiff(gray1, gray2)

    # Apply a colormap for visualization
    heatmap_color = cv2.applyColorMap(diff, cv2.COLORMAP_JET)

    # Convert the heatmap to grayscale
    heatmap_gray = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2GRAY)

    return heatmap_gray

@app.route('/generate_heatmap', methods=['POST'])
def generate_heatmap_api():
    try:
        # Assuming images are sent as files with names 'image1' and 'image2'
        image1_file = request.files['image1']
        image2_file = request.files['image2']

        # Read images from file objects
        image1 = cv2.imdecode(np.fromstring(image1_file.read(), np.uint8), cv2.IMREAD_COLOR)
        image2 = cv2.imdecode(np.fromstring(image2_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Generate the black and white heatmap
        heatmap_bw = generate_heatmap(image1, image2)

        # Save the heatmap to a file or convert to base64 and return
        _, heatmap_encoded = cv2.imencode('.png', heatmap_bw)
        heatmap_base64 = base64.b64encode(heatmap_encoded).decode('utf-8')

        return jsonify({'heatmap': heatmap_base64})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)