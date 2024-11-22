---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Cartography and Geographic Information Systems, Wuhan University, 2023
* Joint Ph.D. , The National Univeristy Of Singapore, 2022
* M.S. in Geomatics Engineering, Wuhan University, 2020
* B.S. in Geomatics Engineering, Wuhan University, 2018

Academic experience
======
* Dec 2023 - Present: Postdoctoral Fellow
  * Chinese University of Hong Kong
  * Institute of Space and Earth Information Science

* Sep 2023 - Nov 2023: Visiting Student
  * Peking University
  * Advisor: Professor Yu Liu

* Jan 2022 - Jan 2023: Joint Student
  * National University of Singapore
  * School of Design and Environment
  * Advisor: Filip Biljecki

Skills
======
* GeoAI and social sensing
* Urban science
* Disaster response
* Social inequality analysis
* Spatial-temporal big data analysis

Reviewer
======
*  Environment International,SCI Q1

*  Applied Geography,SCI Q1

*  Geoscience Letters,SCI Q1

*  International Journal of Applied Earth Observation and Geoinformation,SCI Q1

*  Journal of Environment Development,SCI Q1

*  Science of the Total Environment,SCI Q1

*  Language Resources and Evaluation,SCI Q1

*  Journal of Asian architecture and building engineering,SCI Q1

*  Journal of environmental management,SCI Q1

*  Transactions in Urban Data, Science and Technology

*  International Journal of Crowd Science

*  Computational urban science

*  Transactions in GIS,SSCI Q2

*  Sustainability,SSCI Q2

*  Journal of Cleaner Production,SSCI Q1

*  Plos One,SCI Q1

*  IEEE Access,SCI Q2

*  Environment and Planning B: Urban Analytics and City Science,SCI Q1

*  Landscape and Urban Planning, SCI Q1

*  Climatic Change,SCI Q1

*  Remote Sensing,SCI Q1

*  Energies,SCI Q3

*  Transportation Research Part D: Transport and Environment,SCI Q1

*  Journal of Hydrology,SCI Q1

*  ISPRS International Journal of Geo-Information,SCI Q1

*  Heritage,ESCI Q2

*  Environmental Science and Pollution Research,SCI Q1

*  Urban Science, ESCI

\*  **Membership**, Association for Computing Machinery

\* **Membership**,International Society for Photogrammetry and Remote Sensing

\* **Guest Chair Editor**, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (Special Issue Name: Street View Imagery and GeoAI, IF: 5.5),SCI Q1

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Awards and Honors
======
* National Scholarship for Ph.D. Students, Ministry of Education (Top 3%), 2021 & 2022
* China Scholarship Council Scholarship for Studying Abroad, 2021
* Top 10 Inspirational Graduate Students, Wuhan University, 2023
* First-class Academic Scholarship and Outstanding Graduate, Wuhan University, 2021 & 2022
* Third Prize in the City Data Development Competition (First Place Individual Ranking, Top 5%), Wuhan Municipal Government, 2022
* Second Prize for Academic Innovation, Wuhan University, 2023
* Excellent Original WeChat Account in the Geoinformation Field, Surveying and Mapping Press, 2024

Project Involvement
======
* National Key R&D Program of China: "National Public Security Emergency Platform" (2018YFC0807000)
* National Key R&D Program of China: "Urban Multi-scale Integrated Perception Service System and Demonstration" (2018YFB2100504)
* Ministry of Education, Singapore: "Multi-scale Digital Twins for the Urban Environment"
* Hong Kong Productivity Council and Transport Department: "Vehicle Detection and Vehicle-kilometrage Estimation Based on Remote Sensing Technologies"

Principal Investigator
======
* China-U.S. Scholars Program (CUSP) Grant, Harvard and Yenching Institute, $3,285 USD, April 2024

Joint Supervision of Master's Thesis
======
* Wuhan University: "Extraction of Road Disease Characteristics and Analysis of Spatial Influencing Factors in Wuhan City" (Congpu Hao), 2023
* China University of Geosciences: "Research on Location Description Extraction and Scene Risk Identification for Typical Urban Crime Incidents" (Zheng Xu), 2024
* China University of Geosciences: "Estimation Method for Urban Road Taxi Carbon Emissions Map Based on Street View and Road Network Structure Using Graph Neural Networks" (Tongxu Zou), 2024

Academic Engagements
======
* Reviewer for multiple SCI and SSCI journals including Environment International, Applied Geography, Science of the Total Environment, etc.
* Guest Chair Editor, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (Special Issue: Street View Imagery and GeoAI)
* Member, Association for Computing Machinery
* Member, International Society for Photogrammetry and Remote Sensing

Invited Talks
======
1. Academic presentation at the 2019 China Public Security Congress, Beijing, 2019
2. Academic presentation at The 2nd International Conference on Urban Informatics, Hong Kong, 2023
3. Guest speaker at various academic salons and events at Wuhan University and China University of Geosciences
4. Personal academic WeChat Official Account "Sensingcity" with over 12,000 followers

Conference Participation
======
* Global Conference on Climate Change Polar Studies, Environment and Climate Change
* Global Smart Cities Summit cum The 3rd International Conference on Urban Informatics (ICUI 2023)

Diagram
======
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Analysis of Urban Function Distribution</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f0f2f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #1a237e;
            text-align: center;
            margin-bottom: 30px;
        }
        #chart {
            width: 100%;
            height: 400px;
            margin-bottom: 30px;
        }
        .legend {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .color-box {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }
        @media (max-width: 600px) {
            .container {
                padding: 10px;
            }
            #chart {
                height: 300px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Analysis of Urban Function Distribution</h1>
        <div id="chart"></div>
        <div class="legend">
            <div class="legend-item">
                <div class="color-box" style="background: #FF6B6B"></div>
                <span>Residential</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background: #4ECDC4"></div>
                <span>Commercial</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background: #45B7D1"></div>
                <span>Industrial</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background: #96CEB4"></div>
                <span>Green Space</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background: #D4A5A5"></div>
                <span>Mixed Use</span>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <script>
        const chart = echarts.init(document.getElementById('chart'));
        
        const option = {
            tooltip: {
                trigger: 'item',
                formatter: '{b}: {c} km² ({d}%)'
            },
            series: [{
                name: 'Urban Functions',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: true,
                    formatter: '{b}\n{d}%'
                },
                labelLine: {
                    show: true
                },
                data: [
                    { value: 35, name: 'Residential', itemStyle: { color: '#FF6B6B' } },
                    { value: 25, name: 'Commercial', itemStyle: { color: '#4ECDC4' } },
                    { value: 20, name: 'Industrial', itemStyle: { color: '#45B7D1' } },
                    { value: 15, name: 'Green Space', itemStyle: { color: '#96CEB4' } },
                    { value: 5, name: 'Mixed Use', itemStyle: { color: '#D4A5A5' } }
                ]
            }]
        };

        chart.setOption(option);

        window.addEventListener('resize', function() {
            chart.resize();
        });
    </script>
</body>
</html>