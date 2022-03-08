from numpy import expand_dims
from attendence_api.face_embedding_4 import get_embedding
import pickle
from attendence_api.load_dataset_2 import extract_face

DATASET_DICT = 'attendence_api/model_files/dataset_dect.json'
model_location = 'attendence_api/model_files/model1.pkl'

def predict(input_img):
    load_face = extract_face(input_img)
    embedded_face = get_embedding(load_face)
    samples = expand_dims(embedded_face, axis=0)
    model = load_model()
    yhat_class = model.predict(input_img)
    return yhat_class[0]

# def get_name(yhat_class):
#     with open(DATASET_DICT, 'r') as f:
#         dataset_dict = json.load(f)
#     predict_class =  str(yhat_class[0])
#     predict_name = dataset_dict[predict_class]
#     return(predict_name)

def load_model():
    with open(model_location,'rb') as f:
        models = pickle.load(f)
        return models

