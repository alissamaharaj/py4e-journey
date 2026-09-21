text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(":")
#print(ipos)
piece = text[ipos+5:]
#print(piece)
#print(piece+42.0) = will fail
value = float(piece)
print(value)
#print(value+42.0)
