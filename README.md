## **Animal Species Detection**
The aim of this project is to develop an efficient computer vision model capable of real-time wildlife detection.

<!-- <p align="center">
  <img src="./demo/demo.gif" alt="Demo GIF">
</p> -->


## Datasets
The dataset used in this project consists of labeled images of 10 different animal classes.
- [Dataset 1](https://www.kaggle.com/datasets/biancaferreira/african-wildlife)
- [Dataset 2](https://www.kaggle.com/datasets/brsdincer/danger-of-extinction-animal-image-set)
- [Dataset 3](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset )


## Getting Started
Follow theses steps to set up the environment and run the application.

1. Fork the repository
2. Clone the forked repository.
    ```bash
    git clone https://github.com/<YOUR-USERNAME>/Animal-Species-Detection
    cd Animal-Species-Detection
    ```

3. Create a python virtual environment.
    ``` bash
    python3 -m venv venv
    ```

4. Activate the virtual environment.

    - On Linux and macOS
    ``` bash
    source venv/bin/activate
    ```
    - On Windows
    ``` bash
    venv\Scripts\activate
    ```

5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application.
    ```python
    streamlit run './scripts/app.py'
    ```

## Evaluation
The performance of the model is evaluated by metrics such as Precision, Recal, and Mean Average Precision (mAP).

    * Model - YOLO v8
    * Precision - 0.94
    * Recall - 0.91
    * F1-Score - 0.93
    * mAP@0.5 - 0.9

