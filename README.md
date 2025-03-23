## 📸 **Animal Species Detection**
This project utilizes YOLOv8, a state-of-the-art object detection model, to identify and classify animal or plant species within images. The application features a user-friendly web interface, built with Streamlit, easily upload images and receive real-time species detection results. OpenCV is integrated for image processing. 

## 📚 Datasets
The dataset used in this project consists of labeled images of 10 different animal classes.
- [Wildlife Dataset](https://www.kaggle.com/datasets/biancaferreira/african-wildlife)
- [Danger of Extinctin Image Dataset](https://www.kaggle.com/datasets/brsdincer/danger-of-extinction-animal-image-set)
- [Animal Detection Dataset](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset )


## 🚀 Getting Started
Follow theses steps to set up the environment and run the application.

1. Fork the repository
2. Clone the forked repository.
    ```bash
    git clone https://github.com/<YOUR-USERNAME>/Animal-Species-Detection
    cd Animal-Species-Detection
    ```

3. Create a python virtual environment and activate the environemnt.
    ``` bash
    python3 -m venv venv
    ```

    ```bash
    venv\Scripts\activate
    ```

4. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
5. Run the application.
    ```python
    streamlit run './scripts/app.py'
    ```

## ⚖️ Evaluation
The performance of the model is evaluated by metrics such as Precision, Recal, and Mean Average Precision (mAP).

    * Model - YOLO v8
    * Precision - 0.94
    * Recall - 0.91
    * F1-Score - 0.93
    * mAP@0.5 - 0.9

