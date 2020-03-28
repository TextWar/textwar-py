import sys
import traceback
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
import json
import wild
import town

# file = open("maps/town/town_1.json","r")
# json_ = json.load(file)
# array = []

# arrayx = town.Town(array,hash_map=json_["hashmap"]).array
# arrayx[20][20] = "908950"
# town.Town(arrayx,hash_map=json_["hashmap"]).update()
# dict_ = {json_["hashmap"]: ""}
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/textwar',)


if __name__ == "__main__":
    with SimpleXMLRPCServer(('localhost', 3000),
                            requestHandler=RequestHandler) as server:
        server.register_introspection_functions()
        server.register_multicall_functions()


        @server.register_function
        def get_map(type):
            try:
                map_ = wild.WildMap()
                map_.init_array()
                a = {"hashmap": ["*　","░░"], "type": 2, "name": "some", "author": "someone behind the screen", "version": "b1",
                     "map": map_.generate().array}
                return json.dumps(a)
            except:
                traceback.print_exc(file=sys.stdout)
                return sys.stdout



        @server.register_function
        def update_map(file, json_):
            try:
                print(json_,file)
                obj = json.loads(json_)
                array = []
                for i, c in enumerate(obj["map"]):
                    new = []
                    for ib, str__ in enumerate(c):
                        if type(str__) == int:
                            str__ = str(str__)
                        new.append(str__)
                    array.append(new)
                if obj["type"] == 1:
                    map_ = wild.WildMap(array)
                    map_.file = file
                    return map_.update().file
                else:
                    map_ = town.Town(array,hash_map=obj["hashmap"])
                    map_.file = file
                    return map_.update().file
            except Exception as e:
                traceback.print_exc(file=sys.stdout)

        print("XmlRpc server is started")
        server.serve_forever()
