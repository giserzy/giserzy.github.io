---
title: "Multi-level urban street representation with street-view imagery and hybrid semantic graph"
excerpt: "<img src='/images/abstract.png'>"
collection: portfolio
---

<html>
<head>
    <style>
        .container {
            width: 100%;
            max-width: 900px;
            margin: 20px auto;
            font-family: Arial, sans-serif;
        }
        .legend {
            display: flex;
            gap: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .legend-icon {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }
        .city-map {
            width: 100%;
            height: 600px;
            background: #f5f5f5;
            position: relative;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 12px;
            overflow: hidden;
        }
        .area {
            position: absolute;
            border-radius: 12px;
            opacity: 0.3;
            transition: opacity 0.3s;
        }
        .area:hover {
            opacity: 0.5;
        }
        .area-label {
            position: absolute;
            background: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 13px;
            white-space: nowrap;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            z-index: 3;
        }
        .street {
            position: absolute;
            background: #fff;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }
        .street-horizontal {
            height: 12px;
        }
        .street-vertical {
            width: 12px;
        }
        .building {
            position: absolute;
            background: rgba(149, 165, 166, 0.8);
            border-radius: 4px;
            z-index: 1;
            box-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .green-space {
            position: absolute;
            background: rgba(46, 204, 113, 0.3);
            border-radius: 50%;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="legend">
        <div class="legend-item">
            <div class="legend-icon" style="background: #e74c3c;"></div>
            <span>商业区</span>
        </div>
        <div class="legend-item">
            <div class="legend-icon" style="background: #3498db;"></div>
            <span>住宅区</span>
        </div>
        <div class="legend-item">
            <div class="legend-icon" style="background: #9b59b6;"></div>
            <span>办公区</span>
        </div>
        <div class="legend-item">
            <div class="legend-icon" style="background: #f1c40f;"></div>
            <span>教育区</span>
        </div>
        <div class="legend-item">
            <div class="legend-icon" style="background: #1abc9c;"></div>
            <span>公园绿地</span>
        </div>
    </div>

    <div class="city-map">
        <!-- 主要功能区 -->
        <!-- 商业中心区（CBD）-->
        <div class="area" style="background: #e74c3c; left: 35%; top: 30%; width: 30%; height: 25%;"></div>
        <div class="area-label" style="left: 42%; top: 40%;">商业中心区</div>

        <!-- 相邻的两个住宅区（展示空间依赖）-->
        <div class="area" style="background: #3498db; left: 5%; top: 15%; width: 20%; height: 30%;"></div>
        <div class="area-label" style="left: 8%; top: 25%;">住宅区A</div>

        <div class="area" style="background: #3498db; left: 5%; top: 50%; width: 20%; height: 30%;"></div>
        <div class="area-label" style="left: 8%; top: 60%;">住宅区B</div>

        <!-- 远距离办公区（展示空间交互）-->
        <div class="area" style="background: #9b59b6; right: 5%; top: 10%; width: 25%; height: 35%;"></div>
        <div class="area-label" style="right: 12%; top: 25%;">办公区</div>

        <!-- 教育区 -->
        <div class="area" style="background: #f1c40f; right: 10%; bottom: 15%; width: 20%; height: 25%;"></div>
        <div class="area-label" style="right: 15%; bottom: 25%;">教育区</div>

        <!-- 公园绿地 -->
        <div class="area" style="background: #1abc9c; left: 40%; bottom: 10%; width: 25%; height: 20%;"></div>
        <div class="area-label" style="left: 48%; bottom: 18%;">公园绿地</div>

        <!-- 街道网络 -->
        <!-- 主要道路 -->
        <div class="street street-horizontal" style="left: 0; top: 25%; width: 100%;"></div>
        <div class="street street-horizontal" style="left: 0; top: 45%; width: 100%;"></div>
        <div class="street street-horizontal" style="left: 0; top: 65%; width: 100%;"></div>
        <div class="street street-vertical" style="left: 30%; top: 0; height: 100%;"></div>
        <div class="street street-vertical" style="left: 60%; top: 0; height: 100%;"></div>

        <!-- 建筑物 -->
        <div class="building" style="left: 38%; top: 35%; width: 15px; height: 25px;"></div>
        <div class="building" style="left: 45%; top: 38%; width: 20px; height: 30px;"></div>
        <div class="building" style="left: 52%; top: 36%; width: 18px; height: 28px;"></div>
        <div class="building" style="right: 12%; top: 15%; width: 15px; height: 25px;"></div>
        <div class="building" style="right: 18%; top: 20%; width: 20px; height: 30px;"></div>
        <div class="building" style="left: 8%; top: 20%; width: 15px; height: 20px;"></div>
        <div class="building" style="left: 15%; top: 55%; width: 15px; height: 20px;"></div>

        <!-- 绿地 -->
        <div class="green-space" style="left: 42%; bottom: 15%; width: 40px; height: 40px;"></div>
        <div class="green-space" style="left: 50%; bottom: 20%; width: 30px; height: 30px;"></div>
        <div class="green-space" style="left: 55%; bottom: 18%; width: 35px; height: 35px;"></div>
    </div>

    <div style="margin-top: 20px;">
        <div style="display: flex; gap: 20px;">
            <div style="flex: 1; padding: 15px; background: #f8f9fa; border-radius: 8px;">
                <strong>空间依赖示例</strong>
                <p style="margin: 5px 0;">住宅区A和B紧邻，共享相似的环境特征和功能属性</p>
            </div>
            <div style="flex: 1; padding: 15px; background: #f8f9fa; border-radius: 8px;">
                <strong>空间交互示例</strong>
                <p style="margin: 5px 0;">办公区与商业区、住宅区距离较远但功能互补、人流密集</p>
            </div>
        </div>
    </div>
</div>
</body>
</html>

Model Structure
![Model Structure](/images/model.png)

<html>
<head>
    <style>
        .container {
            width: 100%;
            max-width: 800px;
            margin: 20px auto;
            font-family: Arial, sans-serif;
        }
        .legend {
            display: flex;
            gap: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .legend-icon {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }
        .comparison {
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-top: 20px;
        }
        .section {
            border: 1px solid #ccc;
            padding: 15px;
            border-radius: 8px;
        }
        .title {
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .street-view {
            width: 100%;
            height: 120px;
            background: #f5f5f5;
            position: relative;
            margin: 10px 0;
            border: 1px solid #ddd;
        }
        .tree {
            width: 20px;
            height: 30px;
            background: #2ecc71;
            position: absolute;
            bottom: 0;
        }
        .building {
            width: 40px;
            height: 80px;
            background: #95a5a6;
            position: absolute;
            bottom: 0;
        }
        .arrow {
            text-align: center;
            font-size: 24px;
            color: #7f8c8d;
        }
        .metric {
            background: #e8f6f3;
            padding: 10px;
            margin-top: 5px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="legend">
        <div class="legend-item">
            <div class="legend-icon" style="background: #2ecc71;"></div>
            <span>树木</span>
        </div>
        <div class="legend-item">
            <div class="legend-icon" style="background: #95a5a6;"></div>
            <span>建筑</span>
        </div>
        <div class="legend-item">
            <div class="legend-icon" style="background: #f5f5f5; border: 1px solid #ddd;"></div>
            <span>街道空间</span>
        </div>
    </div>
    
    <div class="comparison">
        <div class="section">
            <div class="title">传统研究方法：仅关注单个要素的比例</div>
            <div class="street-view">
                <div class="tree" style="left: 10%"></div>
                <div class="tree" style="left: 30%"></div>
                <div class="tree" style="left: 50%"></div>
                <div class="tree" style="left: 70%"></div>
                <div class="building" style="left: 20%"></div>
                <div class="building" style="left: 60%"></div>
            </div>
            <div class="metric">
                树木覆盖率: 30% | 建筑覆盖率: 40%
            </div>
        </div>
        
        <div class="arrow">↓</div>
        
        <div class="section">
            <div class="title">研究差距：需要考虑空间关系</div>
            <div style="display: flex; justify-content: space-between;">
                <div style="width: 48%;">
                    <div class="street-view">
                        <div class="tree" style="left: 10%"></div>
                        <div class="tree" style="left: 25%"></div>
                        <div class="tree" style="left: 40%"></div>
                        <div class="tree" style="left: 55%"></div>
                        <div class="building" style="left: 70%"></div>
                        <div class="building" style="left: 85%"></div>
                    </div>
                    <div class="metric">均匀分布的树木</div>
                </div>
                <div style="width: 48%;">
                    <div class="street-view">
                        <div class="tree" style="left: 10%"></div>
                        <div class="tree" style="left: 15%"></div>
                        <div class="tree" style="left: 20%"></div>
                        <div class="tree" style="left: 25%"></div>
                        <div class="building" style="left: 50%"></div>
                        <div class="building" style="left: 70%"></div>
                    </div>
                    <div class="metric">聚集分布的树木</div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>