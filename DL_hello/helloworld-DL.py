import tensorflow as tf
import os
import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
os.environ["THEANO_FLAGS"] = "device=gpu0"
x = tf.placeholder("float", [None, 784])  # X是一个占位符
W = tf.Variable(tf.zeros([784, 10]))  # 权重
b = tf.Variable(tf.zeros([10]))  # 偏置量
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder("float", [None, 10])
cross_entropy = tf.reduce_sum(y_ * tf.log(y))  # 计算损失函数交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
init = tf.initialize_all_variables()  # 初始化所有变量
sess = tf.Session()
sess.run(init)
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    # 该循环的每个步骤中，我们都会随机抓取训练数据中的100个批处理数据点，
    # 然后我们用这些数据点作为参数替换之前的占位符来运行train_step。
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  # 将布尔值转换成浮点值
print(sess.run(accuracy, feed_dict={
      x: mnist.test.images, y_: mnist.test.labels}))
