📝 Writer Part – Braille to Text (Box 1)
This part lets us type using Braille, like a special keyboard for visually impaired users. By pressing different combinations of six buttons, we can form letters, which then get converted into regular English text.

🔧 How it works:
We used six push buttons, each representing one of the six dots in a Braille cell (dot 1 to dot 6).

These buttons are connected to GPIO pins of the Raspberry Pi.

When a combination is pressed, the program reads which buttons are down and forms a pattern like "100000" (meaning only dot 1 was pressed).

The program then checks this pattern against a dictionary defined in the code that maps each combination to an English letter.

If a match is found, that letter is:

Printed on the terminal (for debug/visibility)

Appended to a text file called write.txt

📂 Where the text goes:
The generated text is stored in write.txt, which is located inside the box/ folder on the Desktop.

Every time we enter a new letter, it gets added to this file, forming complete words and sentences.

This file is also used later in the Reader Part (Box 2) for converting text to speech.

Sample Output:
Below is an example of the terminal showing the output while Braille combinations are entered:

<p align="center"> <img width="595" height="467" src="https://github.com/user-attachments/assets/2f9618dc-f259-4cb0-a36a-54ad1846ebb4" alt="Sample Writer Output"> </p>
