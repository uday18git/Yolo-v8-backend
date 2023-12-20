# from flask import Flask, render_template, request, jsonify
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from io import BytesIO
# import base64
#
# app = Flask(__name__)
#
# def resize_image(image, target_size):
#     return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
#
# def generate_heatmap(image1, image2):
#     target_size = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
#     image1_resized = resize_image(image1, target_size)
#     image2_resized = resize_image(image2, target_size)
#
#     gray1 = cv2.cvtColor(image1_resized, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)
#
#     diff = cv2.absdiff(gray1, gray2)
#     heatmap_color = cv2.applyColorMap(diff, cv2.COLORMAP_JET)
#     heatmap_gray = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2GRAY)
#
#     return heatmap_gray
#
# @app.route('/')
# def index():
#     return render_template('index1.html')
#
# @app.route('/detect', methods=['POST'])
# def detect_changes():
#     image1 = cv2.imdecode(np.fromstring(request.files['image1'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
#     image2 = cv2.imdecode(np.fromstring(request.files['image2'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
#
#     heatmap_bw = generate_heatmap(image1, image2)
#
#     # Save the result image temporarily
#     result_path = 'static/images/result.jpg'
#     cv2.imwrite(result_path, heatmap_bw)
#
#     # Convert result image to base64 for displaying in HTML
#     with open(result_path, 'rb') as img_file:
#         result_base64 = base64.b64encode(img_file.read()).decode('utf-8')
#
#     return jsonify({'result_image': result_base64})
#
# if __name__ == '__main__':
#     app.run(debug=True,port=8081)
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from io import BytesIO
import base64

app = Flask(__name__)

def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

def generate_heatmap(image1, image2):
    target_size = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
    image1_resized = resize_image(image1, target_size)
    image2_resized = resize_image(image2, target_size)

    gray1 = cv2.cvtColor(image1_resized, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)
    heatmap_color = cv2.applyColorMap(diff, cv2.COLORMAP_VIRIDIS)
    heatmap_gray = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2GRAY)

    return heatmap_gray

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/detect', methods=['POST'])
def detect_changes():
    image1 = cv2.imdecode(np.fromstring(request.files['image1'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    image2 = cv2.imdecode(np.fromstring(request.files['image2'].read(), np.uint8), cv2.IMREAD_UNCHANGED)

    heatmap_bw = generate_heatmap(image1, image2)

    # Convert result image to base64 for displaying in HTML
    _, result_buffer = cv2.imencode('.jpg', heatmap_bw)
    result_base64 = base64.b64encode(result_buffer).decode('utf-8')

    return jsonify({'result_image': result_base64})

if __name__ == '__main__':
    app.run(debug=True,port=8081)

