# Face Detection


My Python face detection project allows you to detect and count faces in both photos and live video streams.

# Installation
* `pip install opencv-python facenet-pytorch`

# Usage
You can detect faces using a webcam or in a photo. By default, if you run the file like this:

`python Face Detection.py`

It will open your webcam and detect faces in a live video stream.

If you want to detect faces and count them in a photo, just set the `-m` or ``--mode`` flags to "photo", and the `-p` or `--photo` flags to the photo path.

`python Face Detection.py --mode photo --photo ./Test.jpg`

# Example

Test Image:


![Test](https://github.com/karim-fadi/face-detection/assets/147660672/68c6e871-061a-4e6c-b165-c9531b7f5f5c)

Result:


![Result](https://github.com/karim-fadi/face-detection/assets/147660672/3a892c10-742a-4b8f-af8e-b48814bf6199)


![Screenshot 2023-10-20 135039](https://github.com/karim-fadi/face-detection/assets/147660672/3928dafd-5687-44be-a153-e09ea2c2074c)
