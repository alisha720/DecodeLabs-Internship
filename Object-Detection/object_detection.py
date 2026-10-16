import cv2
import numpy as np

# Load the MobileNet-SSD model
prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"

net = cv2.dnn.readNetFromCaffe(prototxt, model)

# Object labels
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

# Select an image
image_path = input("Enter image path: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found. Check the image path.")
    raise SystemExit

height, width = image.shape[:2]

# Prepare image for the model
blob = cv2.dnn.blobFromImage(
    cv2.resize(image, (300, 300)),
    0.007843,
    (300, 300),
    127.5
)

net.setInput(blob)
detections = net.forward()

# Draw detections with confidence >= 80%
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence >= 0.80:
        class_id = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array(
            [width, height, width, height]
        )

        x1, y1, x2, y2 = box.astype("int")
        label = CLASSES[class_id]
        text = f"{label}: {confidence * 100:.1f}%"

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            image, text, (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
        )

        print(text)

# Display and save the result
cv2.imshow("Object Detection", image)
cv2.imwrite("detected_output.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()