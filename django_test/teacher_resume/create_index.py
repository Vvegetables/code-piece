import os

from elasticsearch.client import Elasticsearch

from django_test.settings import BASE_DIR
import json

class ElasticClient:
    def __init__(self, index_name, index_type, ip="127.0.0.1"):
        '''
        @param index_name: 索引名称
        @param index_type: 索引类型
        '''
        self.index_name = index_name
        self.index_type = index_type
        
        self.es = Elasticsearch([ip])
        
    def create_index(self, index_name="teacher_resume", index_type="tr_type"):
        #创建索引
        _index_mappings = {
            "mappings": {
                self.index_type: {
                    "properties": {
                        "teachername": {
                            "type": "keyword"
                        },
                        "telephone": {
                            "type": "text"
                        },
                        "email": {
                            "type": "keyword"
                        },
                        "research_direction": {
                            "type": "array"
                        },
                        "personal_profile": {
                            "type": "text"
                        },
                        "teaching_results": {
                            "type": "text"
                        },
                        "research_results": {
                            "type": "text"
                        },
                        "lab_introduction": {
                            "type": "text"
                        },
                    }
                }
            }    
        }
        self.es.indices.create(index=self.index_name, body=_index_mappings, ignore=400)
    
    def load_index(self):
        with open(os.path.join(BASE_DIR, 'static', 'files', 'test_json.json')) as f:
            result = json.load(f)
            for item in result:
                res = self.es.index(index=self.index_name, doc_type=self.index_type, body=item)
                print(res)
                
if __name__ == "__main__":
    client = ElasticClient("teacher_resume", "tr_type")
    client.create_index()
    client.load_index()
