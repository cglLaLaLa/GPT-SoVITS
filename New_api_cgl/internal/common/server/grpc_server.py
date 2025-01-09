import grpc

from concurrent import futures
import os

from more_itertools.more import side_effect

from New_api_cgl import userSliceMap, SLICE_GRPC_PORT, NOW_DIR
from tools import my_utils
from tools.my_utils import load_audio, check_for_existance, check_details
from subprocess import Popen
from config import python_exec,infer_device,is_half,exp_root,webui_port_main,webui_port_infer_tts,webui_port_uvr5,webui_port_subfix,is_share

from New_api_cgl.internal.common.genproto.slice_pb import start_slice_pb2_grpc, start_slice_pb2

class SliceService(start_slice_pb2_grpc.SliceServiceServicer):
    def StartSlice(self, request, context):
        uid = "test_001"
        inp =  "/home/cgl/slice/input" + uid
        out =  "/home/cgl/slice/output" + uid
        res =  open_slice(uid,inp,out,request.threshold,request.min_length,request.min_interval,request.max_sil_kept,request._max,request.alpha,request.n_parts)
        data = []
        uid_data = start_slice_pb2.KeyValuePair(key='uid', value=uid)
        res_data = start_slice_pb2.KeyValuePair(key='res', value=res)
        data.append(uid_data)
        data.append(res_data)
        return start_slice_pb2.StartResponse(
            status = "1",
            data = data,
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    start_slice_pb2_grpc.add_SliceServiceServicer_to_server(SliceService(), server)
    server.add_insecure_port('[::]:' + SLICE_GRPC_PORT)
    server.start()
    server.wait_for_termination()



def open_slice(uid,inp,opt_root,threshold,min_length,min_interval,hop_size,max_sil_kept,_max,alpha,n_parts):
    ps_slice= userSliceMap.get(uid)
    inp = my_utils.clean_path(inp)
    opt_root = my_utils.clean_path(opt_root)
    check_for_existance([inp])
    if(os.path.exists(inp)==False):
        os.mkdir(inp)
    if (os.path.exists(opt_root) == False):
        os.mkdir(opt_root)
    if os.path.isfile(inp):n_parts=1
    elif os.path.isdir(inp):pass
    else:
        #yield "输入路径存在但既不是文件也不是文件夹", {"__type__":"update","visible":True}, {"__type__":"update","visible":False}, {"__type__": "update"}, {"__type__": "update"}, {"__type__": "update"}
        return "输入路径存在但既不是文件也不是文件夹"
    if (ps_slice == []):
        for i_part in range(n_parts):
            cmd = '"%s" tools/slice_audio.py "%s" "%s" %s %s %s %s %s %s %s %s %s''' % (python_exec,inp, opt_root, threshold, min_length, min_interval, hop_size, max_sil_kept, _max, alpha, i_part, n_parts)
            print(cmd)
            p = Popen(cmd, shell=True)
            ps_slice.append(p)
        for p in ps_slice:
            p.wait()
        userSliceMap.remove(uid)
        return "切割结束"
    else:
        return "已有正在进行的切割任务"


if __name__ == "__main__":
    serve()
















