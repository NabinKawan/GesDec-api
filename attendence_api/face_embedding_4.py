
# calculate a face embedding for each face in the dataset using facenet
from numpy import expand_dims
from tensorflow.python.keras.models import load_model
MODEL = load_model('attendence_api/model_files/facenet_keras.h5')
# get the face embedding for one face
def get_embedding( face_pixels, model=MODEL):
	# scale pixel values
	face_pixels = face_pixels.astype('float32')
	# standardize pixel values across channels (global)
	mean, std = face_pixels.mean(), face_pixels.std()
	face_pixels = (face_pixels - mean) / std
	# transform face into one sample
	samples = expand_dims(face_pixels, axis=0)
	# make prediction to get embedding
	yhat = model.predict(samples)
	return yhat[0]
 
if __name__ == '__main__':
	print("hi")