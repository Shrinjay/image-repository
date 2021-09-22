from torch import hub

MIN_CONFIDENCE = 0.6


class CVModel:
    def __init__(self):
        self.model = hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def run_model(self, img):
        return self.model(img)

    def get_labels(self, img):
        results = self.run_model(img)
        df = results.pandas().xyxy[0]
        df = df[df['confidence'] > MIN_CONFIDENCE]
        return list(df['name'])
