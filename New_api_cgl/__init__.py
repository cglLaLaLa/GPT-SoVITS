from New_api_cgl.internal.common.util.singleton_concurrent_hashmap import SingletonConcurrentHashMap
import os

#切分音频时使用 key:uid value:用户文件夹下的音频文件
userSliceMap = SingletonConcurrentHashMap.__new__(SingletonConcurrentHashMap)

SLICE_GRPC_PORT = '50051'

NOW_DIR = os.getcwd()
os.environ["SLICE_ENV"] = NOW_DIR