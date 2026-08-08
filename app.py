from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import os
import re
from pypdf import PdfReader

def norm_qstn(question):
   question=question.lower()
   question=question.strip()
   question=re.sub(r"[^\w\s]","",question)
   return question

model=SentenceTransformer("all-MiniLM-L6-v2")

files=os.listdir("papers")

questions=[]
for file in files:
    if file.endswith(".pdf"):
       pdf_path=os.path.join("papers",file)
       pdf_read=PdfReader(pdf_path)

       for page in pdf_read.pages:
         text= page.extract_text()
         if text is not None:
            lines=text.split("\n")

            for line in lines:
               line=line.strip()

               if re.match(r"^Q?\d+[.)]", line):
                   line = re.sub(r"^Q?\d+[.)]\s*", "", line)
                   line=norm_qstn(line)
                   questions.append(line)               
         

frequency={}
embedding={}
for question in questions:
   embedding[question]=model.encode(question)
   
for question in questions:
   match = False
   for existing_question in frequency:
      similarity=cos_sim(embedding[question],embedding[existing_question]).item()

      

      if similarity>0.80:
         frequency[existing_question]+=1
         match =True
         break
   if not match:
         frequency[question]=1
sorted_questions=sorted(frequency.items(),key=lambda item:item[1],reverse=True)

for question, count in sorted_questions:
   print(question,"->",count)




