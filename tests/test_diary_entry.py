from lib.diary_entry import *

def test_input_title_and_content_instanciates_correctly():
    diary_entry = DiaryEntry("Great Day!", "I found £10 on the floor!")
    assert diary_entry.title == "Great Day!"
    assert diary_entry.contents == "I found £10 on the floor!"

def test_count_words_method_return_the_number_of_words_in_conents():
    diary_entry = DiaryEntry("Count Test", "Contents string is seven word in length")
    assert diary_entry.count_words() == 7

def test_method_calculates_and_returns_reading_time():
        diary_entry = DiaryEntry("Wpm", "reading time is three minutes if contents string length is eighteen and the words per minute is 6")
        assert diary_entry.reading_time(6) == "3 minutes"
        
def test_reading_chunk_method_returns_the_target_amount_of_contents():
    diary_entry = DiaryEntry("Great Day!", "I found £10 on the floor!")
    assert diary_entry.reading_chunk(1, 4) == "I found £10 on"
    