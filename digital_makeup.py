from PIL import Image, ImageDraw
import face_recognition
import cv2

# Load anh tu thu muc
image = face_recognition.load_image_file("model3.jpg")

# Find all facial features in all the faces in the image
# Tim cac vi tri cua khuon mat
face_landmarks_list = face_recognition.face_landmarks(image)


# xu ly khuon mat
pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    #xu ly voi chan may
    #d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    #d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    #d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=3)
    #d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=3)

    # Xu ly voi moi
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Xu ly voi mat
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=5)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=5)
    # Xuat hinh anh
    #cv2.imwrite("nghia.jpg",d)
    pil_image.show()
    