from ultralytics import YOLO


def main():

    model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

    results = model.train(data="datasets/data.yaml", epochs=100, imgsz=640, device="mps")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
