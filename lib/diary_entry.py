class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.index = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        return f"{int(word_count / wpm)} minutes" 

    def reading_chunk(self, wpm, minutes):
        words_to_read = int(wpm * minutes)
        end_of_contents = self.index + words_to_read
        chunk = self.contents.split()[self.index: end_of_contents]
        self.index += words_to_read
        if self.index >= self.count_words(): 
            self.index = 0
        return " ".join(chunk) 