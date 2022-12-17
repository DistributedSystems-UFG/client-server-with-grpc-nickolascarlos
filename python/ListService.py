from concurrent import futures
import logging

import grpc
import ListService_pb2
import ListService_pb2_grpc

class ListServer(ListService_pb2_grpc.ListServiceServicer):
  
  datalist = ListService_pb2.List()

  def GetList(self, request, context):
    return self.datalist

  def Append(self, request, context):
    self.datalist.items.append(request.item)
    return self.datalist

  def Insert(self, request, context):
    self.datalist = ListService_pb2.List(items=self.datalist.items[0:request.position] + [request.item] + self.datalist.items[request.position:])
    return self.datalist

  def Delete(self, request, context):
    item_index = list(self.datalist.items).index(request.item)
    self.datalist = ListService_pb2.List(items=self.datalist.items[0:item_index] + self.datalist.items[item_index + 1:])
    return self.datalist

  def Find(self, request, context):
    for (index, item) in enumerate(self.datalist.items):
      if (item == request.item):
        return ListService_pb2.ListItemPosition(position=index)
    return ListService_pb2.ListItemPosition(position = -1)

  def Sort(self, request, context):
    self.datalist.items.sort(reverse=request.reverse)
    return self.datalist

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ListService_pb2_grpc.add_ListServiceServicer_to_server(ListServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()