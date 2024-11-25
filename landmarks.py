import csv


class Landmark:
    """determine and return a certain landmark based on current distance."""
    _LOCATIONS = []

    @staticmethod
    def _load_locations():
        """load locations from the locations file and append them to the _LOCATIONS list"""
        with open('./locations', 'r') as f:
            _reader = csv.reader(f)
            for row in _reader:
                Landmark._LOCATIONS.append(row)

    def __init__(self):
        """Create the list of names and corresponding distances of each location"""
        Landmark._load_locations()
        self._name = []
        self._distance = []
        for i in Landmark._LOCATIONS:
            self._name.append(i[0])
            self._distance.append(i[1])

    def get_landmark(self, distance: int, speed: int):
        """get a landmark based on your current distance
        and accounting for if your current travel pace
        would make you go over the landmarks value"""
        if speed == 1:
            if str(distance) in self._distance:
                i = self._distance.index(str(distance))
                return self._name[i], 0
            else:
                return None
        else:
            if str(distance) in self._distance:
                i = self._distance.index(str(distance))
                return self._name[i], 0
            else:
                for i in range(1, speed):
                    if str(distance + i) in self._distance:
                        j = self._distance.index(str(distance + i))
                        return self._name[j], i
                return None
