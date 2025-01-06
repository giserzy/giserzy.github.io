---
title: "Topic  Visualization"
excerpt: "LDA"
collection: portfolio
header:
  teaser: "/images/lda.png"
---

<style>
    .map-container {
        width: 100%;
        height: 600px;
        overflow: hidden;
    }
    iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
</style>

<div class="map-container">
    <iframe src="/images/lda.html"></iframe>
</div>

LDA Topic  Visualization
<!-- The calculated model file can be found
[city2vec](/images/TxCity.model) -->
<!-- [链接描述](文件路径/文件名.pdf) -->

<!-- 中文：
这个过程首先使用node2vec将网络中的节点映射为高维向量表示，每个节点都获得一个能够捕捉其网络特征的向量。随后，通过计算节点向量之间的余弦相似度来确定节点关系，并基于设定的相似度阈值和期望连接数量(这里是3)来构建新的网络连接。最终，使用力导向布局或t-SNE降维等方法，将这种高维空间中的关系映射到二维平面上进行可视化展示。

English:
This process begins by using node2vec to map network nodes into high-dimensional vector representations, where each node receives a vector that captures its network characteristics. Subsequently, node relationships are determined by calculating cosine similarities between node vectors, and new network connections are established based on predefined similarity thresholds and desired connection counts(n=3). Finally, these high-dimensional relationships are mapped onto a two-dimensional plane for visualization using either force-directed layouts or dimensionality reduction methods like t-SNE.


```python
from pyvis.network import Network
import networkx as nx
import webbrowser
import os

def create_network_visualization(model, n_connections=3, threshold=0.5):
    # 创建NetworkX图
    G = nx.Graph()
    
    # 获取所有节点
    nodes = list(model.wv.index_to_key)
    
    # 添加节点
    for node in nodes:
        G.add_node(node)
    
    # 添加边
    for node in nodes:
        similar_nodes = model.wv.most_similar(node, topn=n_connections)
        for similar_node, weight in similar_nodes:
            if weight > threshold:
                G.add_edge(node, similar_node, weight=weight)
    
    # 创建Pyvis网络
    nt = Network('750px', '100%', bgcolor="#ffffff", font_color='black')
    
    # 从NetworkX图中获取数据
    nt.from_nx(G)
    
    # 设置物理布局选项
    nt.set_options("""
    const options = {
        "nodes": {
            "font": {
                "size": 14
            },
            "size": 20
        },
        "edges": {
            "color": {
                "inherit": true
            },
            "smooth": {
                "enabled": false
            }
        },
        "physics": {
            "barnesHut": {
                "gravitationalConstant": -2000,
                "centralGravity": 0.3,
                "springLength": 95
            },
            "minVelocity": 0.75
        }
    }""")
    
    # 生成HTML文件
    try:
        nt.save_graph('network.html')
        print("网络图已保存为 'network.html'")
        
        # 自动打开浏览器显示结果
        webbrowser.open('file://' + os.path.abspath('network.html'))
    except Exception as e:
        print(f"保存文件时出错: {e}")
        
        # 尝试另一种保存方式
        try:
            html_string = nt.generate_html()
            with open('network.html', 'w', encoding='utf-8') as f:
                f.write(html_string)
            print("使用替代方法保存成功")
            webbrowser.open('file://' + os.path.abspath('network.html'))
        except Exception as e2:
            print(f"替代保存方法也失败: {e2}")

# 使用示例
create_network_visualization(model, n_connections=3, threshold=0.5)
``` -->