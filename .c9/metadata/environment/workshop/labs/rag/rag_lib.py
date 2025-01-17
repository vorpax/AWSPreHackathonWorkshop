{"filter":false,"title":"rag_lib.py","tooltip":"/workshop/labs/rag/rag_lib.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["import itertools","import boto3","import chromadb","from chromadb.utils.embedding_functions import AmazonBedrockEmbeddingFunction",""],"id":1}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["def get_collection(path, collection_name):","    session = boto3.Session()","    embedding_function = AmazonBedrockEmbeddingFunction(session=session, model_name=\"amazon.titan-embed-text-v2:0\")","    ","    client = chromadb.PersistentClient(path=path)","    collection = client.get_collection(collection_name, embedding_function=embedding_function)","    ","    return collection",""],"id":3}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["def get_vector_search_results(collection, question):","    ","    results = collection.query(","        query_texts=[question],","        n_results=4","    )","    ","    return results",""],"id":5}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":26,"column":0},"end":{"row":63,"column":0},"action":"insert","lines":["def get_rag_response(question):","","    session = boto3.Session()","    bedrock = session.client(service_name='bedrock-runtime')","    ","    collection = get_collection(\"../../data/chroma\", \"bedrock_faqs_collection\")","    ","    search_results = get_vector_search_results(collection, question)","    ","    flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb","    ","    rag_content = \"\\n\\n\".join(flattened_results_list)","    print(rag_content)","    ","    message = {","        \"role\": \"user\",","        \"content\": [","            { \"text\": rag_content },","            { \"text\": \"Based on the content above, please answer the following question:\" },","            { \"text\": question }","        ]","    }","    ","    response = bedrock.converse(","        modelId=\"anthropic.claude-3-sonnet-20240229-v1:0\",","        messages=[message],","        inferenceConfig={","            \"maxTokens\": 2000,","            \"temperature\": 0,","            \"topP\": 0.9,","            \"stopSequences\": []","        },","    )","    ","    return response['output']['message']['content'][0]['text'], flattened_results_list","","",""],"id":7}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":8}]]},"ace":{"folds":[],"scrolltop":340,"scrollleft":0,"selection":{"start":{"row":25,"column":0},"end":{"row":25,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1737154478444,"hash":"4d8cd4dcc6cc16e24f611602933c40c583eb7e52"}