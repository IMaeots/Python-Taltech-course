"""Music."""


class Note:
    """Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """
    def __init__(self, note: str):
        """Initialize the class.

        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """
        note = evaluate_note(note)

        self.note_name = note[0]
        self.sharpness = note[1]

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note_name + self.sharpness}>"

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        if isinstance(other, Note):
            return (self.note_name == other.note_name) and (self.sharpness == other.sharpness)
        return False


def evaluate_note(note: str) -> str:
    note_name = note[0].upper()
    note_sharpness = note[1] if len(note) > 1 else ' '

    if note_sharpness == 'b' or note_sharpness == 'B':
        # Change note backwards one and make it sharp
        if note_name == 'A':
            note_name = 'Z'
        else:
            prev_ascii = ord(note_name) - 1
            note_name = chr(prev_ascii)

        note_sharpness = '#'

    return note_name + note_sharpness


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """
        self.note_collection = []

    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """
        if isinstance(note, Note):
            self.note_collection.append(note)
        else:
            raise TypeError()

    def pop(self, note: str) -> Note | None:
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        index = 0
        note = evaluate_note(note)
        for __note in self.note_collection[::-1]:
            index -= 1
            if __note.note_name == note[0] and __note.sharpness == note[1]:
                self.note_collection.remove(__note)
                return __note

        return None

    def extract(self) -> list[Note]:
        """
        Return a list of all the notes from the collection and empty the collection itself.

        Order of the list must be the same as the order in which the notes were added.

        Example:
          collection = NoteCollection()
          collection.add(Note('A'))
          collection.add(Note('C'))
          collection.extract() # -> [<Note: A>, <Note: C>]
          collection.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted everything.

        :return: A list of all the notes that were previously in the collection.
        """
        current_collection = self.note_collection.copy()
        self.note_collection.clear()
        return current_collection

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the collection.

        Example:
          collection = NoteCollection()
          collection.add(Note('C#'))
          collection.add(Note('Lb'))
          print(collection.get_content())

        Output in console:
           Notes:
            * C#
            * Lb

        The notes must be sorted alphabetically by name and then by sharpness, that is A, A#, B, Cb, C and so on.
        Recommendation: Use normalized note names, not just the __repr__()

        :return: Content as a string
        """
        content = "Notes:\n"
        for note in sorted(self.note_collection, key=lambda tone: tone.note_name):
            content += f" * {note.note_name}{note.sharpness}\n"

        if content == "Notes:\n":
            return content + f" Empty"
        else:
            return content


if __name__ == '__main__':
    note_one = Note('a') # yes, lowercase
    note_two = Note('C')
    note_three = Note('Eb')
    collection = NoteCollection()

    print(note_one)  # <Note: A>
    print(note_two)  # <Note: C>
    print(note_three)  # <Note: Eb>

    collection.add(note_one)
    collection.add(note_two)

    print(collection.get_content())
    # Notes:
    #   * A
    #   * C

    print(collection.extract())  # [<Note: A>,<Note: C>]
    print(collection.get_content())
    # Notes:
    #  Empty

    collection.add(note_one)
    collection.add(note_two)
    collection.add(note_three)

    print(collection.pop('a') == note_one)  # True
    print(collection.pop('Eb') == note_three)  # True