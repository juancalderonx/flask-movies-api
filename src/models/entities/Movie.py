from utils.DateFormat import DateFormat
class Movie:

    def __init__(self, id=None, title=None,duration=None,
                 released=None) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

    def toJSON(self):
        """Returns a JSON representation of the Movie object."""

        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': DateFormat.dateFormatter(self.released)
        }
