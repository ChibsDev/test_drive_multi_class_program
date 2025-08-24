class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        return f"{int(word_count / wpm)} minutes" 

    def reading_chunk(self, wpm, minutes):
        words_to_read = int(wpm * minutes)
        chunk = self.contents.split()[0:words_to_read]
        return " ".join(chunk)