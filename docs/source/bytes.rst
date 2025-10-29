================
Bytes
================

In Python, ``bytes`` is a type used to store and manipulate data. A byte consists of 8 bits, and it can represent 256 different values (2^8). 
Each bit can be either 0 or 1, which allow the creation of a wide range of binary patterns.

One of the most typical use cases is string encoding. 
These encodings are standards used to represent sets of characters, which can be used to handle text that contains characters not included in the english alphabet. 

Let’s see an example:

.. code-block:: python
   :linenos:

    # Encoding a string with german characters using latin-1 encoding
    german_text = "Übergrößenträger"
    ENCODING_FORMAT = "latin-1"
    encoded_bytes = german_text.encode(ENCODING_FORMAT)
    print(type(encoded_bytes))  # => <class 'bytes'>
    print(encoded_bytes)  # => b'\xdcbergr\xf6\xdfentr\xe4ger'

    # Decoding latin-1 bytes back to a string
    decoded_string = encoded_bytes.decode(ENCODING_FORMAT)
    print(decoded_string)  # => "Übergrößenträger"

    some_bytes = b"jim"  # Can also be created this way
    print(type(some_bytes))  # => <class 'bytes'>

Learn more: https://docs.python.org/3/howto/unicode.html.

.. note::

    It's common to see external network services that only accept data in byte format instead of string. 
    By writing and transmitting string texts as bytes, you ensure compatibility with these services, 
    and prevent potential representation issues when decoding the text back to string.


The capabilities of bytes are not limited to data in text format. It can also handle external files stored as binary data, such as images, audio files and more! 
You can see the contents of an image file as bytes:

.. code-block:: python
   :linenos:

    # Open the image file in binary mode (“rb”)
    with open("some_image.jpg", "rb") as file:
        # Read the image bytes
        image_bytes = file.read()

    # Print the first 9 bytes of the image
    print(image_bytes[:10])  # => b'\xff\xd8\xff\xe0\x00\x10JFIF'


.. image:: https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHh4OTZpcGh0Y3BlZjFyd3R6Yml0N3ZtZTNrOWh6Y2R2eDM5MmVpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EBId5v0YNRyPGHytLK/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------

You may be wondering why someone would want to open an image file in this cryptic format...
It turns out that manipulating bytes is more powerful than it looks. 
This technique can be used to alter the image itself, such as applying filters, changing colors, and even file compression! 

Another peculiar use case is **steganography**, which can be used to conceal secret messages into the file itself, only visible if the file is opened in binary mode, then decoded back into string.

.. image:: https://y.yarn.co/b55b68b6-fc2e-4de1-912c-b44502c0e208_text.gif
   :alt: Description of the animation
   :align: center
   
---------------------------

.. note::

    Steganography is the practice of representing information within another message or physical object, in such a manner that the presence of the information is not evident to human inspection.
