import genanki

def create_flashcard_deck(flashcards, deck_name="Arabic Flashcards"):
    """Generates an Anki deck from flashcards and exports it as a .apkg file.
    Creates bidirectional cards (one Arabic→English, one English→Arabic)."""
    deck_id = 123456789  # Unique deck ID
    deck = genanki.Deck(deck_id, deck_name)
    
    model = genanki.Model(
        1607392319,
        "Arabic Flashcard Model",
        fields=[
            {"name": "Front"},
            {"name": "Back"}
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Front}}",
                "afmt": "{{Front}}<hr id='answer'>{{Back}}"
            }
        ],
    )
    
    for flashcard in flashcards:
        front = flashcard.get("front", "n/a")
        back = flashcard.get("back", "n/a")
        
        # Create Arabic → English card
        note_ar_to_en = genanki.Note(
            model=model,
            fields=[front, back]
        )
        deck.add_note(note_ar_to_en)
        
        # Create English → Arabic card
        note_en_to_ar = genanki.Note(
            model=model,
            fields=[back, front]
        )
        deck.add_note(note_en_to_ar)
    
    output_file = f"{deck_name.replace(' ', '_').lower()}.apkg"
    genanki.Package(deck).write_to_file(output_file)
    return output_file

# Mock Flashcards for Testing
mock_flashcards = [
    {
        "front": "كَتَبَ – يَكْتُبُ\nكِتَابَة\nباب: ضَرَبَ يَضْرِبُ\nنوع الفعل: ناقص يائي",
        "back": "to write"
    },
    {
        "front": "كتاب\nجمع: كتب",
        "back": "book"
    },
    {
        "front": "n/a",
        "back": "n/a"
    }
]

# Test the function by running this script directly
if __name__ == "__main__":
    output_file = create_flashcard_deck(mock_flashcards, deck_name="TestDeck")
    print(f"Anki deck created successfully: {output_file}")
