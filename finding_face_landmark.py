import sys
import dlib
from skimage import io

# You can download the required pre-trained face detection model here:
# Training model with shape_prodictor_68_face_landmarks.dat"
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Load hinh anh tu thu muc
file_name = "ro.jpg" 

# Tao HOG voi dlib
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)

win = dlib.image_window()

# Load image
file_name = "ro.jpg"
image = io.imread(file_name)

# Chay HOG face detector on the image data
detected_faces = face_detector(image, 1)

#Xuat ra nhung khuon mat nhan dien duoc
print("Found {} faces in the image file {}".format(len(detected_faces), file_name))

# Output
win.set_image(image)

# Voi moi khuon mat, tim cac vi tri 
for i, face_rect in enumerate(detected_faces):
	# Xuat cac vi tri
	print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
	#win.add_overlay(face_rect)
	pose_landmarks = face_pose_predictor(image, face_rect)
	
	win.add_overlay(pose_landmarks)
	        
dlib.hit_enter_to_continue()