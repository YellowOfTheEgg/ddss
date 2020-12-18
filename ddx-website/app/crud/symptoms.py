from . import knowledge_base

#read operation from crud for getting symptoms
def get():
    return list(knowledge_base.get().keys())
