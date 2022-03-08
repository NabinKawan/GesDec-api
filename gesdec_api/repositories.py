from fastapi.responses import FileResponse

class ModelRepository:
    path='gesdec_api/model_files'
    
    @staticmethod
    def get_model():
       return FileResponse(f'{ModelRepository.path}/model.json')
    
    @staticmethod
    def _get_shar1of1():
        return FileResponse(f'{ModelRepository.path}/group1-shard1of1.bin')
    
    # @staticmethod
    # def _get_shar2of3():
    #     return FileResponse(f'{ModelRepository.path}/group1-shard2of3.bin')    
 
    # @staticmethod
    # def _get_shar3of3():
    #     return FileResponse(f'{ModelRepository.path}/group1-shard3of3.bin')