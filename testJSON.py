import json

print('测试json')

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

# 我们用到了json库的loads方法
data = json.loads(sampleJson)
print(data['key2'])