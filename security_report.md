# Project Report
## Model Analysis Report
1. Why is Embedding important and efficient?
Because Embedding can catch similar/related words, making semantic search more efficient.
It is able to capture:  
- Words with similar significent, such as synonyms with very close vector and antonimes with opposite vector.
- Associate the text with previous content, separating very similar word such as bank and bank.
- Grammar struction.
- Relation between different topic.

comparing to matching，Embedding don't require same "words"，but requiring same meaning，so it can process very complicated text.

2. Why can Embedding sometimes fail?
Main reason of embedding failing is because:

- Dataset probleme.  
 -> Not enough data.  
 -> Data bias.  
 -> Need the sample information for a spesific topic.  

- Model probleme
 -> Not enough vectors for the model.  
 -> No enough content.  
 -> Not able to understand same word with different meaning.  

- Calculating problem
 -> Similarity not good.  
 -> Top‑K not good.  
 -> need remarker to ordernize.  

3. Why is Cosine Similarity better for text?
Because text is a high concentrated mixture of vectors, meaning having a long piece of vector, but Cosine similarity only cares about what is most important thet is the angle.  
Euclidean is very affected by long vectors, so long text is not kind to Euclidean.  

4. TF-IDF vs Embedding 的差异
项目             TF-IDF               Embedding  
基础        word frequency         vector thinking  
依赖词面          a lot              not that much  
语义理解       not at all                a lot  
同义词     not able to handle       able to handle  
多语言     not able to handle       able to handle  
上下文             no                     yes  
Embedding is now the core of searching model.  

5. 如何提高语义搜索质量？  
Use a bigger Embedding model  
Use reranker  
Use better word "Separator"  
Add profetional information  
Use RAG  
Use FAISS/Milvus  

## Security Analysis Report
1. Where is the debit of Prompt Injection?  
Prompt Injection debit  
User input  
Outer info  
RAG content  

2. Prompt Injection attacking route:  
User → Input → Embedding → Retrieval → LLM → Output  
Attack is usualy in：  
- Input  
- LLM  
Embedding is bot following the rule, but changing the rule into vectors and affect final result.  

3. Why can attack be sometimes success?  
Bacause LLM can:  
- Follow user prompt  
- Cannot separate good prompt and bad prompt  
- Cannot separate system prompt and user prompt  
- Cannot dicide wether to believe or not  

4. Prompt Filter lower risk?  
- Prompt Filter can:  
- Limite input length  
- Predict bad prompt  
- Reject bad prompt  
- Clean input  
- Protect system Prompt  
- Stop bad movement  

5. System rest risk:  
- Filter can only filt basic attack  
- Cannot filt complicate attack  
- Cannot filt more than 1 attack  
- Cannot filt RAG Poisoning  
- Cannot filt Unicode  

6. How to improve？      
- Use more safe safety model  
- more filtering  
- limit authority  
- use better RAG  
- JSON spying  
