# Face Detection

# Installation
* `pip install opencv-python facenet-pytorch`

# Usage
You can detect faces using a webcam or in a photo. By default, if you run the file like this:

`python Face Detection.py`

It will open your webcam and detect faces in a live video stream.

If you want to detect faces and count them in a photo, just set the `-m` or ``--mode`` flags to "photo", and the `-p` or `--photo` flags to the photo path.

`python Face Detection.py --mode photo --photo ./Test.jpg`
