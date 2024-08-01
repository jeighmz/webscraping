from google_images_download import google_images_download

def download_images(keyword, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword, "limit": limit, "output_directory": "data/img/google"}
    response.download(arguments)
    # store them locally
    print("Downloaded images for keyword: ", keyword)


if __name__ == "__main__":
    keyword = input("your search keyword: ")
    limit = 10
    download_images(keyword, limit)

# Deprecrated