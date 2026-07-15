from ultralytics import YOLO
import cv2


class ObjectDetector:

    def __init__(self):

        self.model = YOLO("yolo11n.pt")

        self.class_names = self.model.names

        self.allowed_classes = {
            "person",
            "car",
            "bus",
            "truck",
            "motorcycle",
            "bicycle"
        }

        self.confidence = 0.4

    def detect(self, frame):

        results = self.model(frame, conf=self.confidence)

        detections = []

        annotated = frame.copy()

        for result in results:

            for box in result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                confidence = float(box.conf[0])

                class_id = int(box.cls[0])

                label = self.class_names[class_id]

                if label not in self.allowed_classes:
                    continue

                detections.append(
                    {
                        "class_id": class_id,
                        "label": label,
                        "confidence": confidence,
                        "bbox": {
                            "x1": x1,
                            "y1": y1,
                            "x2": x2,
                            "y2": y2
                        },
                        "center": (
                            (x1 + x2) // 2,
                            (y1 + y2) // 2
                        )
                    }
                )

                cv2.rectangle(
                    annotated,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    annotated,
                    f"{label} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        return annotated, detections