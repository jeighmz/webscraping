from bing_image_downloader import downloader

query_string = input("your search keyword: ")
downloader.download(query_string, limit=10,  output_dir='data/img/bing', 
adult_filter_off=True, force_replace=False, timeout=60)