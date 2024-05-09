from glob import glob
train_img_list = glob(r'C:\Users\WSU\vscode\maritime detection\yolov5\dataset\train\images\*.jpg')
valid_img_list = glob(r'C:\Users\WSU\vscode\maritime detection\yolov5\dataset\valid\images\*.jpg')
test_img_list = glob(r'C:\Users\WSU\vscode\maritime detection\yolov5\dataset\test\images\*.jpg')
print(len(train_img_list), len(valid_img_list), len(test_img_list))

import yaml
if len(train_img_list) > 0:
    with open(r'C:\Users\WSU\vscode\maritime detection\yolov5\dataset\train.txt','w') as f:
        f.write('\n'.join(train_img_list) + '\n')
    with open(r'C:\Users\WSU\vscode\maritime detection\yolov5\dataset\val.txt','w') as f:
        f.write('\n'.join(valid_img_list) + '\n')
    with open(r'C:\Users\WSU\vscode\maritime detection\yolov5\dataset\test.txt','w') as f:
        f.write('\n'.join(test_img_list) + '\n')
else:
    print("not found")
