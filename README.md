# Flash Card App - Marathi Language Learning

A simple flashcard app built using Python and Tkinter designed to help you learn Marathi words. This app displays flashcards with Marathi-English word pairs and allows users to mark whether they know the word or not using ❌ and ✅ buttons.

## Features

- Displays Marathi words with their English translations.
- Easy-to-use interface with image-based buttons.
- Flip the card to reveal the English translation.
- Mark words as known or unknown using ❌ and ✅ buttons.

## File Structure

```plaintext
DAY 31 FLASH CARDS/
├── data/
│   ├── marathi_words.csv             # Source data with Marathi-English word pairs
│   ├── marathi_words_to_learn.csv    # Stores words that the user still needs to learn
├── images/
│   ├── card_back.png                 # Image for the back of the flashcard
│   ├── card_front.png                # Image for the front of the flashcard
│   ├── right.png                     # Image for the ✅ button
│   ├── wrong.png                     # Image for the ❌ button
├── main.py                           # Main Python script to run the app
├── requirements.txt                  # Python dependencies file
