# # Add your virtual environment path if needed
import io
import os
import platform
from google.cloud import storage, vision


"""
Use this script to OCR images.
"""

# Get OS name
host_os_name = platform.system()


def detect_text(
    client,
    path_of_image_file,# path to image fule
    root_for_image,# root folder where the image is located
    path_for_converted_images,# folder where the converted image will be moved
    path_for_converted_txt,# folder where txt file will be saved
    host_os_name,# detect Windows OS or otherwise
):
    """Detects text in the file."""
    with io.open(path_of_image_file, "rb") as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(
        image=image
    )  # client.text_detection(image=image)#change to client.document_text_detection(image=image) for scanned books
    texts = response.text_annotations[0].description
    print(f"Texts:\n{texts}")
    # Generate file name to save ocr text.
    # split file path to get filename
    path_of_image_file_head, path_of_image_file_tail = os.path.split(path_of_image_file)
    # generate txt file path
    txt_file_name = path_of_image_file_tail + ".txt"
    txt_file_path = os.path.join(path_for_converted_txt, txt_file_name)
    # write to txt file
    if host_os_name == "Windows":
        with open(txt_file_path, "w", encoding="utf-8") as tfn:
            tfn.write(texts)
    else:
        with open(txt_file_path, "w") as tfn:
            tfn.write(texts)
    # move image to converted folder
    os.rename(
        path_of_image_file,
        path_of_image_file.replace(root_for_image, path_for_converted_images),
    )


if __name__ == "__main__":

    # Set up environment to provide secret key.
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_secret_key.json"

    client = vision.ImageAnnotatorClient()
    single_or_multi = input(
        "Do you want to OCR single image(1) or a set of images in a folder(2)?"
    )
    if single_or_multi == str(1):
        path_of_single_file = input("enter path of image here\n")
        path_of_single_file_root = os.path.split(path_of_single_file)[0]
        # now detect text
        detect_text(
            client,
            path_of_single_file,  # path to image file
            path_of_single_file_root,  # root folder where image is located
            path_of_single_file_root,  # path where converted image will be moved
            path_of_single_file_root,  # path where txt file will be saved
            host_os_name,  # to recognize Windows platform
        )
    else:
        folder_path = input("Enter folder path here.\n")
        if os.path.isdir(folder_path):
            if not folder_path.endswith("/"):
                folder_path = os.path.join(folder_path, "")

            # create folders to move converted images and ocr txt.
            path_for_converted_images = os.path.join(folder_path, "converted", "")
            path_for_txt = os.path.join(folder_path, "txt", "")

            # list all dir and files in the path provided.
            all_files_n_folders = os.listdir(folder_path)
            all_files = [
                os.path.join(folder_path, item)
                for item in all_files_n_folders
                if os.path.isfile(os.path.join(folder_path, item))
            ]

            if len(all_files) > 0:
                if not os.path.isdir(path_for_converted_images):
                    os.makedirs(path_for_converted_images)
                if not os.path.isdir(path_for_txt):
                    os.makedirs(path_for_txt)
                try:
                    for path_of_item in all_files:
                        print(path_of_item)
                        if os.path.isfile(path_of_item) and path_of_item.endswith(
                            (".jpg", ".png")
                        ):  # add more formats here, if needed

                            try:
                                detect_text(
                                    client,
                                    path_of_item,  # path to image file
                                    folder_path,  # folder where image file is located
                                    path_for_converted_images,  # folder where converted image will be moved after conversion
                                    path_for_txt,  # folder where txt file will be saved
                                    host_os_name,  # detect Windows.
                                )

                            except Exception as x:
                                print(x)

                        elif os.path.isfile(path_of_item) and path_of_item.endswith(
                            ".txt"
                        ):
                            os.rename(
                                path_of_item,
                                path_of_item.replace(folder_path, path_for_txt),
                            )
                        elif os.path.isfile(path_of_item) or os.path.isdir(
                            path_of_item
                        ):
                            print("this file is either not an image or it was not added in script as allowed type.")
                except Exception as x:
                    print(x)
            else:
                print("No images available.")
