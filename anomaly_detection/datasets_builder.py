import os
import random

from tqdm import tqdm

train_rate=0.8
input_normal_path= '../../DeepLog0806/data/spark/normal-spark-data'
output_normal_train_path= '../../DeepLog0806/data/spark/normal-spark-train'
output_normal_test_path= '../../DeepLog0806/data/spark/normal-spark-test'

def clear_file(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write('')

def do_split_dataset():
    with open(input_normal_path, "r", encoding="utf-8") as f_data:
        with open(output_normal_train_path, "w", encoding="utf-8") as f_train:
            with open(output_normal_test_path, "w", encoding="utf-8") as f_test:
                for line in tqdm(f_data.readlines(),desc='dataset builder'):
                    if len(line.strip())==0:
                        continue
                    if random.random()<=train_rate:
                        f_train.write(line)
                    else:
                        f_test.write(line)

if __name__ == '__main__':
    do_split_dataset()

