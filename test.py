"""script is generated from a tutorial on metaflow site"""
import tensorflow as tf
import os
import argparse
from generate import getBatch

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the 
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it 
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="prefix")
    return graph
if __name__ == '__main__':
    
    # We use our "load_graph" function
    graph = load_graph("C:/Python35/puzzle15ML/frozen_model.pb")

    # We can verify that we can access the list of operations in the graph
    for op in graph.get_operations():
        print(op.name)
    

    x = graph.get_tensor_by_name("prefix/input:0")
    y = graph.get_tensor_by_name("prefix/result:0")
    b=graph.get_tensor_by_name("prefix/bias:0")
    w=graph.get_tensor_by_name("prefix/weight:0")
    
        
    # We launch a Session
    with tf.Session(graph=graph) as sess:
        batch_xs= getBatch(10)
        print(batch_xs)
        print(sess.run(y, feed_dict={x: batch_xs}))
        print(sess.run(w))
        
            #print(score)
        
    
