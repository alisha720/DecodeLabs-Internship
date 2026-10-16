Object Detection Using Python

Project Overview

This project detects objects in an image using Python and the MobileNet SSD deep learning model. It identifies objects and displays their labels with confidence scores and bounding boxes.

Features

- Detects objects in images.
- Displays object names and confidence scores.
- Draws bounding boxes around detected objects.
- Uses a pre-trained MobileNet SSD model.

Technologies Used

- Python
- OpenCV
- MobileNet SSD
- Deep Learning

Project Files

- "object_detection.py" – Python code for object detection.
- "MobileNetSSD_deploy.prototxt" – Model architecture configuration.
- "MobileNetSSD_deploy.caffemodel" – Pre-trained model weights.
- "test.image.png" – Input image used for detection.
- "object_detection_output.png" – Output image showing detected objects.

Requirements

Install Python and OpenCV before running the project.

Install OpenCV using:

pip install opencv-python

How to Run

1. Download or clone this repository.
2. Open the "Object-Detection" folder in VS Code.
3. Run the Python script:

python object_detection.py

4. Enter the input image path when prompted:

test.image.png

5. View the detected objects and their confidence scores.

Sample Output

The model successfully detected people in the test image with confidence scores such as 99.5% and 87.3%.

Learning Outcome

This project helped me understand image-based object detection, pre-trained deep learning models, and the use of OpenCV in computer vision.