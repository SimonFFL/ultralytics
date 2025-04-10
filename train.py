from ultralytics import YOLO
from pathlib import Path

if __name__ == "__main__":
    # Load a model
    model = YOLO("test_yolo/train/weights/best.pt")  # load an official model
    # set the model to gpu 5
    model.to("cuda:5")  # set the model to gpu 5

    # # Train the model
    # results = model.train(data="AB_20220608.yaml", epochs=10, imgsz=640, project="test_yolo", device="1")  # train the model
    # # Validate the model
    # results = model.val()  # validate the model
    # # Predict with the model    
    results = model.predict(source="/media/chenqunWorkSpace/Project_R/code/YOLOv5/data_test_time")  # predict with the model

    for result in results:
        #save result
        result.save(filename="test_yolo/" + Path(result.path).name)  # save the result


