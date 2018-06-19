import tensorflow as tf
from generate import getBatch

def main():
    x=tf.placeholder(tf.float32,[None,2],name="input")
    W = tf.Variable(tf.zeros([2, 2]),name="weight")
    b = tf.Variable(0.0,name="bias")
    predicted_y = tf.add(tf.matmul(x, W),b,name="result")
    print(predicted_y)
    loss=tf.reduce_mean(tf.abs(predicted_y-100))


    print("@loss")
    saver=tf.train.Saver()
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
    train_op = optimizer.minimize(
        loss=loss,
        global_step=tf.train.get_global_step())
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    for _ in range(1000):
        batch_xs= getBatch()
        print(sess.run(train_op, feed_dict={x: batch_xs}))
    saver.save(sess,"C:/Python35/puzzle15ML/modeldir/model.ckpt")



main()
