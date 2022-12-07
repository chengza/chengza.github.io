目前算得上流行的联邦学习框架有微众银行的FATE、海外社区开发的Flower和FedML。FATE是一个工业级框架，比较全面，但是我猜测可能太重量级，所以此次不选择它，FedML和Flower相差不大，Flower明确不支持纵向联邦学习，FedML很可能也不支持。我选择FedML因为它应该是体量适中，并且根据谷歌学术搜索结果来看使用量还可以。



# 安装与部署

官方文档在 https://doc.fedml.ai/ 。

安装方式有很多，简单起见我选择使用 pip 安装。首先建立一个conda虚拟环境。

```
conda create -n federated python=3.9 --yes
conda activate federated
```

由于网速还不错，代理速度够快，进度条唰唰唰地走。注意到其中有一个比较慢的步骤，是在安装torch，也就是说FedML默认依赖了PyTorch，但愿配合良好。

官方文档说，默认使用torch，如果愿意，也可以一键安装其他框架的版本。

```
pip install "fedml[tensorflow]"
pip install "fedml[jax]"
pip install "fedml[mxnet]"
```

官方文档在命令之后标注说仅在linux上保证成功，再mac和PC上需要参考torch的说明解决错误。而如果使用conda安装，则还要求使用python3.7，否则可能遇到兼容性问题，虽然后续版本有计划支持。

# 模拟实验

FedML有好几种模式，针对不同用途设计，我使用FedML Parrot执行模拟联邦学习实验。

[FedML Parrot User Guide &mdash; FedML documentation](https://doc.fedml.ai/simulation/user_guide.html)

我选择一个单进程模拟实验的案例。具体代码在 [FedML/python/examples/simulation/sp_fedavg_mnist_lr_example at master · FedML-AI/FedML · GitHub](https://github.com/FedML-AI/FedML/tree/master/python/examples/simulation/sp_fedavg_mnist_lr_example) 。实际上，这里的代码其实只是调用了FedML里的函数，没有实现什么东西。比如一行命令就跑起来的版本实际上代码就只有

```
import fedml


if __name__ == "__main__":
    fedml.run_simulation()
```

结论是，对于模拟实验，如果不大幅修改联邦学习算法中的任何一个部分，仅仅使用现成的构造，那么其实只需要编辑配置文件即可。真正有意义的是使用自己的模型、聚合函数、数据集来做模拟实验。案例的实验似乎仅仅相当于Hello world罢了。

我将上边的四行代码（还算上了空行）用vi填写到服务器上的torch_fedavg_mnist_lr_one_line_example.py文件中。另外创建了一个fedml-config.yml文件，内容如下。其实就是把官方案例的内容复制下来。不过注意到其中默认没使用gpu，如果使用gpu，可以改为true，而gpu_id保持0不用改。

```
common_args:
  training_type: "simulation"
  random_seed: 0

data_args:
  dataset: "mnist"
  data_cache_dir: "../../../data/mnist"
  partition_method: "hetero"
  partition_alpha: 0.5

model_args:
  model: "lr"

train_args:
  federated_optimizer: "FedAvg"
  client_id_list: "[]"
  client_num_in_total: 1000
  client_num_per_round: 10
  comm_round: 200
  epochs: 1
  batch_size: 10
  client_optimizer: sgd
  learning_rate: 0.03
  weight_decay: 0.001

validation_args:
  frequency_of_the_test: 5

device_args:
  using_gpu: false
  gpu_id: 0

comm_args:
  backend: "sp"

tracking_args:
  log_file_dir: ./log
  enable_wandb: false
  wandb_key: ee0b5f53d949c84cee7decbe7a629e63fb2f8408
  wandb_entity: fedml-ai
  wandb_project: simulation
  run_name: fedml_torch_fedavg_mnist_lr
```



然后运行命令，开启这个 Hello world 吧。

```
python torch_fedavg_mnist_lr_one_line_example.py --cf fedml_config.yaml
```

就能看到一些软件、硬件、网络检测信息输出，以及慢慢等待下载mnist数据集的进度条。
