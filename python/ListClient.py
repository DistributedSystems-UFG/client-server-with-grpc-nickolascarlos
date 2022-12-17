from __future__ import print_function
import logging

import grpc
import ListService_pb2
import ListService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = ListService_pb2_grpc.ListServiceStub(channel)

        # Get list
        response = stub.GetList(ListService_pb2.EmptyMessage())
        print('List: ' + str(response.items))

        # Append some items to the list
        stub.Append(ListService_pb2.ListItem(item=781))
        stub.Append(ListService_pb2.ListItem(item=71))
        stub.Append(ListService_pb2.ListItem(item=81))
        stub.Append(ListService_pb2.ListItem(item=78))
        stub.Append(ListService_pb2.ListItem(item=171))
        response = stub.Append(ListService_pb2.ListItem(item=99))
        print('\n\nList: \n' + str(response.items))

        # Insert an item (444) in position 3
        response = stub.Insert(ListService_pb2.ListItemInsert(item=444, position=3))
        print('\n\nList after insertion of item 444 in position 3: \n' + str(response.items))

        # Delete an item (71)
        response = stub.Delete(ListService_pb2.ListItem(item=71))
        print('\n\nList after deletion of item 71: \n' + str(response.items))

        # Search item (171), its index is returned
        response = stub.Find(ListService_pb2.ListItem(item=171))
        print('\n\nItem 171 position: \n' + str(response.position))

        # Sort list
        response = stub.Sort(ListService_pb2.ListSort(reverse=False))
        print('\n\nList after sorting: \n' + str(response.items))

        print()
    
if __name__ == '__main__':
    logging.basicConfig()
    run()