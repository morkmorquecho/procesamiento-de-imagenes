import tensorflow as tf

matrizA = tf.constant([[1,2,-3],[4,0,2]])
matrizB = tf.constant([[3,1],[2,4], [-1,5]])

product = tf.matmul(matrizA, matrizB)

sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

