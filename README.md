## Dependencies

```shell
conda create -n LabelStudio python=3.12 -y
conda activate LabelStudio
pip install poetry
poetry install
```

## Run

```shell
python main.py
```

## Detection

```shell
yolo predict model=./runs/detect/train/weights/best.pt source=0 save=True show=True
```

