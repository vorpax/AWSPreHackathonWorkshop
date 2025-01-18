{"filter":false,"title":"create_guardrail.py","tooltip":"/workshop/labs/guardrails/create_guardrail.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["import boto3, json, random, string",""],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":47,"column":38},"action":"insert","lines":["client = boto3.client(service_name='bedrock') #creates a Bedrock client","","response = client.create_guardrail(","    name=\"Guardrail-from-Code-\" + \"\".join(random.choices(string.ascii_lowercase, k=8)),","    description='string',","    topicPolicyConfig={","        'topicsConfig': [","            {","                \"name\": \"Bitcoin\",","                \"definition\": \"Providing advice, direction, or examples of how to mine, use, or interact with Bitcoin, including Cryptocurrency-related third-party services.\",","                \"examples\": [","                    \"How do I mine Bitcoin?\",","                    \"What is the current value of BTC?\",","                    \"Which instance is the best for crypto mining?\",","                    \"Is mining cryptocurrency against the terms?\",","                    \"How do I maximize my Bitcoin profits?\",","                ],","                \"type\": \"DENY\",","            }","        ]","    },","    contentPolicyConfig={","        'filtersConfig': [","            {\"type\": \"SEXUAL\", \"inputStrength\": \"HIGH\", \"outputStrength\": \"HIGH\"},","            {\"type\": \"HATE\", \"inputStrength\": \"HIGH\", \"outputStrength\": \"HIGH\"},","            {\"type\": \"VIOLENCE\", \"inputStrength\": \"HIGH\", \"outputStrength\": \"HIGH\"},","            {\"type\": \"INSULTS\", \"inputStrength\": \"HIGH\", \"outputStrength\": \"HIGH\"},","            {\"type\": \"MISCONDUCT\", \"inputStrength\": \"HIGH\", \"outputStrength\": \"HIGH\"},","            {\"type\": \"PROMPT_ATTACK\", \"inputStrength\": \"HIGH\", \"outputStrength\": \"NONE\"},","        ]","    },","    wordPolicyConfig={","        \"wordsConfig\": [{\"text\": \"AnyCompany\"}],","        \"managedWordListsConfig\": [{\"type\": \"PROFANITY\"}],","    },","    sensitiveInformationPolicyConfig={","        \"piiEntitiesConfig\": [","            {\"type\": \"NAME\", \"action\": \"ANONYMIZE\"},","            {\"type\": \"EMAIL\", \"action\": \"ANONYMIZE\"},","        ],","    },","    blockedInputMessaging=\"Apologies, this model cannot be used to discuss inappropriate or off-topic content.\",","    blockedOutputsMessaging=\"Apologies, the model's response to your request was blocked.\",",")","","guardrail_id = response['guardrailId']"],"id":3}],[{"start":{"row":47,"column":38},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":49,"column":0},"end":{"row":51,"column":1},"action":"insert","lines":["response = client.create_guardrail_version(","    guardrailIdentifier=guardrail_id,",")"],"id":5}],[{"start":{"row":51,"column":1},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":53,"column":0},"end":{"row":55,"column":0},"action":"insert","lines":["","print(guardrail_id)",""],"id":7}]]},"ace":{"folds":[],"scrolltop":356.9999910593036,"scrollleft":0,"selection":{"start":{"row":55,"column":0},"end":{"row":55,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1737202203349,"hash":"99dabb61437daa736a4f9096b381d6b40e893527"}