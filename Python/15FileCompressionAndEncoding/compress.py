import zlib,base64

data =  open('demo.txt','r').read()
data_bytes = bytes(data,'utf-8')# string to bytes

# Compressing the byte type data and then encoding(string->byte) it, which returns byte as well:

compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
decoded_data = compressed_data.decode('utf-8')
# bytes to string
compressed_file = open('compressed.txt','w')
compressed_file.write(decoded_data)

# decompressing(byte data) and then decoding(byte->string) the returned byte data from above:

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
decoded_data2 = decompressed_data.decode('utf-8')
decompressed_file = open('decompressed.txt','w')
decompressed_file.write(decoded_data2)
decompressed_file.close()

# Note:i) Both string and byte data can be encoded and compressed OR decoded and decompressed, the only difference is: Byte data can directly be decompressed OR compressed, while String data needs Encoding to transform into Byte data before going through Compression, and Decompressed file always return data in Bytes, so if those Bytes were text orginally, we need to Decode those Bytes back to String.