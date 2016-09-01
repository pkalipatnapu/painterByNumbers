import sys
import os
from get_second_last_layer import *
# Takes input directory of images and returns a csv file with fileName,<feature vector>

train_dir = sys.argv[1]
print "Train dir = " + train_dir
output_file = sys.argv[2]
print "Output File = " + output_file
output_writer = open(output_file, 'w')

for filename in os.listdir(train_dir):
    imageName = filename.split('.')[0]
    feature_vector = run_inference_on_image(train_dir + filename)
    feature_vector_csv = ','.join(str(i) for i in feature_vector)
    output_writer.write(imageName + ',' + feature_vector_csv + '\n')
output_writer.close()
    

    

    
