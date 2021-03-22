# Importing libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image = Image.open(r"C:\Users\HP\Desktop\Classroom Materials\Competitive Programming\programs for submission\StreamlitApps\BioInformaticsApp\dna-logo.jpg")
st.image(image,use_column_widht=True)
st.write("""

# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
	""")

# Input Text Box
st.header("Enter DNA Sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # skip the sequence name (first line)
sequence = ''.join(sequence) # concatenates list to string
st.write("""

***

""")

# Prints the input DNA Sequence
st.header("INPUT (DNA Query)")
sequence

## DNA nucleotide count
st.header("OUTPUT (DNA Nucleotide Count)")


## Print Dictionary
st.subheader("1. Print Dictionary")
def DNA_nucleotide_count(seq):
	d=dict([
	('A',seq.count('A')),
	('T',seq.count('T')),
	('G',seq.count('G')),
	('C',seq.count('C'))
	])
	return d

X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())

X

### 2. Print text
st.subheader("2. Print text")
st.write("There are "+str(X['A'])+' adenine (A)')
st.write("There are "+str(X['T'])+' thymine (T)')
st.write("There are "+str(X['G'])+' adenine (guanine)')
st.write("There are "+str(X['C'])+' thymine (cytosine)')

## 3. Display Dataframe
st.subheader('3. Display Dataframe')
df=pd.DataFrame.from_dict(X, orient='index')
df=df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader("4. Display Bar Chart ")
p=alt.Chart(df).mark_bar().encode(
x="nucleotide",
y="count"
)
p=p.properties(
width=alt.Step(80) # width of bar
)
st.write(p)
