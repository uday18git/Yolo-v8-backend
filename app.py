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


import os
from flask import Flask, request, jsonify, render_template, Response
from changeSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask_cors import CORS, cross_origin
from changeSegmentation.constant.application import APP_HOST, APP_PORT

app = Flask(__name__)
CORS(app)

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

        print("Running the yolo command")
        os.system("yolo task=segment mode=predict model=artifacts\\model_trainer\\best.pt conf=0.25 source=data\\inputImage.jpg save=true")

        # Encode the result image to base64
        print("Encoding the result image to base64")
        opencodebase64 = encodeImageIntoBase64("runs\\segment\\predict\\inputImage.jpg")

        # Create the result dictionary
        print("Creating the result dictionary")
        result = {"image": opencodebase64.decode('utf-8')}

        # Remove the temporary files and folders
        print("Removing the temporary files and folders")
        os.system("rmdir /s /q runs")
        os.remove("data\\inputImage.jpg")

    except ValueError as val:
        print(val)
        return Response("Value not found inside JSON data")
    except KeyError:
        return Response("Key value error: incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)

