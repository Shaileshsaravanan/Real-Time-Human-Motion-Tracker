import cv2
import numpy as np
import argparse

def load_model(model_name):
    if model_name == "yolo":
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        with open("coco.names", "r") as f:
            classes = f.read().strip().split('\n')
    elif model_name == "ssd":
        net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")
        with open("mobilenet_classes.txt", "r") as f:
            classes = f.read().strip().split('\n')
    else:
        raise ValueError("Invalid model name. Supported models: 'yolo' or 'ssd'")

    return net, classes

def detect_humans(frame, net, classes, confidence_threshold=0.5):
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (416, 416), 127.5)

    net.setInput(blob)
    detections = net.forward()

    for detection in detections[0, 0]:
        score = detection[2]
        class_id = int(detection[1])

        if score > confidence_threshold and classes[class_id] == "person":
            x = int(detection[3] * width)
            y = int(detection[4] * height)
            w = int(detection[5] * width)
            h = int(detection[6] * height)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return frame

def main(model_name, confidence_threshold):
    try:
        net, classes = load_model(model_name)
    except Exception as e:
        print("Error:", str(e))
        return

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        frame = detect_humans(frame, net, classes, confidence_threshold)

        cv2.imshow("Human Object Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="yolo", help="Choose the model: 'yolo' or 'ssd'")
    parser.add_argument("--confidence", type=float, default=0.5, help="Minimum confidence threshold for detection")
    args = parser.parse_args()

    main(args.model, args.confidence)
