# 🏃 Real-Time Human Motion Tracker

The Real-Time Human Motion Tracker is a Python-based project that uses a webcam to detect and track human movements in real-time. The application employs the YOLOv3 (You Only Look Once version 3) model for object detection to identify humans in the webcam feed and visually highlight their movements with green bounding boxes.

## 🌟 Features

- Real-time human motion tracking using the webcam.
- Utilizes the YOLOv3 model for human detection.
- Live video feed with green bounding boxes indicating detected humans.
- Command-line arguments to select the model and set confidence threshold for human detection.

## ⚙️ Requirements

- Python 3.x
- OpenCV library (`pip install opencv-python`)
- Numpy library (`pip install numpy`)
- YOLOv3 model 

## 🚀 Getting Started

1. Clone this repository:

```bash
git clone https://github.com/shaileshsaravanan/real-time-human-motion-tracker.git
cd real-time-human-motion-tracker
```

2. Download the YOLOv3 model files:

   - Download the `yolov3.weights` file, `yolov3.cfg` configuration file, and `coco.names` file from https://pjreddie.com/darknet/yolo/ and place them in the project directory.

3. Run the tracker with optional arguments:

```bash
python motion_tracker.py --model yolo --confidence 0.5
```

- `--model`: Choose the model for human detection (Supported models: 'yolo' or 'ssd', default: 'yolo').
- `--confidence`: Set the minimum confidence threshold for detection (Default: 0.5).

## 📷 Usage

1. Ensure that your webcam is connected and working properly.
2. Execute the `motion_tracker.py` script, and the webcam feed with detected humans will appear.
3. Tracked humans will be enclosed with green bounding boxes.

## ❗ Troubleshooting

- If the webcam is not working, check your webcam drivers and try reconnecting it.
- If the YOLOv3 model files are missing or not in the correct location, the tracker will not work. Make sure the `yolov3.weights`, `yolov3.cfg`, and `coco.names` files are in the project directory.
- Make sure to have the required Python libraries installed.

## 🙏 Acknowledgments

- YOLOv3 model by Joseph Redmon, Ali Farhadi, and others. More information available at https://pjreddie.com/darknet/yolo/.
- This project is for educational purposes and inspired by the amazing community of developers contributing to computer vision and object detection projects.

## 📄 License

The Real-Time Human Motion Tracker is open-source software under the [MIT License](LICENSE).
```