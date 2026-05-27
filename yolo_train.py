from roboflow import Roboflow
from ultralytics import YOLO


def main():
    # Connect to Roboflow
    rf = Roboflow(api_key="D4sI5yqzlOyI2BJX7XYd")

    # Download dataset automatically
    project = rf.workspace("medicalvision-xbbat").project("abc-hgxjc")
    dataset = project.version(12).download("yolov8")

    # Train model on GPU
    model = YOLO("yolov8n.pt")
    model.train(
        data=dataset.location + "/data.yaml",
        epochs=50,
        device=0
    )


if __name__ == "__main__":
    main()
