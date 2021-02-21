import streamlit as st
from PIL import Image
import shutil
import os
def main(image):
	img=Image.open(image)
	value = st.slider("Select the optimize values : ",min_value=0, max_value=15,value=15)
	st.write("You have selected :", value)
	col1,col2=st.beta_columns(2)
	with col1:
		st.header("Original Image")
		st.image(image,caption=str(len(img.fp.read())/1000)+" KB",use_column_with=True)
	res="result.jpeg"
	img.save(res,optimize=True, quality=value)
	with col2:
		header="Result"
		st.header(header)
		st.image(res,caption=str(os.path.getsize(res)/1000)+" KB",use_column_with=True)
	if st.button("Save"):
		shutil.move(res,"C:\\Users\\HP\\desktop\\"+res)
		st.write("File Saved on Desktop")
	else:
		st.write("Not Saved!!!")
def pick():
	filename = st.file_uploader("Upload a file")
	if filename:
		main(filename)
	else:
		st.write("No File Uploaded!!!")
if __name__ == '__main__':
	st.title("Image Optimizer with Pillow")
	pick()