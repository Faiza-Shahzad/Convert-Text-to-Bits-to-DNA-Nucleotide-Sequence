# Convert-Text-to-Bits-to-DNA-Nucleotide-Sequence
Educational Python prototype that encodes text into DNA bases (A/T/G/C) and decodes it back, with a round-trip check.
# Text to DNA Encoder (Educational Prototype)

A small Python program that converts a text message into a DNA sequence
(A, T, G, C) and converts it back, to show the basic idea behind DNA data storage.

## How it works

1. **Text to ASCII:** each character is converted to its ASCII number.
2. **ASCII to bits:** each number becomes an 8-bit binary string.
3. **Bits to DNA:** bits are split into pairs and mapped to bases:
   `00 = A`, `01 = T`, `10 = G`, `11 = C`.
4. **DNA to text:** the process is reversed to recover the original message.
5. **Round-trip check:** the program prints `True` if the recovered text
   matches the original.

## Example

    Input:          FAIZA
    ASCII:          [70, 65, 73, 90, 65]
    Bits:           0100011001000001010010010101101001000001
    DNA:            TATGTAATTAGTTTGGTAAT
    Recovered text: FAIZA
    Round trip OK:  True

## How to run

    python text_to_dna.py

## Limitations (what this version does NOT do)

- **No biological constraints.** The simple 2-bit mapping can produce DNA
  with low GC content (the example above is about 20% GC) or long
  repeats such as `AAAA`. Real DNA synthesis and sequencing need
  balanced GC content and short homopolymers.
- **No error correction.** A single changed base corrupts the decoded text.
- **English text only.** Characters above ASCII value 255 (for example Urdu
  letters) are not supported yet. UTF-8 byte handling is planned.
- **No data format.** There is no header, length field, or chunk index.

## Planned next steps

- A checker for GC content and homopolymer runs
- Constraint-aware encoding that avoids repeats
- Scrambling of the input data
- Chunking with index and checksum
- FASTA file output
- Tests

This project is for learning and is not intended for real DNA synthesis.
