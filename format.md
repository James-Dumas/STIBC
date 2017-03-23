# 8xp file format

BYTES|DESCRIPTION
-------|-----------
8      |every program starts with the ascii text: `**TI83F*`. in hex this is 2A 2A 54 49 38 33 46 2A
3      |always contains 1A 0A 00 or 1A 0A 0A. which one you get depends on what calculator model was used, but I'm not sure which models produce which or how this plays into compatibility between models.
42     |4s character comment. This can be anything, but it usually contains file creation info.
2      |size of the entire data section in bytes.
       |**Start of Data Section**
2      |always 0D 00.
2      |size of the program data in bytes.
1      |variable type ID. the ID for programs is 05.
8      |program name, padded with 00.
1      |version, usually 00.
1      |flag. default is 00, set to 80 to make the program archived.
2      |size of the program data in bytes.
       |**Start of Program Data**
2      |number of token bytes in the program.
n      |list of tokens in the program (actual code).
       |**End of Program Data & Data Section**
2      |checksum. lower 2 bytes of the sum of the entire data section.

Note: every two-byte integer is stored with the least significant byte first.
e.g. if the two bytes were `0xAB` and `0xCD` in that order it would represent the integer `0xCDAB`.

### Template:
2A 2A 54 49 38 33 46 2A 1A 0A 00 (42 byte comment) (data size) 0D 00 (program data size) 05 (program name) 00 00 (program data size) (program token size) (actual code) (checksum)
