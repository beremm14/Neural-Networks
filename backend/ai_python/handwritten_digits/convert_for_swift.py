import coremltools as ml
import os

def getHome():
    backend = os.path.dirname(os.getcwd())
    return os.path.dirname(backend)

output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
scale = 1/255.
coreml_model = ml.converters.keras.convert(getHome() + '/models/num_reader.h5',
                                                   input_names='image',
                                                   image_input_names='image',
                                                   output_names='output',
                                                   class_labels=output_labels,
                                                   image_scale=scale)

coreml_model.author = 'Emil Berger'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Model to predict handwritten digits'

coreml_model.input_description['image'] = '28x28 grayscale image of digit to predict'
coreml_model.output_description['output'] = 'Digit ASCII value (prediction)'

coreml_model.save(getHome() + "/models/num_reader.mlmodel")
