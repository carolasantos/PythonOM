# Quebra de linha:
# \r\n -> return CRLF
# \n -> linefeed LF

print(12, 32, 10, 11, sep="-", end='\r\n')
print(23, 5, sep=' / ', end='\n##')
print(9, 10, 11, sep="-", end='\n')
