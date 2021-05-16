from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import tensorflow as tf
import os
import numpy as np
from PIL import Image as im

# loading our model
model = tf.keras.models.load_model('./aimodel/mymodel.h5')


@login_required(login_url='login')
def imageapp(request):
    if request.method == 'GET':
        return render(request, 'processor.html')


@login_required(login_url='login')
def imageprocess(request):
    if request.method == 'GET':
        return redirect('app')
    else:
        fileObj = request.FILES['dirtyPhoto']
        fs = FileSystemStorage()
        image_path = fs.save(fileObj.name, fileObj)
        image_path = '.' + fs.url(image_path)
        image_arr = []
        # reading image via image preprocessor.
        l_image = tf.keras.preprocessing.image.load_img(
            image_path, target_size=(256, 256))
        image_arr.append(tf.keras.preprocessing.image.img_to_array(l_image))
        m_image = np.array(image_arr, dtype=np.uint16)
        # using model to restore image.
        predict = model.predict(m_image)
        final_predict = predict[0]
        # Now convert the numpy image array into image file.
        data = tf.keras.preprocessing.image.array_to_img(final_predict)
        saving_path = "./media/processed_" + image_path.replace('./media/', '')
        data.save(saving_path)
        return render(request, 'output.html', {'restored_image': saving_path})

        # return render(request, 'output.html')

# ref
# answered Jul 29 '18 at 4:10 JPG
# https: // stackoverflow.com/questions/51576185/multivaluedictkeyerror-after-uploading-file

# https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
