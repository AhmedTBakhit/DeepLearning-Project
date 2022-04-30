from pathlib import Path
data_dir = "D:/data/cougerNotaCouger/"

def load_img(self, dir):
    """open image file, replace all '-10000' transparent values with zero, and return"""
    image_path = str(
        list(
            Path(dir.glob(
                f"*.*"
            )
        )[0]
    ))
    return image_path

image = cv.imread(image_path, cv.IMREAD_UNCHANGED)

from pathlib import Path
import glob
import cv2 as cv

data_dir = "D:\\data\\cougerNotaCouger\\coug"
labels = ["filename, coug"]

# for name in glob.glob(f'{data_dir}/*[0-9].*'):
#     print(name)

for i, path in enumerate(Path(data_dir).rglob('*.*')):
    pathname = str(path)
    print(pathname)
    
        # print(pathname)
    image = cv.imread(pathname)
    
    # cv.imwrite(image, f"{data_dir}/coug_{i}.png")
    filename = f"{str(data_dir)}\\coug_{i}.png"
    cv.imwrite(filename, image)
    labels.append(f"coug_{i}.png, 1")
    # cv.imwrite(image, f"{data_dir}coug{i}.png")