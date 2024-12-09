import binascii
import tempfile

from PIL import Image
import base64


def image_to_text(image_path):
    """Convert image to base64-encoded text."""
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()
        encoded_str = base64.b64encode(img_data).decode('utf-8')
        return encoded_str


def text_to_image(encoded_str, output_path):
    """Convert base64-encoded text back to image."""

    # Ensure correct padding for the base64 string
    missing_padding = len(encoded_str) % 4
    if missing_padding:
        encoded_str += '=' * (4 - missing_padding)

    try:
        decoded_img_data = base64.b64decode(encoded_str)

        # Save the decoded image data to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(decoded_img_data)
            temp_file_path = temp_file.name

        print(f"Temp Image saved as {temp_file_path}")

        # Rename or move the temporary file to the desired output path
        import shutil
        shutil.move(temp_file_path, output_path)

        print(f"Image saved as {output_path}")

    except binascii.Error as e:
        print(f"Error decoding base64 string: {e}")

if __name__ == "__main__":
    # Path to the image file
    image_path = './res/drawable/email-icon.png'

    # # Convert image to text
    # encoded_text = image_to_text(image_path)
    # print("Encoded Text:", encoded_text[:50], "...")  # Displaying first 50 characters of the encoded text

    encoded_text = "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAACX"
    # Convert text back to image
    output_image_path = 'decoded_image.jpg'
    text_to_image(encoded_text, output_image_path)
    print(f"Image saved as {output_image_path}")
