import cv2
import numpy as np

# Load the YOLOv3 model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Get the names of the model's output layers
output_layers = net.getUnconnectedOutLayersNames()

# Set the input image
img = cv2.imread("path/to/image.jpg")
height, width, channels = img.shape

# Prepare the input blob
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# Set the blob as the input to the model
net.setInput(blob)

# Get the output from the model
outputs = net.forward(output_layers)

# Initialize lists for the bounding boxes, confidences, and class IDs
boxes = []
confidences = []
class_ids = []

# Loop over each output in the model's output layers
for output in outputs:
    # Loop over each detection in the output
    for detection in output:
        # Extract the class ID and confidence score
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        # Filter out weak detections
        if confidence > 0.5:
            # Convert the center coordinates from relative to absolute
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)

            # Convert the width and height from relative to absolute
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Calculate the top left corner of the bounding box
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # Add the bounding box, confidence score, and class ID to their respective lists
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-max suppression to remove redundant bounding boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw the bounding boxes on the image
for i in indices:
    i = i[0]
    box = boxes[i]
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show the image
cv2.imshow("Object Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()