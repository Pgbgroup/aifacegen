import requests
from io import BytesIO
from PIL import Image
n=1408
def download_image(save_path):
    url = "https://thispersondoesnotexist.com/"
    response = requests.get(url)

    if response.status_code == 200:
        image_bytes = BytesIO(response.content)
        image = Image.open(image_bytes)
        image.save(save_path)
        print(f"Image downloaded and saved at {save_path}")
    else:
        print(f"Failed to download image. Image status code: {response.status_code}")
        
while True:
    if __name__ == "__main__":
        n+=1
        save_path = "downloaded_image"+str(n)+".jpg"
        download_image(save_path)
