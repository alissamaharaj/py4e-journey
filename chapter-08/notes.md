*22-09-26: Completed the exercises and the quiz. Exercise 7_02 was difficult for me because I didn't understand how to use the `split()` function or what it does; I had to use the hints on the autograder to help me. Even with the help, I still struggled to understand why, in this code block, the index used was '1' instead of ':':
```python
 if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    conf = line.split()
    tot = tot + float(conf[1])
```
After some further reading, I realized that using the `split()` function treats the resulting parts as 'words' instead of continuing to treat it as a string of individual characters. This completely explained everything about the choices made, and it's a very clever choice as well.
