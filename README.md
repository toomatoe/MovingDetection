# Moving Detection

Moving Detection is a small Python research project for testing motion detection on CCTV-style footage first, then expanding into object tracking and human-focused analysis later.

## What this repo is for

The aim is to build a practical testbed that can answer a few simple questions well:

- Can we detect moving vehicles reliably in messy real-world video?
- How many false positives does the baseline produce?
- Which approach gives the best balance of speed and accuracy?
- What should be promoted from notebook experiments into reusable code?

## Working plan

### Stage 1: Motion detection baseline

Start with methods that are easy to explain and easy to measure:

- Frame differencing
- OpenCV background subtraction with MOG2 or KNN
- Contour cleanup with thresholding and morphology
- Optional optical flow checks for motion consistency

### Stage 2: Object detection and tracking

Once the baseline is stable, move to learned detectors and trackers:

- YOLO through Ultralytics for quick object detection
- ByteTrack or DeepSORT for frame-to-frame identity
- OpenCV overlays for debugging and visualization

### Stage 3: Human analysis

After vehicle motion works, branch into human-specific experiments:

- Face detection with MediaPipe or OpenCV DNN
- Face mesh and landmark tracking
- Eye-region analysis and gaze-related features
- Pose estimation for broader body movement context

## Recommended datasets

Good starting points for motion and vehicle research:

- UA-DETRAC
- AI City Challenge datasets
- BDD100K
- KITTI
- MOT17 and MOT20
- VIRAT

Later, for face and eye work:

- 300-W
- WFLW
- CelebA
- MPIIFaceGaze

## Project layout

- `src/moving_detection/`: reusable application code
- `notebooks/`: experiment space for notebook-first work
- `tests/`: small checks for imports and basic behavior
- `data/`: raw clips, sample assets, and processed outputs
- `models/`: saved model weights or experiment artifacts

## Tools and libraries

Core stack:

- NumPy
- OpenCV
- Matplotlib
- scikit-learn
- PyYAML
- tqdm

Notebook support:

- JupyterLab
- ipykernel

Optional vision stack for later stages:

- PyTorch
- torchvision
- Ultralytics
- supervision
- MediaPipe

## How to work in the repo

1. Activate the virtual environment.
2. Open the notebook in `notebooks/` for fast experimentation.
3. Move stable logic into `src/moving_detection/`.
4. Add tests once a baseline detector is working on sample footage.

## Next step

The most useful next piece is a notebook that loads a sample video, runs a motion baseline, and shows the frame output so the approach can be evaluated on real footage.
