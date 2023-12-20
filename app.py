# import sys,os
# from changeSegmentation.pipeline.training_pipeline import TrainPipeline
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask import Flask, request, jsonify, render_template,Response
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
#
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#
#
# @app.route("/train")
# def trainRoute():
#     obj = TrainPipeline()
#     obj.run_pipeline()
#     return "Training Successfull!!"
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/predict",methods = ['POST','GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         decodeImage(image,clApp.filename)
#         os.system("yolo task=segment mode=predict model= artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")
#         opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
#         result = {"image": opencodebase64.decode('utf-8')}
#         os.system("rm -rf runs")
#
#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside json data")
#     except KeyError:
#         return Response("Key value error incorrect key passed")
#
#     except Exception as e:
#         print(e)
#         result = "invalid input"
#
#     return jsonify(result)
#
# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host=APP_HOST,port = APP_PORT)
#     app.run(host='0.0.0.0',port=

# import os
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
#
# app = Flask(__name__)
# CORS(app)
#
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#
# # Your existing routes...
# @app.route("/")
# def home():
#     return render_template("index.html")
# @app.route("/predict", methods=['POST', 'GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         decodeImage(image, clApp.filename)
#
#         # Check if the file already exists
#         if os.path.exists("data/inputImage.jpg"):
#             os.remove("data/inputImage.jpg")
#
#         # Move the newly uploaded image to the data folder
#         os.rename(clApp.filename, os.path.join("data", clApp.filename))
#
#         os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")
#
#         # Encode the result image to base64
#         opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
#
#         # Create the result dictionary
#         result = {"image": opencodebase64.decode('utf-8')}
#
#         # Remove the temporary files and folders
#         os.system("rm -rf runs")
#         os.remove("data/inputImage.jpg")
#
#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside JSON data")
#     except KeyError:
#         return Response("Key value error: incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"
#
#     return jsonify(result)
#
# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host='0.0.0.0', port=80)


# import os
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#
# # Your existing routes...
# @app.route("/")
# def home():
#     return render_template("index.html")
# @app.route("/predict", methods=['POST', 'GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         decodeImage(image, clApp.filename)
#
#         # Check if the file already exists
#         print("Checking if the file already exists")
#         # if os.path.exists("data\\inputImage.jpg"):
#         #     print("File already exists so deleting it")
#         #     os.remove("data\\inputImage.jpg")
#
#         # Move the newly uploaded image to the data folder
#         print("Moving the newly uploaded image to the data folder")
#         os.rename(clApp.filename, os.path.join("data", clApp.filename))
#
#         if os.path.exists("data\inputImage.jpg"):
#             print("suck cess")
#         else:
#             print("not suck cess")
#
#         print("Running the yolo command")
#         os.system("yolo task=segment mode=predict model=artifacts\\model_trainer\\best.pt conf=0.25 source=data\\inputImage.jpg save=true")
#
#         # Encode the result image to base64
#         print("Encoding the result image to base64")
#         opencodebase64 = encodeImageIntoBase64("runs\\segment\\predict\\inputImage.jpg")
#
#         # Create the result dictionary
#         print("Creating the result dictionary")
#         result = {"image": opencodebase64.decode('utf-8')}
#
#         # Remove the temporary files and folders
#         print("Removing the temporary files and folders")
#         os.system("rmdir /s /q runs")
#         os.remove("data\\inputImage.jpg")
#
#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside JSON data")
#     except KeyError:
#         return Response("Key value error: incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"
#
#     return jsonify(result)
#
# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host=APP_HOST,port = APP_PORT)


# import os
# from ultralytics import YOLO
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
# import base64
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
# #
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         print(type(image))
#
#         image=image['data']
#         print(type(image))
#         print(len(image))
#
#         image=bytes(image)
#         image=base64.b64encode(image).decode('utf-8')
#         clApp = ClientApp()
#         print("Checking if image already exists")
#         if os.path.exists("data/inputImage.jpg"):
#             print("Removing because it exists")
#             os.remove("data/inputImage.jpg")
#
#         # Save the image to the data folder with the name inputImage.jpg
#         print("decoding and saving")
#         decodeImage(image, clApp.filename)
#
#         print("Running the yolo command")
#         model = YOLO("artifacts/model_trainer/best.pt")
#         arr = model.predict(source = "data/inputImage.jpg",conf=0.4,save=True)
#         # os.system("yolo task=segment mode=predict model= artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")
#
#         # Encode the result image to base64
#         print("Encoding the result image to base64")
#         opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
#
#         # Create the result dictionary
#         print("Creating the result dictionary")
#         result = {"image": opencodebase64.decode('utf-8')}
#         # print(result)
#
#
#         # Remove the temporary files and folders
#         print("Removing the temporary files and folders")
#         os.system("rm -rf runs")
#         os.remove("data/inputImage.jpg")
#
#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside JSON data")
#     except KeyError:
#         return Response("Key value error: incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"
#
#     print(len(result))
#     print(arr[0].box.cls)
#     print("jkdj")
#     return jsonify(result,arr[0].box.cls)
#
# if __name__ == "__main__":
#     app.run(host=APP_HOST, port=APP_PORT)
#
# #
# # # ... (existing code)
# #
#
#
# import os
# from ultralytics import YOLO
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
# import base64
# import cv2
# import numpy as np
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
# #
# @app.route("/")
# def home():rt os
# from ultralytics import YOLO
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
# import base64
# import cv2
# import numpy as np
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.j
#     return render_template("index.html")
#
# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         print(type(image))
#
#         image=image['data']
#         print(type(image))
#         print(len(image))
#
#         image=bytes(image)
#         image=base64.b64encode(image).decode('utf-8')
#         clApp = ClientApp()
#         print("Checking if image already exists")
#         if os.path.exists("data/inputImage.jpg"):
#             print("Removing because it exists")
#             os.remove("data/inputImage.jpg")
#
#         # Save the image to the data folder with the name inputImage.jpg
#         print("decoding and saving")
#         decodeImage(image, clApp.filename)
#
#         print("Running the yolo command")
#         # os.system("yolo task=segment mode=predict model= artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")
#         model = YOLO("artifacts/model_trainer/best.pt")
#         arr = model.predict(source="data/inputImage.jpg", conf=0.50,save=True)
#         # Encode the result image to base64
#         print("Encoding the result image to base64")
#         opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
#
#         # print(opencodebase64)
#         # Create the result dictionary
#         print("Creating the result dictionary")
#         result = {"image": opencodebase64.decode('utf-8')}
#         # print(result)
#
#         print(len(arr))
#         print(type(arr))
#         print(type(arr[0]))
#
#         # print()
#         # print(arr[0].boxes)
#         # print(arr[0].boxes.cls.numpy())
#         # print(arr[0].boxes.conf.numpy())
#         # print(arr[0].boxes.data.numpy())
#
#         responseObj={
#             "result":opencodebase64.decode('utf-8'),
#             "classes":arr[0].boxes.cls.tolist(),
#             "confidenceScore":arr[0].boxes.conf.tolist(),
#             "data":arr[0].boxes.data.tolist()
#         }
#
#         # print(responseObj)
#
#         # Remove the temporary files and folders
#         print("Removing the temporary files and folders")
#         os.system("rm -rf runs")
#         os.remove("data/inputImage.jpg")
#
#
#         return jsonify(responseObj)
#
#     except ValueError as val:
#
#         print(val)
#
#         return jsonify({"error": "Value not found inside JSON data"})
#
#     except KeyError:
#
#         return jsonify({"error": "Key value error: incorrect key passed"})
#
#     except Exception as e:
#
#         print(e)
#
#         return jsonify({"error": "Invalid input"})
#
# def resize_image(image, target_size):
#     target_size = (max(target_size[0], 3), max(target_size[1], 3))
#     return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
#
# def generate_heatmap(image1, image2):
#     # Convert images to grayscale
#     target_size = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
#     image1_resized = resize_image(image1, target_size)
#     image2_resized = resize_image(image2, target_size)
#
#     gray1 = cv2.cvtColor(image1_resized, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)
#
#     # Compute absolute difference
#     diff = cv2.absdiff(gray1, gray2)
#
#     # Apply a colormap for visualization
#     heatmap_color = cv2.applyColorMap(diff, cv2.COLORMAP_JET)
#
#     # Convert the heatmap to grayscale
#     heatmap_gray = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2GRAY)
#
#     return heatmap_gray
#
# @app.route('/generate_heatmap', methods=['POST'])
# def generate_heatmap_api():
#     try:
#         # Assuming images are sent as base64-encoded strings in JSON payload
#         image1_base64 = request.json['image1']
#         image2_base64 = request.json['image2']
#
#         # Decode base64 strings to bytes
#         image1_bytes = base64.b64decode(image1_base64)
#         image2_bytes = base64.b64decode(image2_base64)
#
#         # Convert bytes to image objects
#         image1 = cv2.imdecode(np.frombuffer(image1_bytes, np.uint8), cv2.IMREAD_COLOR)
#         image2 = cv2.imdecode(np.frombuffer(image2_bytes, np.uint8), cv2.IMREAD_COLOR)
#
#         # Generate the black and white heatmap
#         heatmap_bw = generate_heatmap(image1, image2)
#
#         # Save the heatmap to a file or convert to base64 and return
#         _, heatmap_encoded = cv2.imencode('.png', heatmap_bw)
#         heatmap_base64 = base64.b64encode(heatmap_encoded).decode('utf-8')
#
#         return jsonify({'heatmap': heatmap_base64})
#
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
# if __name__== "__main__":
#     app.run(host=APP_HOST, port=APP_PORT)


# import os
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
# import time
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#
# # Your existing routes...
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/predict", methods=['POST', 'GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         clApp = ClientApp()
#
#         # Save the image to the data folder with the name inputImage.jpg
#         print("decoding and saving")
#         decodeImage(image, clApp.filename)
#         # give code to count the time it took to run the yolo
#         x = time.time()
#         print("Running the yolo command")
#         os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.15 source=data/inputImage.jpg save=true")
#
#         # Encode the result image to base64
#         print("Encoding the result image to base64")
#         opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
#
#         # Create the result dictionary
#         print("Creating the result dictionary")
#         result = {"image": opencodebase64.decode('utf-8')}
#         y = time.time()
#         print("Time taken to run yolo: ", y - x)
#         # Remove the temporary files and folders
#         print("Removing the temporary files and folders")
#         os.system("rm -rf runs")
#         os.remove("data/inputImage.jpg")
#
#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside JSON data")
#     except KeyError:
#         return Response("Key value error: incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"
#
#     return jsonify(result)
#
# if __name__ == "__main__":
#     app.run(host=APP_HOST, port=APP_PORT)

# import os
# from ultralytics import YOLO
# from flask import Flask, request, jsonify, render_template, Response
# from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask_cors import CORS, cross_origin
# from changeSegmentation.constant.application import APP_HOST, APP_PORT
# import base64
#
# app = Flask(__name__)
# CORS(app)
#
# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
# #
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     try:
#
#
#         image = request.json['image']
#         print(type(image))
#
#         image=image['data']
#         print(type(image))
#         print(len(image))
#
#         image=bytes(image)
#         image=base64.b64encode(image).decode('utf-8')
#         clApp = ClientApp()
#         print("Checking if image already exists")
#         if os.path.exists("data/inputImage.jpg"):
#             print("Removing because it exists")
#             os.remove("data/inputImage.jpg")
#
#         # Save the image to the data folder with the name inputImage.jpg
#         print("decoding and saving")
#         decodeImage(image, clApp.filename)
#
#         print("Running the yolo command")
#         # os.system("yolo task=segment mode=predict model= artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")
#         model = YOLO("artifacts/model_trainer/best.pt")
#         arr = model.predict(source="data/inputImage.jpg", conf=0.50,save=True)
#         # Encode the result image to base64
#         print("Encoding the result image to base64")
#         opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
#
#         # print(opencodebase64)
#         # Create the result dictionary
#         print("Creating the result dictionary")
#         result = {"image": opencodebase64.decode('utf-8')}
#         # print(result)
#
#         print(len(arr))
#         print(type(arr))
#         print(type(arr[0]))
#
#         # print()
#         # print(arr[0].boxes)
#         # print(arr[0].boxes.cls.numpy())
#         # print(arr[0].boxes.conf.numpy())
#         # print(arr[0].boxes.data.numpy())
#
#         responseObj={
#             "result":opencodebase64.decode('utf-8'),
#             "classes":arr[0].boxes.cls.tolist(),
#             "confidenceScore":arr[0].boxes.conf.tolist(),
#             "data":arr[0].boxes.data.tolist()
#         }
#
#         # print(responseObj)
#
#         # Remove the temporary files and folders
#         print("Removing the temporary files and folders")
#         os.system("rm -rf runs")
#         os.remove("data/inputImage.jpg")
#
#
#         return jsonify(responseObj)
#
#     except ValueError as val:
#
#         print(val)
#
#         return jsonify({"error": "Value not found inside JSON data"})
#
#     except KeyError:
#
#         return jsonify({"error": "Key value error: incorrect key passed"})
#
#     except Exception as e:
#
#         print(e)
#
#         return jsonify({"error": "Invalid input"})
#
#
# if __name__== "__main__":
#     app.run(host=APP_HOST, port=APP_PORT)



# ----------------------------------------------------------------------------------------------------------------------------------------------


import os
from flask import Flask, request, jsonify, render_template, Response
from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask_cors import CORS, cross_origin
from changeSegmentation.constant.application import APP_HOST, APP_PORT
import time
import cv2
import io
import base64
import numpy as np

app = Flask(__name__)
CORS(app)


def resize_image(image, target_size):
    target_size = (max(target_size[0], 3), max(target_size[1], 3))
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


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


# Your existing routes...
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        clApp = ClientApp()

        # Save the image to the data folder with the name inputImage.jpg
        print("decoding and saving")
        decodeImage(image, clApp.filename)
        # give code to count the time it took to run the yolo
        x = time.time()
        print("Running the yolo command")
        os.system(
            "yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.15 source=data/inputImage.jpg save=true")

        # Encode the result image to base64
        print("Encoding the result image to base64")
        opencodebase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")

        # Create the result dictionary
        print("Creating the result dictionary")
        result = {"image": opencodebase64.decode('utf-8')}
        y = time.time()
        print("Time taken to run yolo: ", y - x)
        # Remove the temporary files and folders
        print("Removing the temporary files and folders")
        os.system("rm -rf runs")
        os.remove("data/inputImage.jpg")

    except ValueError as val:
        print(val)
        return Response("Value not found inside JSON data")
    except KeyError:
        return Response("Key value error: incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


@app.route('/generate_heatmap', methods=['POST'])
def generate_heatmap_api():
    try:
        # Assuming images are sent as files with names 'image1' and 'image2'
        image1_file = request.files['image1']
        image2_file = request.files['image2']

        # Read images from file objects
        image1 = cv2.imdecode(np.frombuffer(image1_file.read(), np.uint8), cv2.IMREAD_COLOR)
        image2 = cv2.imdecode(np.frombuffer(image2_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Generate the black and white heatmap
        heatmap_bw = generate_heatmap(image1, image2)

        # Save the heatmap to a file or convert to base64 and return
        _, heatmap_encoded = cv2.imencode('.png', heatmap_bw)
        heatmap_base64 = base64.b64encode(heatmap_encoded).decode('utf-8')

        return jsonify({'heatmap': heatmap_base64})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)