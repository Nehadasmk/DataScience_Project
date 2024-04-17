
from flask import Flask, render_template, url_for, request, redirect
from caption import *
import warnings
import base64
warnings.filterwarnings("ignore")



app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('camera.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img =request.json['image']
		# print(img)
		# print(img.filename)
		#app.logger.info("test"+type(img))
		convert_and_save(img)

		#img.save("static/"+img.filename)

	
		#caption = caption_this_image("static/"+img.filename)



		
		#result_dic = {
			#'image' : "static/" + img.filename,
			#'description' : caption
		#}
	return render_template('camera.html')
	#return render_template('camera.html', results = result_dic)
def convert_and_save(b64_string):
    with open("static/imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(b64_string))


if __name__ == '__main__':
	app.run(debug = True)