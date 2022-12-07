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


