import tensorflow as  tf
sess = tf.Session()
W = tf.Variable([.3],tf.float32)
B = tf.Variable([-.3],tf.float32)
x = tf.placeholder(tf.float32)
linear_mode = W*x+B
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_mode,{x:[1,2,3,4]}))