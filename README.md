# Funny JSON Explorer（FJE）

一个JSON文件可视化的命令行界面小工具

运行：fje -f <json file> -s <style> -i <icon family>

```
{
    oranges: {
        'mandarin': {                            ├─ oranges
            clementine: null,                    │  └─ mandarin
            tangerine: 'cheap & juicy!'  -=>     │     ├─ clementine
        }                                        │     └─ tangerine: cheap & juicy!
    },                                           └─ apples
    apples: {                                       ├─ gala
        'gala': null,                               └─ pink lady
        'pink lady': null
    }
}
```

FJE可以快速切换风格（style），包括：树形（tree）、矩形（rectangle）；

```
├─ oranges                             ┌─ oranges ───────────────────────────────┐
│  └─ mandarin                         │  ├─ mandarin ───────────────────────────┤
│     ├─ clementine                    │  │  ├─ clementine ──────────────────────┤
│     └─ tangerine: cheap & juicy!     │  │  ├─ tangerine: cheap & juicy! ───────┤
└─ apples                              ├─ apples ────────────────────────────────┤
   └─ gala                             └──┴─✩gala ───────────────────────────────┘

        树形（tree）                                   矩形（rectangle）
```

也可以指定图标族（icon family），为中间节点或叶节点指定一套icon

```
├─♢oranges                             
│  └─♢mandarin                         
│     ├─♤clementine                    
│     └─♤tangerine: cheap & juicy!  
└─♢apples                              
   └─♤gala                             

poker-face-icon-family: 中间节点icon：♢ 叶节点icon：♤  
```

# 使用方法

使用环境：Python3

在项目根目录运行：`src/main -f <json file> -s <style> -i <icon family>`

比如：`src/main -f datasets/test.json -s rectangle -i color`

效果截图：

<center class="half">    <img src="https://cdn.jsdelivr.net/gh/Xxxxic/ImageStorage@main/img/202406130001911.png" width="430"/><img src="https://cdn.jsdelivr.net/gh/Xxxxic/ImageStorage@main/img/202406130001411.png" width="410"/></center>

<center class="half">    <img src="https://cdn.jsdelivr.net/gh/Xxxxic/ImageStorage@main/img/202406130001238.png" width="420"/><img src="https://cdn.jsdelivr.net/gh/Xxxxic/ImageStorage@main/img/202406130001199.png" width="420"/></center>

#### 扩展

1. **新的风格**：在`src/factory`中加入新抽象工厂类。
2. **新图标簇**：修改配置文件`src/config/icon.json`即可自定义图标簇。

#### 类图

<img src="https://cdn.jsdelivr.net/gh/Xxxxic/ImageStorage@main/img/202406130004958.png" width="800"/>

#### 设计模式及作用

##### 抽象工厂

抽象工厂模式用于生产不同产品族的所有产品。一个项目中可能包含多个产品族，每个具体工厂负责创建同一族但不同等级结构的产品。

在本项目中，抽象类 AbstractFactory 作为抽象工厂，提供了两种产品族的接口，给到不同的具体工厂去实现，这里是工厂 IconFactory 和 StyleFactory 实现。

##### 工厂方法

工厂方法模式定义了一个创建产品对象的接口，将实际的产品创建工作推迟到具体的子工厂类中。

如本项目中的 StyleFactory 是抽象工厂，由具体子工厂 TreeStyleFactory 和 RectangleStyleFactory 实现，用于生产两种不同风格的 Style 产品。

##### 简单工厂

简单工厂模式，也被称为静态工厂方法，封装了对象的实例化逻辑，适用于产品种类较少且变动不大的场景。

在本项目中，IconFactory 就是一个简单工厂，用于生产少量且变化不大的 Icon 产品。

##### 建造者模式

建造者模式用于将一个复杂对象的构建过程拆分为多个简单的步骤，逐步完成对象的构建。具体而言，建造者模式将复杂对象的构造与其属性赋值过程分离，允许灵活选择每个部分的具体实现。

在本项目中，JsonExplorer 扮演了建造者的角色，通过设置内部的具体工厂并调用它们的接口来生产不同的产品。

##### 组合模式

组合模式使用户能够对单个对象和组合对象进行一致的访问。它通过将对象组合成树状的层次结构来表示“部分-整体”的关系。

在本项目中，Node、Container 和 Leaf 使用了组合模式。Node 定义了组合对象的所有接口，Container 是中间节点，Leaf 是叶子节点。

