### Quick Start

```bash
conda create -n yolov5_pyqt5 python=3.8
conda activate yolov5_pyqt5
pip install -r requirements.txt
python main.py
```
### About Packaging

- install pyinstaller

```
pip install pyinstaller==5.7.0
```

- package the GUI

```
pyinstaller -D -w --add-data="./utils/*;./utils" --add-data="./config/*;./config" --add-data="./icon/*;./icon" --add-data="./pt/*;./pt" --add-data="./imgs/*;./imgs" main.py
```

- if no errors occur, the packaged application is in dist/main

### Function

1. support image/video/webcam/rtsp as input
2. change model
3. change IoU
4. change confidence
5. set latency
6. paly/pause/stop
7. result statistics
8. save  detected image/video automatically

You can find ui files in [main_win](./main_win) and [dialog](dialog)

