# RSA CTF Challenge - Even Modulus Flaw

**Flag:** `picoCTF{tw0_1$_pr!m305af7255}`

## Vulnerability Explanation
The core vulnerability is that the public modulus ($N$) is an even number, trivially revealing that one of its underlying prime factors is 2. This completely bypasses the mathematical difficulty of prime factorization, allowing for the instant calculation of the private decryption key.
