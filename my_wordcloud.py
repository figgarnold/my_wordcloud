import os, sys
from PIL import Image #mport the Image module from pillow
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


#set parent directory
current_directory = os.path.dirname(__file__)

#set image as a variable
sausage_image_path = os.path.join(current_directory, "sausage.png")
sausage_image = Image.open(sausage_image_path)

#creates a pixel array (255 represents "white")
sausage_mask = np.array(sausage_image)
print(sausage_mask)

#read in text str from .txt file
with open(os.path.join(current_directory, "cloudtext.txt")) as f:
  lyrics = f.read()

#generate wordcloud
wordcloud = WordCloud(background_color="white", mask=sausage_mask, collocations=False, stopwords=STOPWORDS, contour_color="white", contour_width=1)

wordcloud.generate(lyrics)

#used print statement to debug and then commented out
#print(wordcloud)

image_colors = ImageColorGenerator(sausage_mask)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()