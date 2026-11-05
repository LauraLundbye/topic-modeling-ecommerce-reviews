import kagglehub
import shutil
import os
import pandas as pd

def main():
    #downloadig the data from kaggle, saving it to the data folder, and loading it in
    path = kagglehub.dataset_download("nicapotato/womens-ecommerce-clothing-reviews")
    destination = "/work/LauraEmilieLundbye#6815/topic-modeling-ecommerce-reviews/data"
    shutil.copytree(path, destination, dirs_exist_ok=True)
    df = pd.read_csv(os.path.join(destination, "Womens Clothing E-Commerce Reviews.csv"))


if __name__ == "__main__":
    main()