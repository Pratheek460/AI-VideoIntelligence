import math


class ObjectTracker:

    def __init__(self):

        self.next_id = 1

        self.objects = {}

    def update(self, detections):

        tracked = []

        for detection in detections:

            cx, cy = detection["center"]

            assigned = None

            for object_id, old_center in self.objects.items():

                distance = math.sqrt(

                    (cx - old_center[0]) ** 2 +

                    (cy - old_center[1]) ** 2

                )

                if distance < 50:

                    assigned = object_id

                    break

            if assigned is None:

                assigned = self.next_id

                self.next_id += 1

            self.objects[assigned] = (cx, cy)

            detection["id"] = assigned

            tracked.append(detection)

        return tracked