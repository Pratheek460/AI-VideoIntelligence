class AnalyticsEngine:

    def analyze(self, tracked_objects):

        people = 0

        vehicles = 0

        for obj in tracked_objects:

            if obj["label"] == "person":
                people += 1

            elif obj["label"] in [

                "car",

                "truck",

                "bus",

                "motorcycle"

            ]:

                vehicles += 1

        return {

            "people": people,

            "vehicles": vehicles,

            "total": len(tracked_objects)

        }