import os
import re

publications = """
2024
1. Ma, H., Zhang, Y., Liu, P., Zhang, F., & Zhu, P. (2024). How does spatial structure affect psychological restoration? A method based on graph neural networks and street view imagery. Landscape and Urban Planning, 251, 105171.
2. Zhang, Y., Kwan, M.P., & Ma, H. (2024). Sensing noise exposure and its inequality based on noise complaint data through vision-language hybrid method. Applied Geography, 171, 103369.
3. He, S., Du, W., Zhang, Y., Chen, L., Chen, Z., & Chen, N. (2024). Next location prediction using heterogeneous graph-based fusion network with physical and social awareness. International Journal of Geographical Information Science, 1-26.
4. Liu, P., Zhang, Y., & Biljecki, F. (2024). Explainable spatially explicit geospatial artificial intelligence in urban analytics. Environment and Planning B: Urban Analytics and City Science, 51(5), 1104-1123.
5. Wang, W., Li, Y., Zhang, Y., & Wu, Z. (2024). Pedestrian evacuation planning under dam-break flood disaster considering road risk and road pedestrian demand. International Journal of Disaster Risk Reduction, 104, 104355.
6. Chen Z., Zou T., Xu Z., & Zhang, Y*. (2024). SAGE-GSAN: A Graph-Based Method for Estimating Urban Taxi CO Emissions Using Street View Images. Journal of Cleaner Production.
7. Zhang, Y., Li Y., & Zhang, F*. (2024). Multi-level urban street representation with street-view imagery and hybrid semantic graph. ISPRS Journal of Photogrammetry and Remote Sensing. (minor) (ESI 3%)
2023
1. Cui, Q., Zhang, Y., Yang, G., Huang, Y., & Chen, Y. (2023). Analysing gender differences in the perceived safety from street view imagery. International Journal of Applied Earth Observation and Geoinformation, 124.
2. Ma, H., Xu, Q., & Zhang, Y*. (2023). High or low? Exploring the restorative effects of visual levels on campus spaces using machine learning and street view imagery. Urban Forestry & Urban Greening, 88, 128087.
3. Zhai, W., Zhang, K., Gou, F., Cheng, H., Li, Z., & Zhang, Y. (2023). Examining supply-demand imbalances and social inequalities of regulating ecosystem services in high-density cities: A case study of Wuhan, China. Ecological Indicators, 154, 110654.
4. Zhang, Y., Zhang, F., Fang, L., & Chen, N. (2023). Inferring socioeconomic environment from built environment characteristics based street view images: An approach of Seq2Seq method. International Journal of Applied Earth Observation and Geoinformation, 123.
5. Zheng, X., Li, M., Wan, Z., & Zhang, Y. (2023). Knowledge mining and graph visualization of ancient Chinese scientific and technological documents bibliographic summaries based on digital humanities. Library Hi Tech.
6. Wang, P., Zhang, Y., Hu, T., & Zhang, T. (2023). Urban traffic flow prediction: A dynamic temporal graph network considering missing values. International Journal of Geographical Information Science, 37(4), 885-912.
7. Zhang, Y., Liu, P., & Biljecki, F. (2023). Knowledge and topology: A two layer spatially dependent graph neural networks to identify urban functions with time-series street view image. ISPRS Journal of Photogrammetry and Remote Sensing, 198, 153-168. (ESI 3%)
8. Wang, S., Zhang, X., Chen, N., Tian, L., Zhang, Y., & Nam, W.H. (2023). A systematic review and quantitative meta-analysis of the relationships between driving forces and cyanobacterial blooms at global scale. Environmental Research, 216, 114670.
9. Zhang, Y., Chen, N., Wang, S., Wen, M., & Chen, Z. (2023). Will carbon trading reduce spatial inequality? A spatial analysis of 200 cities in China. Journal of Environmental Management, 325, 116402.
2022
1. Li, Y., Zhang, Y*., & Chen, M. (2022). Highway Vehicle Route Reconstruction Using Sparse and Noisy Communication Base Station Fingerprints. IEEE Sensors Journal, 22(22), 22040-22052.
2. Liu, J., Chen, N., Chen, Z., Xu, L., Du, W., Zhang, Y., & Wang, C. (2022). Towards sustainable smart cities: Maturity assessment and development pattern recognition in China. Journal of Cleaner Production, 370, 133248.
3. Zhang, Y., Zheng, X., Helbich, M., Chen, N., & Chen, Z. (2022). City2vec: Urban knowledge discovery based on population mobile network. Sustainable Cities and Society, 85, 104000.
4. Zhang, Y., Zhang, F., & Chen, N. (2022). Migratable urban street scene sensing method based on vision language pre-trained model. International Journal of Applied Earth Observation and Geoinformation, 113.
5. Wang, C., Ma, L., Zhang, Y., Chen, N., & Wang, W. (2022). Spatiotemporal dynamics of wetlands and their driving factors based on PLS-SEM: A case study in Wuhan. Science of the Total Environment, 806, 151310.
2021
1. Zhang, Y., Chen, Z., Zheng, X., Chen, N., & Wang, Y. (2021). Extracting the location of flooding events in urban systems and analyzing the semantic risk using social sensing data. Journal of Hydrology, 603, 127053.
2. Zhang, Y., Chen, N., Du, W., Li, Y., & Zheng, X. (2021). Multi-source sensor based urban habitat and resident health sensing: A case study of Wuhan, China. Building and Environment, 198, 107883.
3. Chen, N., Zhang, Y.*, Du, W.*, Li, Y., Chen, M., & Zheng, X. (2021). KE-CNN: A new social sensing method for extracting geographical attributes from text semantic features and its application in Wuhan, China. Computers, Environment and Urban Systems, 88, 101629.
4. Zhang, Y., Zheng, X., Chen, M., Li, Y., Yan, Y., & Wang, P. (2021). Urban fine-grained spatial structure detection based on a new traffic flow interaction analysis framework. ISPRS International Journal of Geo-Information, 10(4), 227.
2020
1. Zhang, Y., Chen, N., Du, W., Yao, S., & Zheng, X. (2020). A new geo-propagation model of event evolution chain based on public opinion and epidemic coupling. International Journal of Environmental Research and Public Health, 17(24), 9235.
2. Zhang, Y., Li, Y., Yang, B., Zheng, X., & Chen, M. (2020). Risk assessment of COVID-19 based on multisource data from a geographical viewpoint. IEEE Access, 8, 125702-125713.
"""

def create_md_file(paper, index, year):
    # Extract information
    parts = paper.split('. ', 1)
    if len(parts) < 2:
        print(f"Skipping invalid paper entry: {paper}")
        return
    _, rest = parts
    
    # Use regular expressions to extract information
    match = re.match(r'(.*?)\((\d{4})\)\.\s*(.*?)\.\s*(.*)', rest)
    if not match:
        print(f"Skipping paper with invalid format: {paper}")
        return
    
    authors, year, title, venue = match.groups()
    
    # Remove any trailing periods from the venue
    venue = venue.rstrip('.')
    
    # Create filename
    filename = f"{year}-paper-{index}.md"
    
    # Create content
    content = f"""---
title: "{title.strip()}"
collection: publications
category: manuscripts
permalink: /publication/{year}-paper-{index}
excerpt: 'This paper is about {title.strip()}.'
date: {year}-01-01
venue: '{venue.strip()}'
paperurl: 'http://academicpages.github.io/files/paper{index}.pdf'
citation: '{authors.strip()} ({year}). &quot;{title.strip()}&quot; <i>{venue.strip()}</i>'
---

{authors.strip()} ({year}). {title.strip()}. <i>{venue.strip()}</i>

"""
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Split the publications into years and papers
years = publications.strip().split('\n')

current_year = None
paper_index = 1

for line in years:
    line = line.strip()
    if line.isdigit():  # This is a year line
        current_year = line
        paper_index = 1
    elif line and current_year:  # This is a paper entry
        create_md_file(line, paper_index, current_year)
        paper_index += 1

print(f"Generated markdown files in the current directory.")