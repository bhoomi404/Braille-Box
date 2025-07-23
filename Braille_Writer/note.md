📝 Writer Part – Braille to Text (Box 1)
This part of the project lets us type text using Braille input. It’s like a keyboard for blind users, where they press specific buttons in combination to form letters. The main goal here is to convert Braille button inputs into English letters and display/store them.

🔧 How it works:
We used six push buttons, each one representing one dot of the standard Braille cell (dots 1 to 6).

These buttons are connected to six GPIO pins on the Raspberry Pi.

When we press a combination of buttons, the program checks which buttons are currently pressed and creates a binary-like pattern (e.g. "100000" for only dot 1).

This pattern is compared with a predefined dictionary in the code that maps Braille combinations to English alphabets.

Once a match is found, that alphabet is written to a text file (e.g., write.txt) and also printed in the terminal.

This way, we can keep pressing different button combinations, and it will build up a full sentence or word in the file.

📂 Where the text goes:
The text is saved in a file called write.txt, which is stored inside the box/ folder on the Desktop. Every time a valid letter is detected, it's added to this file. This file is later used by the second part (the Reader).

Sample output:
<img width="595" height="467" alt="image" src="https://github.com/user-attachments/assets/2f9618dc-f259-4cb0-a36a-54ad1846ebb4" />
