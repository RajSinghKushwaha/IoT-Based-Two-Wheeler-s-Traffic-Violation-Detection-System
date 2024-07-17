import os
train_img_path = "dataset/images/train"
val_img_path = "dataset/images/val"

#Training images
with open('dataset/train.txt',"a+") as f:
    img_list = os.listdir(train_img_path)
    for img in img_list:
        f.write(os.path.join(train_img_path,img+'\n'))
    print("Done")

#Validation image
with open('dataset/val.txt', "a+") as f:
    img_list = os.listdir(val_img_path)
    for img in img_list:
        f.write(os.path.join(val_img_path,img+'\n'))
    print("Done")