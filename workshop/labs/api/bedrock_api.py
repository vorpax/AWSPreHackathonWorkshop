import json
import boto3


session = boto3.Session()

bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

bedrock_model_id = "amazon.titan-text-express-v1" #set the foundation model

prompt = "Can you give me tips to quickly type Latex using neovim + vimtex + Luasnip + nvim-cmp, I'm already using nvim and I know basic commands, I've already set up the plugins. I'd like to know specific vim motions that could be useful to be faster at typing latex and particularly math in vim." #the prompt to send to the model

body = json.dumps({
    "inputText": prompt,
    "textGenerationConfig": {
        "temperature": 0,  
        "topP": 0.5,
        "maxTokenCount": 2048,
        "stopSequences": []
    }
}) #build the request payload


response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json', contentType='application/json') #send the payload to Amazon Bedrock

response_body = json.loads(response.get('body').read()) # read the response

response_text = response_body["results"][0]["outputText"] #extract the text from the JSON response

print(response_text)



