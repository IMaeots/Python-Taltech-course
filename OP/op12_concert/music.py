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
        self.sharpness = note[1] if len(note) > 1 else ''
        self.note = self.note_name + self.sharpness

    def transpose(self, interval):
        """Logic to transpose the note by the given interval."""
        notes_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        current_index = notes_order.index(self.note_name)

        if interval == 2:
            new_index = (current_index + 1) % len(notes_order)
            return Note(notes_order[new_index] + self.sharpness)
        else:
            if self.sharpness == '#':
                new_index = (current_index + 1) % len(notes_order)
                return Note(notes_order[new_index])
            else:
                return Note(self.note_name + '#')

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note_name + self.sharpness}>"

    def __hash__(self):
        """Give Note a Hash."""
        return hash(self.note)

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        if isinstance(other, Note):
            return (self.note_name == other.note_name) and (self.sharpness == other.sharpness)
        return False


def evaluate_note(note: str) -> str:
    """Change the note into correct format."""
    note_name = note[0].upper()
    note_sharpness = note[1] if len(note) > 1 else ''

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
            if note not in self.note_collection:
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
            if __note.note_name == note[0] and __note.sharpness == (note[1] if len(note) > 1 else ''):
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
        first = True
        for note in sorted(self.note_collection, key=lambda tone: tone.note_name):
            if first:
                content += f"  * {note.note_name}{note.sharpness}"
                first = False
            else:
                content += f"\n  * {note.note_name}{note.sharpness}"

        if content == "Notes:\n":
            return content + "  Empty."
        else:
            return content


class Chord:
    """Chord class."""

    def __init__(self, note_one: Note, note_two: Note, chord_name: str, note_three: Note = None):
        """
        Initialize chord class.

        A chord consists of 2-3 notes and their chord product (string).
        If any of the parameters are the same, raise the 'DuplicateNoteNamesException' exception.
        """
        notes = [note_one, note_two]
        if note_three:
            notes.append(note_three)

        note_names = set()
        for note in notes:
            note_name = f"{note.note_name}{note.sharpness}"
            if note_name in note_names:
                raise DuplicateNoteNamesException("Duplicate note names found in the chord.")
            note_names.add(note_name)

        if chord_name in note_names:
            raise DuplicateNoteNamesException("Duplicate note names found in the chord.")

        self.notes = notes
        self.chord_name = chord_name

    def __repr__(self) -> str:
        """
        Chord representation.

        Return as: <Chord: [chord_name]> where [chord_name] is the name of the chord.
        """
        return f"<Chord: {self.chord_name}>"

    def get_notes(self):
        """Get function to return notes of chord."""
        return self.notes


class Chords:
    """Chords class."""

    def __init__(self):
        """
        Initialize the Chords class.

        Add whatever you need to make this class function.
        """
        self.chords = {}

    def add(self, chord: Chord) -> None:
        """
        Determine if chord is valid and then add it to chords.

        If there already exists a chord for the given pair of components, raise the 'ChordOverlapException' exception.

        :param chord: Chord to be added.
        """
        components = tuple(sorted(chord.notes, key=lambda x: x.note))  # Sorting for consistency.

        if components in self.chords:
            raise ChordOverlapException("Chord with these components already exists.")

        self.chords[components] = chord

    def get(self, first_note: Note, second_note: Note, third_note: Note = None) -> Chord | None:
        """
        Return the chord for the 2-3 notes.

        The order of the first_note and second_note and third_note is interchangeable.

        If there are no combinations for the 2-3 notes, return None

        Example:
          chords = Chords()
          chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
          print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
          print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
          print(chords.get(Note('D'), Note('Z')))  # ->  None
          chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
          print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

        :param first_note: The first note of the chord.
        :param second_note: The second note of the chord.
        :param third_note: The third note of the chord.
        :return: Chord or None.
        """
        notes = [first_note, second_note]
        if third_note:
            notes.append(third_note)

        components = tuple(sorted(notes, key=lambda x: x.note))  # Sorting for consistency.

        for key, chord in self.chords.items():
            if key == components:
                return chord

        return None


class DuplicateNoteNamesException(Exception):
    """Raised when attempting to add a chord that has same names for notes and product."""


class ChordOverlapException(Exception):
    """Raised when attempting to add a combination of notes that are already used for another existing chord."""


if __name__ == '__main__':
    chords = Chords()
    chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
    print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
    print(chords.get(Note('D'), Note('Z')))  # ->  None
    chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
    print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

    chords = Chords()

    chord1 = Chord(Note('A'), Note('C#'), 'Amaj', Note('E'))
    chord2 = Chord(Note('E'), Note('G'), 'Emin', note_three=Note('B'))
    chord3 = Chord(Note('E'), Note('B'), 'E5')

    chords.add(chord1)
    chords.add(chord2)
    chords.add(chord3)

    print(chords.get(Note('e'), Note('b')))  # -> <Chord: E5>

    try:
        wrong_chord = Chord(Note('E'), Note('A'), 'E')
        print('Did not raise, not working as intended.')
    except DuplicateNoteNamesException:
        print('Raised DuplicateNoteNamesException, working as intended!')

    try:
        chords.add(Chord(Note('E'), Note('B'), 'Emaj7add9'))
        print('Did not raise, not working as intended.')
    except ChordOverlapException:
        print('Raised ChordOverlapException, working as intended!')
