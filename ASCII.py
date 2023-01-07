from PIL import Image

def image_to_ascii(image):
  # Open image and convert to grayscale
  img = Image.open(image).convert('L')

  # Get image dimensions
  width, height = img.size

  # Create a list of ASCII characters
  ascii_chars = [ '#', ',', ':', '*', '<', '+', 'S', '%', '@', 'A', '.']

  # Calculate pixel step size
  step_size = 256 / len(ascii_chars)

  # Create a blank string
  ascii_image = ""

  # For each pixel in the image
  for y in range(height):
      for x in range(width):
          # Get the pixel value
          pixel_value = img.getpixel((x, y))

          # Calculate which ASCII character the pixel value maps to
          ascii_char = ascii_chars[int(pixel_value / step_size)]

          # Add the ASCII character to the string
          ascii_image += ascii_char

      # Add a line break at the end of each row
      ascii_image += "\n"

  return ascii_image

# Test the function
ascii_text = image_to_ascii("Sample Image.png")

# Save the ASCII text to a file
with open("ascii_image.txt", "w") as f:
    f.write(ascii_text)
