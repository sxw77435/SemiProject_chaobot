import dotenv
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
import os,dotenv,glob
from flask import request, jsonify,Blueprint,render_template
from langchain.memory import ConversationBufferMemory

os.environ["OPENAI_API_KEY"] = "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"

   
dotenv.load_dotenv()

# # 파일 합치기 방법1(encoding도 잘되는법)
# directory = "C:/workspace/99_semiproject/app/python/crawling2/files"
# outfile_name = "merge_file.txt"
# out_file = open(outfile_name,'w', encoding="utf-8")
# input_files = os.listdir(directory)
# for filename in input_files:
#     if ".txt" not in filename:
#         continue
#     file = open(os.path.join(directory, filename), 'r', encoding="utf-8")
#     content = file.read()
#     out_file.write(content+"\n\n")
#     file.close()
#     print("Process done")

# #파일 합치기 방법2(encoding때문에 잘안되는 법)
# file_list = glob.glob(os.path.join('app/python/crawling2/files', '*txt'))

# with open('app/python/crawling2/files/merge.txt', 'w',encoding="UTF-8") as outfile:
#      for filename in sorted(file_list):
#         with open(filename) as file:
#             for line in file:
#                 outfile.write(line)
            

# folder_path="app/python/crawling2/files"
# file_list = os.listdir(folder_path)
# for file_name in file_list[:500]:
#     file_path = os.path.join(folder_path, file_name)
    
loader = TextLoader("merge_file.txt", encoding="UTF-8")

documents = loader.load()


text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=50)

# docs.extend(text_splitter.split_documents(documents))
docs = text_splitter.split_documents(documents)
    
    

    
# print("=================================",len(docs))
# print("=================================",docs[4])
              
   
faissIndex = FAISS.from_documents(docs, OpenAIEmbeddings())
print("faissIndex == ", faissIndex )

info_idx = "fass_taxInfo"
faissIndex.save_local(info_idx)
 
# memory = ConversationBufferMemory()

# print("docs[0] == ", docs[0]) 

# question = "혈중알코울사례 알려줘"
# query = question
# retriever = faissIndex.as_retriever(search_type="similarity", search_kwargs={"k":1})
# relevant_docs =  retriever.get_relevant_documents(query)

# num_docs = len(relevant_docs)
# print("len(relevant_docs) == ", num_docs)
# for i in range(num_docs) :
#   print("relevant_docs[", i , "] == ", relevant_docs[i])

     
     
dotenv.load_dotenv()                                   
                                      
template = """ 
{query} 중에 해당지역,해당년도 문서를 정확하게 제공하는 챗봇이다.          
       
질문에 대한 답변은 다음과 같은 형식으로 구성됩니다:          
지역: [여기에 지역을 기재합니다]
판결날짜: YYYY-MM-DD
범죄 사실: [여기에 범죄 사실을 요약하여 기재합니다] 
판결 결과: [여기에 판결 주문을 명확하게 기재합니다]       
"""
  



prompt = PromptTemplate(
    input_variables=["query"],
    template=template,
) 
   

chatbot = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),streaming=True,
        temperature=0.1, model_name="gpt-3.5-turbo",  max_tokens=500
    ), 
    chain_type="stuff",
    retriever=FAISS.load_local(info_idx, OpenAIEmbeddings())
        .as_retriever(search_type="similarity", search_kwargs={"k":1},chain_type_kwargs={"prompt":prompt})
)


      

modeling_bp = Blueprint('modeling',__name__)

@modeling_bp.route('/search', methods=['GET','POST'])
def search_cases():
    if request.method == 'POST':
        data = request.get_json()
        user_input = data.get('ask')
        # retriever = faissIndex.as_retriever(search_type="similarity", search_kwargs={"k":1})

        # relevant_docs = retriever.get_relevant_documents(user_input)
        
        question = f"{user_input}"
#         #question = f"{user_input}판결에 대해알려줘"

        print(question)

        # num_docs = len(relevant_docs)
        # print("len(relevant_docs) == ", num_docs)
        # for i in range(num_docs) :
        #   print("relevant_docs[", i , "] == ", relevant_docs[i])
        # if relevant_docs:
        #     bot_response = str(relevant_docs[0])  
        # else:
        #     bot_response = "죄송합니다.비슷한 사례를 못찾아습니다."
           
#         # full_response = template.format(region=user_input) + bot_response
        full_response = chatbot.run(prompt.format(query=question))
        return jsonify({'answer': full_response})
    else:
        return render_template('modeling.html')