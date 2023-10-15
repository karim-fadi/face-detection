# Importing Libraries
import os
import cv2
from facenet_pytorch import MTCNN
from PIL import Image
import argparse

# Handling Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", type=str, required=False)
parser.add_argument("-p", "--photo", type=str)
args = parser.parse_args()

mode = "webcam"
if args.mode == "webcam" or args.mode == "photo":
    mode = args.mode

photo_path = args.photo

num_faces = 0

# Initializing MTCNN
mtcnn = MTCNN(image_size=240, margin=0, keep_all=True, min_face_size=40)

cam = cv2.VideoCapture(0) 

if mode == "webcam":
    while True:
        ret, frame = cam.read()

        frame = cv2.flip(frame, 1)

        if not ret:
            print("Failed To Access Webcam !")
            break
            
        img = Image.fromarray(frame)
        img_cropped_list, prob_list = mtcnn(img, return_prob=True) 
        
        if img_cropped_list is not None:
            boxes, _ = mtcnn.detect(img)
            num_faces = len(_)
                    
            for i, prob in enumerate(list(prob_list)):
                if prob > 0.90:
                    box = boxes[i]
                    
                    frame = cv2.rectangle(frame, (int(box[0]), int(box[1])) , (int(box[2]), int(box[3])), (255 , 0, 0), 2)

                    label = "Number of Faces Detected: " + str(num_faces)
                    cv2.putText(frame, label, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)
            
        key = cv2.waitKey(1)

        if key == 27: # Escape Key
            break

elif mode == "photo":
    try: 
        if os.path.exists(photo_path) == True:
            print("Reading Photo...")
            img = cv2.imread(photo_path)

            img_cropped_list, prob_list = mtcnn(img, return_prob=True) 

            if img_cropped_list is not None:
                print("Detecting Faces...")
                boxes, _ = mtcnn.detect(img)
                        
                for i, prob in enumerate(list(prob_list)):
                    if prob > 0.9:
                        
                        box = boxes[i]
                        
                        cv2.rectangle(img, (int(box[0]), int(box[1])) , (int(box[2]), int(box[3])), (255 , 0, 0), 3)

                        cv2.imwrite("Result.jpg", img)
                        num_faces += 1

            print("Number of Faces Detected:", num_faces)
            print("Wrote Image at Result.jpg")

        else:
            print("Invalid Path to a Photo !")

    except:
        print("Invalid Path to a Photo !")

cam.release()
cv2.destroyAllWindows()