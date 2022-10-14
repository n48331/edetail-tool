import os
src = './folders/1234_AB_S1'
print(os.listdir(src))

os.rename(src+'/1234_AB_S1_Slide-thumb.jpg', src+'/1234_AB_S2_Slide-thumb.jpg')
