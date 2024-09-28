# Image Generator

## Description
The Image Generator is a simple GUI application built using Python that allows users to generate and download random images based on specified categories from the Unsplash API. The application is user-friendly, featuring a straightforward interface built with Tkinter and ttkbootstrap.

## Features
- Input a category to retrieve a random image from Unsplash.
- Display the generated image in the GUI.
- Download the displayed image to your local machine.

## Requirements
To run this project, ensure you have the following Python packages installed:
- `requests`
- `Pillow`
- `ttkbootstrap`

You can install these packages using pip:

```bash
pip install requests
pip install Pillow
pip install ttkbootstrap

Usage
Run the Application: Execute the script using Python:

bash
Copy code
python image_generator.py
Generate an Image:

Enter a category (e.g., "nature", "technology", "cars") in the input field.
Click the "Generate Image" button to fetch a random image.
Download the Image:

Once the image is displayed, click the "Download Image" button to save it to your local directory as downloaded_image.jpg.
Code Explanation
Main Window: The application uses Tkinter to create a GUI window where users can interact with the app.
Image Retrieval: The app retrieves a random image based on the user’s input category from the Unsplash API.
Image Display and Download: The fetched image is displayed in the GUI, and users can download it with a click.
Screenshots
(You can add screenshots of the application in use here)

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Unsplash API for providing high-quality images.
Tkinter for the GUI framework.
Pillow for image handling.
Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

Contact
For any inquiries, please contact Your Name.
