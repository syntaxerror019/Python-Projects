import cv2

# Load the pre-trained face detection model YOu can use others too
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image_path = 'obama.jpg'
image = cv2.imread(image_path)
#Make it a grey scale image for later
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Do the stuff to process and sfjhlskfdk
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save or display the image with detected faces
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)

# Display the original and modified images
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Facees', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
