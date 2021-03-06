import tensorflow as tf

x_data = [1., 2., 3.]
y_data = [1., 2., 3.]


W = tf.Variable(tf.random_uniform([1], -10.0, 10.0))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = W * X


cost = tf.reduce_mean(tf.square(hypothesis - Y))
descent = W - tf.multiply(0.1, tf.reduce_mean(tf.multiply((tf.multiply(W, X) - Y), X)))
update = W.assign(descent)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(1, 101):
    sess.run(update, feed_dict={X:x_data, Y:y_data})
    print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))
