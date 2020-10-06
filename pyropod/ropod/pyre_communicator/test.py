import logging
from ropod.pyre_communicator.base_class import RopodPyre
import zmq
from ropod.utils.uuid import generate_uuid
import time


if __name__ == '__main__':

    # logging.getLogger('pyre').setLevel(logging.WARNING)
    # logging.getLogger("requests").setLevel(logging.WARNING)

    # logging.basicConfig(format="%(asctime)s [%(name)-12.12s] [%(levelname)-5.5s]  %(message)s",
    #                     level=logging.DEBUG)

    ctx = zmq.Context()

    n_nodes = 15
    node_names = ['node_' + str(i) for i in range(0, n_nodes)]
    nodes = list()

    zyre_config = {"groups": ["TEST-GROUP"],
                   "message_types": ["TEST_MSG"],
                   "ctx": ctx}

    for node_name in node_names:
        zyre_config.update(node_name=node_name)
        node = RopodPyre(zyre_config)
        # node.start()
        nodes.append(node)

    time.sleep(5)
    for node in nodes:
        print("starting node: ", node.name())
        node.start()
        time.sleep(5)


    # node1.shutdown()
    # node2.shutdown()
    # node3.shutdown()
