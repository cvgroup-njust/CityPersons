The models are trained on the training set.
The test.prototxt and config file are also provided.

The model "vgg16_faster_rcnn_train_1x.caffemodel" is trained with input image scale of 1.0, which should give you a MR(Reasonable) of 15.14% on the validation set;
the model "vgg16_faster_rcnn_train_1.3x.caffemodel" is trained with input image scale of 1.3, which should give you a MR(Reasonable) of 12.81% on the validation set.
The reported numbers are from tests with the same scale as training time.
Please note the 1x model runs ~2x faster than the 1.3x model.

The models are available in the Google Drive (https://github.com/myding-njust/citypersons/tree/master/annotations/?at=default).
