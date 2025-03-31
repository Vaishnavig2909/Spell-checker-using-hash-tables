# Spell-checker-using-hash-tables
## Overview of the Project
- A spell-checker tool that identifies misspelled words in a sentence.
- Provides word suggestions using edit distance.

## Key Features:
- Spell-checking using hash keys.
- Suggests similar words for correction

## Objectives
- Implement a spell-checker using efficient DSA techniques.
- Compare different word distance algorithms.
- Evaluate hash functions for collision reduction.

## Methodology
- Framework:
Input sentence -> Tokenize into words.
Use hashing table to check if each word is correctly spelled.
If misspelled, suggest corrections based on word distance algorithms.

## Hash tables concept
- Hashing is a mathematical process that converts data into a unique string of characters called a hash value, hash code, or hash digest.

- Hash tables are an effective data structure for implementing dictionaries.

- A hash table is a data structure where elements are accessed by a keyword rather than an index number, unlike in lists and arrays

- Data items are stored in key/value pairs similar to dictionaries

- Hash tables are used in different applications such as network routers,  operating systems, computer games, and bioinformatics.

- The main idea at the heart of the hash table data structure is that it allows users to assign keys to elements and then use those keys later to look up or remove elements.

- A hash function h to compute the slot from the key k
h:U {0,1, …, m-1}
where the size m of the hash table is typically much less than |U|
An element with key k hashes to slot h(k)
h(k) is the hash value of key
![image](https://github.com/user-attachments/assets/71c359c8-2417-4037-897f-5bf07f96d11c)

## Methodology
- Different approaches possible for implementation: 

1. For hashing:

Non-Cryptographic Hash Functions: FNV Hash, CRC32
Cryptographic Hash Functions: MD5, SHA-256, SHA-512

2. For calculating Edit distance

Levenshtein Distance
Jaro-Winkler Distance
Damerau-Levenshtein Distance

## Fnv hash (Fowler-Noll-Vo Hash)

- Paradigm:
Bitwise Operations: The algorithm relies on XOR and multiplication operations to mix the input bits thoroughly.

- Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

- Collision Avoidance:
FNV avoids collisions by:
Using large prime numbers to reduce patterns in hash values.
Ensuring that even small changes in input produce significantly different outputs (good avalanche effect).

## CRC32 (Cyclic Redundancy Check, 32-bit)

- Paradigm:
Bitwise Operations: The algorithm relies on XOR and multiplication operations to mix the input bits thoroughly.

- Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

- Collision Avoidance:
FNV avoids collisions by:
Using large prime numbers to reduce patterns in hash values.
Ensuring that even small changes in input produce significantly different outputs (good avalanche effect).

## MD5 (Message Digest Algorithm 5)

- Paradigm:
 Cryptographic hash function

- Complexity:
Time: O(n), where n is the length of the input.
Space: O(1)

- Collision Avoidance:MD5 was designed to minimize collisions using sophisticated compression functions. However, advances in cryptanalysis have made it possible to find collisions efficiently, rendering it insecure. 

## SHA-256 (Secure Hash Algorithm 256-bit)

- Paradigm: Cryptographic hash function (part of the SHA-2 family, secure for most cryptographic purposes).

- Complexity:
Time: O(n), where n is the length of the input.
Space: O(1) 

- Collision Avoidance:SHA-256 minimizes collisions through its design, which includes mixing functions and a large output space (256 bits). As of now, no practical collision attacks exist. 

## SHA-512 (Secure Hash Algorithm 512-bit)
- Paradigm:
Cryptographic hash function (part of the SHA-2 family, secure for cryptographic purposes).

- Complexity:
Time: O(n), where n is the length of the input.
Space: O(1) 

- Collision Avoidance: SHA-512's large output space and mixing functions make collisions extremely improbable. It is considered secure and more robust than SHA-256 in scenarios requiring higher security.

## Choice of hashing algorithm: SHA 256

- Strong Cryptographic Security: Resistant to collisions, pre-image, and second pre-image attacks, ensuring robust data integrity.

- 256-bit Output: Larger hash size provides higher resistance to brute-force attacks compared to MD5 (128-bit) or SHA-1 (160-bit).  

- No Known Vulnerabilities: Unlike MD5 and SHA-1, SHA-256 remains unbroken under modern cryptanalysis.  
- Global Standard: Recommended by NIST and widely adopted in SSL/TLS, digital signatures, and authentication systems.

- Efficient Performance: Optimized for both software and hardware, enabling fast and reliable computations.  

- Blockchain and Cryptocurrency Use: Powers secure systems like Bitcoin by ensuring transaction data integrity. 

- Future-Proof Security: Designed to withstand attacks as computational power grows, ensuring long-term reliability.  

- Widespread Adoption: Integrated into diverse applications like file verification, password hashing, and digital signatures.

## Levenshtein Distance

- Paradigm: Dynamic Programming. It uses a matrix to compute the distance between substrings incrementally.

- Complexity:
Time: O(mn), where m and n are the lengths of the two strings.
Space: O(mn) for a full DP matrix

- Other Important Details:
It handles only single-character edits.
It is sensitive to string length; longer strings tend to have larger distances.

## Jaro-Winkler Distance

- Paradigm: Similarity Metric. It does not rely on dynamic programming; instead, it matches and compares characters.

- Formula:
Winkler adjustment: Adds a prefix scale factor p:
![image](https://github.com/user-attachments/assets/8de923f0-ec2a-4f74-aec2-c2836f609f23)
![image](https://github.com/user-attachments/assets/a97edb42-0b2e-4d17-aa22-b9943f82175b)

where l is the length of the common prefix up to a max of 4, and p is a constant scaling factor.

- Complexity:
Time Complexity: O(mn) for matching characters and counting transpositions. For small strings, this is effectively constant time.
Space Complexity: O(1) requires no matrix
Well-suited for short strings and comparisons in applications like record linkage.
Incorporates transpositions but not other edit types like insertions or deletions.

## Damerau-Levenshtein Distance

- Paradigm:
Dynamic Programming, similar to Levenshtein Distance, with an added rule for handling transpositions.

- Complexity:
Time:  O(m×n), where m and n are the lengths of the strings.
Space: O(m×n), though optimizations exist for space reduction.

- More useful when accounting for common human errors like adjacent swaps.

## Choice of distance algorithm: Levenshtein distance

- Works well with strings of any length, unlike Jaro-Winkler, which is more effective for short strings like names.

- While it doesn’t explicitly account for transpositions like Damerau-Levenshtein, it is still effective for detecting general similarity without over-complicating the algorithm.

- While Damerau-Levenshtein captures more realistic typing errors (e.g., adjacent swaps), it adds extra computational overhead. Levenshtein strikes a balance by focusing on three operations (insertions, deletions, and substitutions), keeping both complexity and runtime manageable.

- For certain applications where transpositions are rare or unimportant, Levenshtein provides a faster and simpler solution compared to metrics like Damerau-Levenshtein.

- Levenshtein Distance is often considered better in specific scenarios because of its general-purpose nature, versatility, and simplicity.

- Levenshtein Distance can handle a broad range of string comparison problems.

- It considers insertions, deletions, and substitutions, making it adaptable to various use cases.

- The number it outputs directly represents the minimum edits needed to transform one string into another. This makes it intuitive for users to understand the degree of similarity or dissimilarity between strings.

- Levenshtein Distance uses a straightforward dynamic programming approach, which is easier to code and explain compared to more nuanced metrics.
![image](https://github.com/user-attachments/assets/b99526e5-e78a-450b-97f0-5be859957a40)

## PROGRAMMING LANGUAGE AND OTHER TECHNOLOGY USED
- Python version 3.12
- tkinter for the UI
- hashlib module for cryptographic hash functions

## Conclusion

- The use of hash tables ensures fast and efficient storage and retrieval of words, minimizing lookup times and enabling real-time spell-checking.

- Among the evaluated hashing algorithms, SHA-256 was chosen for its strong collision resistance, ensuring unique and secure word mapping while preventing hash collisions effectively.

- Levenshtein Distance was selected for its ability to handle a wide range of spelling errors, including insertions, deletions, and substitutions, providing reliable and contextually accurate word suggestions.

- Combining SHA-256 for hashing and Levenshtein Distance for word similarity resulted in an optimized system that balances computational efficiency with accuracy in error correction.
