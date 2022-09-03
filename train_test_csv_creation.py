import os
import random

"""
The follwing function is createing two csv file for tarin and test data
train.csv will hold the info train data and
test.csv will hold the photo of test data 
train.csv will hold the image name and the label of that image
test.csv will hold only the image name
"""
def create_train_test_csv():
    fp_train = open('Dataset_from_fundus_images_for_the_study_of_diabetic_retinopathy_V02/train.csv', 'a')
    fp_train.write('Image' + "," + "Status" + "\n")
    fp_test = open('Dataset_from_fundus_images_for_the_study_of_diabetic_retinopathy_V02/test.csv', 'a')
    fp_test.write("Image" + "\n")

    for folder in os.listdir('Dataset_from_fundus_images_for_the_study_of_diabetic_retinopathy_V02'):
        if os.path.isdir('Dataset_from_fundus_images_for_the_study_of_diabetic_retinopathy_V02/{}'.format(folder)):
            file_list = os.listdir('Dataset_from_fundus_images_for_the_study_of_diabetic_retinopathy_V02/{}'.format(folder))
            total_train = int(len(file_list)*0.8)
            train_count = 0
            status = folder.split(".")[1].strip()
            random.shuffle(file_list, shuffleorder)
            for eachfile in file_list:
                if train_count <= total_train:
                    fp_train.write(eachfile + "," + status + "\n")
                    train_count += 1
                    continue
                fp_test.write(eachfile + "\n")
    
    fp_train.close()
    fp_test.close()

    return 


"""
This function will ensure the shuffling in same order for all the directory
"""
def shuffleorder():
    return 0.2

if __name__ == "__main__":
    create_train_test_csv()