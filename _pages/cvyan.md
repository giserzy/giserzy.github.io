% !TEX TS-program = xelatex
% !TEX encoding = UTF-8 Unicode
% !Mode:: "TeX:UTF-8"
\documentclass{resume}
\usepackage{color} 
\usepackage{xcolor}
\usepackage{fontawesome}
\usepackage{zh_CN-Adobefonts_external}
\usepackage{graphicx} % 添加图片支持
\usepackage{linespacing_fix}
\usepackage{cite}

\newcounter{publicationCounter} % 创建一个新的计数器

\newcommand{\myDatedSubsection}[2]{
    \stepcounter{publicationCounter} % 增加计数器
    \subsection*{\textbf{\thepublicationCounter. #1} #2}
    % 这里你可以添加其他格式化和内容
}

\begin{document}
\pagenumbering{gobble}

% 添加个人头像
\begin{minipage}[l]{0.15\textwidth}
  \includegraphics[width=\linewidth]{resume/zy.jpg}
\end{minipage}
\begin{minipage}[l]{0.8\textwidth}
  \name{Yan Zhang}
  \basicInfo{
\email{sggzhang@whu.edu.cn} \textperiodcentered\ 
\faBirthdayCake{Birthday:1997} \textperiodcentered\
\faGraduationCap{Citations:865(h-index:16)}
}

\end{minipage}

 % {https://www.giserzhang.xyz/}
\section{\faGraduationCap\ Education}

\datedsubsection{\textbf{Wuhan University}, Wuhan, China}{Sep 2014 -- Jun 2018}
\textit{Bachelor of Science} in Geomatics Engineering
% Advisor: Associate Professor Hai-Lan Huang

\datedsubsection{\textbf{Wuhan University}, Wuhan, China}{Sep 2018 -- Jun 2020}
\textit{Master of Science} in Geomatics Engineering
% Advisors: Associate Professor Ying-Bing Li, Professor Hai-Yan Sun

\datedsubsection{\textbf{Wuhan University}, Wuhan, China}{Sep 2020 -- Jun 2023}
\textit{Phd} in Cartography and Geographic Information Systems
Advisor: Professor Neng-Cheng Chen

\datedsubsection{\textbf{Peking University}, Beijing,China}{July 2023 -- Dec 2023}
\textit{Visiting Scholars} in Cartography and Geographic Information Systems
Advisor: Professor Yu Liu

\datedsubsection{\textbf{National University of Singapore}, Singapore,Singapore}{Jan 2022 -- Jan 2023}
\textit{Joint Phd Student} in School of Design and Environment
Advisor: Filip Biljecki




\section{\faLaptop\ Career}
\datedsubsection{\textbf{Chinese University of Hong Kong}, Hong Kong, China}{Dec 2023 -- Now}
\textit{Postdoctoral Fellow} in the Institute of Space and Earth Information Science
Advisor: Mei-Po Kwan

\datedsubsection{\textbf{Chinese University of Hong Kong}, Shen Zhen, China}{Feb 2025 -- Now}
\textit{Assistant Researcher} in the Shenzhen Research Institute (Part Time)

\section{\faUsers\ Publications}

\subsection*{\textbf{2025}}

\begin{enumerate}
% \item Ma, H., \textbf{Zhang, Y}., Liu, P., Zhang, F., \& Zhu, P. (2024). How does spatial structure affect psychological restoration? A method based on graph neural networks and street view imagery. \textit{Landscape and Urban Planning}, 251, 105171. IF=8.0, SCI \textbf{Q1}

\item \textbf{Zhang Y}, Kwan, MP. \& Fang, L. (2025). 
An LLM driven dataset on the spatiotemporal distributions of street and neighborhood crime in China. \textit{Scientific Data}. IF=6.9, SCI \textbf{Q1}
{\color{red}{\textbf{indexed by National Earth Observation Data Center and 5000 download}}}

\item \textbf{Zhang Y}, Kwan, MP. (2025). Considering Human Mobility is Essential for Accurate Environmental Exposure Assessment.  {\color{red}{\textbf{Science Bulletin}}, IF=21.1}, SCI \textbf{Q1}.

\item Zeqiang Chen, Xinghao Li, Xiang Zhang, Lei Xu, Wenying Du, Lei Wu, Dinan Wang, \textbf{Yan Zhang}, \& Nengcheng Chen. (2025). Global drought-flood abrupt alternation: spatiotemporal patterns, drivers, and projections. 
{\color{red}{\textbf{The Innovation Geoscience}}}.

\item \textbf{Zhang Y}, Kwan, MP, et al (2025). CrossGraphNet: A Cross-Spatiotemporal Graph-based Method for Traffic Speed Reconstruction Using Remote Sensing Vehicle Detection \textbf{International Journal of Digital Earth}. IF=4.7, SCI \textbf{Q1}.

\item Liu B, Li Y, \textbf{Zhang Y}, et al. (2025). Multi-criteria decision-making method for emergency shelter site selection considering flood risk: A case study of Zhuhai, China.
\textit{Cleaner Engineering and Technology}.

\item Qin Q, Ai T, Xu S, \textbf{Zhang Y}, et al. Learning dual context aware POI representations for geographic mapping[J]. International Journal of Applied Earth Observation and Geoinformation, 2025, 142: 104683.

\item Cui Q, \textbf{Zhang Y}, Ma H, et al. (2025). How about electric vehicle? Sensing owners’ experiences and attitudes through online short video. \textit{Transport Policy}.

\item D Wang, Y Wang, M Dou, M Qiao, X Fu, \textbf{Y Zhang}. (2025). Exploring the nonlinear impact of visual environment on residents’ happiness: a computational framework integrating semantic and geometric features. \textbf{Geo-spatial Information Science}.

\end{enumerate}

\subsection*{\textbf{2024}}

\begin{enumerate}

\item \textbf{Zhang, Y}., Kwan, M.P., \& Ma, H. (2024). Sensing noise exposure and its inequality based on noise complaint data through vision-language hybrid method. \textit{Applied Geography}, 171, 103369. IF=4.0, SSCI \textbf{Q1}

\item \textbf{Zhang Y}., Meipo, Kwan*, Boting Yu,etc. (2024). Probabilistic Quantitative Identification of Urban Functional Zones: Fusing Physical Sensing and Social Sensing Data, \textit{Transactions in GIS}
{IF=2.1, SSCI \textbf{Q2}} 

\item \textbf{Zhang, Y}., Li Y., \& Zhang, F*. (2024). Multi-level urban street representation with street-view imagery and hybrid semantic graph. \textit{ISPRS Journal of Photogrammetry and Remote Sensing}. IF=10.6, {\color{red}{\textbf{ESI 3\%}}}

\item Ma, H., \textbf{Zhang, Y}., Liu, P., Zhang, F., \& Zhu, P. (2024). How does spatial structure affect psychological restoration? A method based on graph neural networks and street view imagery. \textit{Landscape and Urban Planning}, 251, 105171. IF=8.0, SCI \textbf{Q1} {\color{red}{\textbf{ESI Highly Cited Paper \& Hot Paper }}}

\item He, S., Du, W., \textbf{Zhang, Y}., Chen, L., Chen, Z., \& Chen, N. (2024). Next location prediction using heterogeneous graph-based fusion network with physical and social awareness. \textit{International Journal of Geographical Information Science}, 1-26. IF=4.4, SSCI \textbf{Q1}

\item Liu, P., \textbf{Zhang, Y}., \& Biljecki, F. (2024). Explainable spatially explicit geospatial artificial intelligence in urban analytics. \textit{Environment and Planning B: Urban Analytics and City Science}, 51(5), 1104-1123. IF=4.8, SSCI \textbf{Q1}

\item Wang, W., Li, Y., \textbf{Zhang, Y}., \& Wu, Z. (2024). Pedestrian evacuation planning under dam-break flood disaster considering road risk and road pedestrian demand. \textit{International Journal of Disaster Risk Reduction}, 104, 104355. IF=4.7, SCI \textbf{Q1}

\item Chen Z., Zou T., Xu Z., \& \textbf{Zhang, Y*}. (2024). SAGE-GSAN: A Graph-Based Method for Estimating Urban Taxi CO Emissions Using Street View Images. \textit{Journal of Cleaner Production}. IF=9.7, SCI \textbf{Q1}

\item Song L, Liu D, Kwan M P, Y Liu, \textbf{Yan Zhang}. (2024). Machine-based understanding of noise perception in urban environments using mobility-based sensing data[J]. \textit{Computers, Environment and Urban Systems}, 88, 101629. IF=6.8, SSCI \textbf{Q1}

\end{enumerate}

\subsection*{\textbf{2023}}

\begin{enumerate}
\item \textbf{Zhang, Y}., Liu, P., \& Biljecki, F. (2023). Knowledge and topology: A two layer spatially dependent graph neural networks to identify urban functions with time-series street view image. \textit{ISPRS Journal of Photogrammetry and Remote Sensing}, 198, 153-168. IF=10.6, SCI \textbf{Q1}, {\color{red}{\textbf{ESI 3\%, ESI Highly Cited Papers \faTrophy}}}, {\color{red}{1\%}}

\item \textbf{Zhang, Y}., Zhang, F., Fang, L., \& Chen, N. (2023). Inferring socioeconomic environment from built environment characteristics based street view images: An approach of Seq2Seq method. \textit{International Journal of Applied Earth Observation and Geoinformation}, 123. IF=7.5, SCI \textbf{Q1}

\item \textbf{Zhang, Yan}., Chen, N., Wang, S., Wen, M., \& Chen, Z. (2023). Will carbon trading reduce spatial inequality? A spatial analysis of 200 cities in China. \textit{Journal of Environmental Management}, 325, 116402. IF=8.7, SCI \textbf{Q1} {\color{red}{\textbf{reported by China Daily News}}}


\item Cui, Q., \textbf{Zhang, Y}., Yang, G., Huang, Y., \& Chen, Y. (2023). Analysing gender differences in the perceived safety from street view imagery. \textit{International Journal of Applied Earth Observation and Geoinformation}, 124. IF=7.5, SCI \textbf{Q1}

\item Ma, H., Xu, Q., \& \textbf{Zhang, Y*}. (2023). High or low? Exploring the restorative effects of visual levels on campus spaces using machine learning and street view imagery. \textit{Urban Forestry \& Urban Greening}, 88, 128087. IF=6.4, SCI \textbf{Q1}

\item Zhai, W., Zhang, K., Gou, F., Cheng, H., Li, Z., \& \textbf{Zhang, Y}. (2023). Examining supply-demand imbalances and social inequalities of regulating ecosystem services in high-density cities: A case study of Wuhan, China. \textit{Ecological Indicators}, 154, 110654. IF=6.3, SCI \textbf{Q1}

\item Zheng, X., Li, M., Wan, Z., \& Zhang, Y. (2023). Knowledge mining and graph visualization of ancient Chinese scientific and technological documents bibliographic summaries based on digital humanities. \textit{Library Hi Tech}. IF=2.9, SSCI \textbf{Q2}

\item Wang, P., \textbf{Zhang, Y}., Hu, T., \& Zhang, T. (2023). Urban traffic flow prediction: A dynamic temporal graph network considering missing values. \textit{International Journal of Geographical Information Science}, 37(4), 885-912. IF=4.4, SSCI \textbf{Q1}

\item Wang, S., Zhang, X., Chen, N., Tian, L., \textbf{Zhang, Y}., \& Nam, W.H. (2023). A systematic review and quantitative meta-analysis of the relationships between driving forces and cyanobacterial blooms at global scale. \textit{Environmental Research}, 216, 114670. IF=8.6, SCI \textbf{Q1}


\end{enumerate}

\subsection*{\textbf{2022}}

\begin{enumerate}
\item \textbf{Zhang, Y}., Zheng, X., Helbich, M., Chen, N., \& Chen, Z. (2022). City2vec: Urban knowledge discovery based on population mobile network. \textit{Sustainable Cities and Society}, 85, 104000. IF=11.7, SCI \textbf{Q1} (reported by World Urban Planning Education Network; Urban Planning Forum Planning Reviews Highlight)

\item \textbf{Zhang, Y}., Zhang, F., \& Chen, N. (2022). Migratable urban street scene sensing method based on vision language pre-trained model. \textit{International Journal of Applied Earth Observation and Geoinformation}, 113. IF=7.5, SCI \textbf{Q1}


\item Li, Y., \textbf{Zhang, Y*}., \& Chen, M. (2022). Highway Vehicle Route Reconstruction Using Sparse and Noisy Communication Base Station Fingerprints. \textit{IEEE Sensors Journal}, 22(22), 22040-22052. IF=4.3, SCI \textbf{Q1}

\item Liu, J., Chen, N., Chen, Z., Xu, L., Du, W., \textbf{Zhang, Y}., \& Wang, C. (2022). Towards sustainable smart cities: Maturity assessment and development pattern recognition in China. \textit{Journal of Cleaner Production}, 370, 133248. IF=9.7, SCI \textbf{Q1}

\item Wang, C., Ma, L., \textbf{Zhang, Y}., Chen, N., \& Wang, W. (2022). Spatiotemporal dynamics of wetlands and their driving factors based on PLS-SEM: A case study in Wuhan. \textit{Science of the Total Environment}, 806, 151310. IF=9.8, SCI \textbf{Q1}
\end{enumerate}

\subsection*{\textbf{2021}}

\begin{enumerate}
\item \textbf{Zhang, Y}., Chen, Z., Zheng, X., Chen, N., \& Wang, Y. (2021). Extracting the location of flooding events in urban systems and analyzing the semantic risk using social sensing data. \textit{Journal of Hydrology}, 603, 127053. IF=6.4, SCI \textbf{Q1}

\item \textbf{Zhang, Y}., Chen, N., Du, W., Li, Y., \& Zheng, X. (2021). Multi-source sensor based urban habitat and resident health sensing: A case study of Wuhan, China. \textit{Building and Environment}, 198, 107883. IF=7.4, SCI \textbf{Q1}

\item Chen, N., \textbf{Zhang, Y*}., Du, W*., Li, Y., Chen, M., \& Zheng, X. (2021). KE-CNN: A new social sensing method for extracting geographical attributes from text semantic features and its application in Wuhan, China. \textit{Computers, Environment and Urban Systems}, 88, 101629. IF=6.8, SSCI \textbf{Q1}

\item \textbf{Zhang, Y}., Zheng, X., Chen, M., Li, Y., Yan, Y., \& Wang, P. (2021). Urban fine-grained spatial structure detection based on a new traffic flow interaction analysis framework. \textit{ISPRS International Journal of Geo-Information}, 10(4), 227. IF=3.4, SCI \textbf{Q2}
% {\color{red}{\textbf{(This Award host journal)}}}

\item Tang, H., Li, Y., \& Zhang, Y. (2021). Wuhan waterlogging risk assessment based on spatial grid and AHP-entropy method. \textit{Urban Geotechnical Investigation \& Surveying}, 18-23. (In Chinese)
\end{enumerate}

\subsection*{\textbf{2020}}

\begin{enumerate}
\item \textbf{Zhang, Y}., Chen, N., Du, W., Yao, S., \& Zheng, X. (2020). A new geo-propagation model of event evolution chain based on public opinion and epidemic coupling. \textit{International Journal of Environmental Research and Public Health}, 17(24), 9235. IF=4.6, SSCI \textbf{Q1}

\item \textbf{Zhang, Y}., Li, Y., \& Zheng, X. (2020). Spatial and temporal analysis of network public opinion evolution of typhoon "Mangkhut" based on Weibo data. \textit{Journal of Shandong University (Engineering Science)}, 50(5), 118-126. (In Chinese)

\item \textbf{Zhang, Y}., Li, Y., \& Zheng, X. (2020). Research on spatiotemporal correlation of population migration patterns in major public health emergencies. \textit{Geomatics \& Spatial Information Technology}. (In Chinese)

\item \textbf{Zhang, Y}., Li, Y., Yang, B., Zheng, X., \& Chen, M. (2020). Risk assessment of COVID-19 based on multisource data from a geographical viewpoint. \textit{IEEE Access}, 8, 125702-125713. IF=3.9, SCI \textbf{Q2}
\end{enumerate}

\subsection*{Patents}

\begin{enumerate}
\item Zhang, Y., et al. (2023). A Method and Device for Predicting and Visualizing Carbon Emissions from Motor Vehicles on Urban Streets CN115455076A.
% 一种城市街道机动车碳排放预测和可视化方法及装置
%2023106131053
%基于街景影像的道路病害特征提取与空间分析方法及系统
%2024118970542
%一种基于遥感影像数据和深度学习的车辆里程估算方法
%2025100111799
\end{enumerate}


% \item Zhang, Y., et al. (2023). Intelligent Analysis and Mining Method and System for Spatiotemporal Processes Based on Multi-Source Big Data. Chinese Patent CN115455076A.

% 一种城市街道机动车碳排放预测和可视化方法及装置
%基于街景影像的道路病害特征提取与空间分析方法及系统
%申请号 2024118970542
%2023106131053


% \section{\faClipboard\ Under Review Paper}

% \datedsubsection{1. \textbf{How Drivers' Perceived Environmental Features Influence Traffic Speed: Integrating Depth Information and SHAP Value}, First Author}
% {{} Travel Behaviour and Society}
% {IF=5.2, SSCI \textbf{Q1}} 

% \datedsubsection{2. \textbf{Human mobility reduces inequality in urban green exposure}, First Author}
% {The Lancet Planetary Health}
% {IF=14.7, SCI \textbf{Q1}} 

\section{\faUniversity\ Awards and Honors}

\datedline{\textit{Ministry of Education}, National Scholarship for Ph.D. Students, {\color{red}{\textbf{Top 3\%}}}}{December 2021}
\datedline{\textit{Ministry of Education}, National Scholarship for Ph.D. Students, {\color{red}{\textbf{Top 3\%}}}}{October 2022}
\datedline{\textit{China Scholarship Council}, Scholarship for Studying Abroad}{May 2021}
\datedline{\textit{Wuhan University}, First-class Academic Scholarship and Outstanding Graduate}{November 2021}
\datedline{\textit{Wuhan University}, First-class Academic Scholarship and Outstanding Graduate}{November 2022}
% \datedline{\textit{Wuhan University}, Outstanding Graduate}{December 2021}
\datedline{\textit{Wuhan Municipal Government}, Third Prize in the City Data Development Competition (First Place Individual Ranking), {\color{red}{\textbf{Top 5\%}}}}{January 2022}
\datedline{\textit{50th Geneva International Exhibition of Inventions}, Vehicle-Kilometrage Estimation Using Remote Sensing Data and Deep Learning (Mei-Po Kwan; \textbf{Yan Zhang}; Jianying Wang, et al.), {\color{red}{\textbf{Bronze Medal, \faTrophy}}}}{April 2025}
\datedline{\textit{Wuhan University}, Top 10 Inspirational Graduate Students (held every two years)}{April 2023}
\datedline{\textit{Wuhan University}, Second Prize for Academic Innovation}{December 2023}
\datedline{\textit{Surveying and Mapping Press}, Excellent Original WeChat Account in the Geoinformation Field (Product and Technology category)}{January 2024}%{Surveying and Mapping Press}


 
\section{\faGlobe\ Project Involvement}
% increase linespacing [parsep=0.5ex]
\begin{itemize}[parsep=0.5ex]
\item National Key R\&D Program of China: "National Public Security Emergency Platform" (2018YFC0807000)
\item National Key R\&D Program of China: "Urban Multi-scale Integrated Perception Service System and Demonstration" (2018YFB2100504)

% \item Science Popularization Capability Enhancement Project for Graduate Students, China Association for Science and Technology (KXYJS2022084)
%\item "Fuzhou Water System Scientific Dispatching System," Changjiang Water Resources Commission, Changjiang Institute of Survey, Planning, Design, and Research ([350100]CX[GK]2018001)

\item Ministry of Education, Singapore: "Multi-scale Digital Twins for the Urban Environment"
% : From Heartbeats to Cities


\item Project funded by the Hong Kong Productivity Council and the Transport Department: "Vehicle Detection and Vehicle-kilometrage Estimation Based on Remote Sensing Technologies"
\end{itemize}

\section{\faUser\ Principal and Co-Principal Investigators Project}

\datedline{\textit{Harvard and Yenching Institute}, China-U.S. Scholars Program (CUSP) Grant (CUS2101001), {\textbf{\$ 3,285 USD}}}{April 2024}

\datedline{\textit{Research on Explainable Causal Analysis Framework for Traffic Congestion Based on Large Model Agents}, Open Fund of State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing (24I04), {\textbf{50,000 Yuan}}}{Jan 2025}

\section{\faBook\ Joint Supervision of Master's Thesis}

\datedline{\textit{Wuhan University}, \textbf{Title: }Extraction of Road Disease Characteristics and Analysis of Spatial Influencing Factors in Wuhan City, {\textbf{Name:}Congpu Hao}}{2023}
\datedline{\textit{The China University of Geosciences}, \textbf{Title:} Research on Location Description Extraction and Scene Risk Identification for Typical Urban Crime Incidents, {\textbf{Name:}Zheng Xu}}{2024}

\datedline{\textit{The China University of Geosciences}, \textbf{Title:} Estimation Method for Urban Road Taxi Carbon Emissions Map Based on Street View and Road Network Structure Using Graph Neural Networks, {\textbf{Name:}Tongxu Zou}}{2024}


\section{\faCogs\ Research Interests}
% increase linespacing [parsep=0.5ex]
~A(Method: GeoAI and social sensing) $ \times $ B(urban science, disaster response, and inequality):


\begin{itemize}[parsep=0.5ex]
\item \textbf{Micro-scale Urban Perception:} Focusing on urban sensing devices and crowdsourced data for urban function and traffic modeling. 
\item \textbf{Disaster Emergency Management:} Integrating NLP techniques with geo-tagged social media data for the real-time, data-driven and decision-making disaster response.
\item \textbf{Environmental Health and Inequality:} Understand urban human-social systems based on spatial-temporal big data.
\end{itemize}


\section{\faTrophy\ Academic Engagements}
\datedline{\textit{{\color{red}Guest Chair Editor}}, IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (Special Issue: Street View Imagery and GeoAI, IF: 5.5)}{{SCI Q1}}

\datedline{\textit{{\color{red}Youth Editor}}, Human Settlements and Sustainability}

\datedline{\textit{Membership}, Association for Computing Machinery}{{ACM}}

% \datedline{\textit{Membership},International Society for Photogrammetry and Remote Sensing}{{ISPRS}}

\datedline{\textit{Membership},Association of American Geographers}{{AAG}}

\datedline{\textit{Membership},IEEE Geoscience and Remote Sensing }{{GRSS}}

\datedline{\textit{Reviewer}, Environment International}{{SCI Q1}}

\datedline{\textit{Reviewer},Computers, Environment and Urban Systems}{{SSCI Q1}}

\datedline{\textit{Reviewer}, Language Resources and Evaluation}{{SCI Q1}}

% \datedline{\textit{Reviewer}, Transactions in Urban Data, Science and Technology}

%{{Domestic Journal}}

\datedline{\textit{Reviewer}, Transactions in GIS}{{SSCI Q2}}

\datedline{\textit{Reviewer}, Environmental Impact Assessment Review}{{SCI Q1}}
% Environmental Impact Assessment Review

\datedline{\textit{Reviewer}, Cities}{{SSCI Q1}}

\datedline{\textit{Reviewer}, Applied Geography}{{SCI Q1}}

\datedline{\textit{Reviewer}, Geoscience Letters}{{SCI Q1}}

\datedline{\textit{Reviewer}, International Journal of Applied Earth Observation and Geoinformation}{{SCI Q1}}

\datedline{\textit{Reviewer}, Journal of Environment \& Development}{{SCI Q1}}

\datedline{\textit{Reviewer}, Remote Sensing of Environment}{{SCI Q1}}

\datedline{\textit{Reviewer}, ISPRS Journal of Photogrammetry and Remote Sensing}{{SCI Q1}}


\datedline{\textit{Reviewer}, Science of the Total Environment}{{SCI Q1}}

\datedline{\textit{Reviewer}, Journal of Environment Management}{{SCI Q1}}

\datedline{\textit{Reviewer}, Remote Sensing}{{SCI Q1}}

\datedline{\textit{Reviewer}, Energies}{{SCI Q1}}

\datedline{\textit{Reviewer}, Journal of Cleaner Production}{{SSCI Q1}}

\datedline{\textit{Reviewer}, Plos One}{{SCI Q1}}

\datedline{\textit{Reviewer}, IEEE Access}{{SCI Q2}}

\datedline{\textit{Reviewer}, International Journal of Crowd Science}{{EI}}

\datedline{\textit{Reviewer}, Environment and Planning B: Urban Analytics and City Science}{{SSCI SCI Q1}}

\datedline{\textit{Reviewer}, Landscape and Urban Planning}{{SCI SCI Q1}}


\datedline{\textit{Reviewer}, Climatic Change}{{SCI Q1}}

\datedline{\textit{Reviewer}, Transportation Research Part C: Emerging Technologies}{{SCI Q1}}

\datedline{\textit{Reviewer}, Transportation Research Part D: Transport and Environment}{{SCI Q1}}

\datedline{\textit{Reviewer}, Journal of Hydrology}{{SCI Q1}}

\datedline{\textit{Reviewer}, Environmental Science and Pollution Research}{{SCI Q1}}

\datedline{\textit{Reviewer}, IEEE Transactions on Intelligent Transportation Systems}{{SCI Q1}}

\datedline{\textit{Reviewer}, Journal of Remote Sensing}{{SCI Q1}}

\section{\faBook\ Invited Talks}

\begin{enumerate}
\item Academic presentation at the 2019 China Public Security Congress, 2019, Beijing.
\item Academic presentation at the 2025 AAG Annual Meeting, 2025, Detroit.
\item Academic presentation at The 2nd International Conference on Urban Informatics, 2023, Hong Kong.
\item Guest speaker at the Jianbai Academic Salon, No. 68, Wuhan University
\item The Surveying and Remote Sensing Star Lake Café, No. 28, Wuhan University
\item Guest speaker at the 288th Doctoral Salon of Wuhan University
\item Future Spatiotemporal Salon of the National GIS Center, China University of Geosciences, Third Session.
\item Academic presentation at the 2025 AAG Annual Meeting (Detroit, Mich.)
\item Academic presentation at the Institute of Space and Earth Information Science (ISEIS)
\item Personal academic WeChat Official Account, "Sensingcity," with over 17,000 followers and accumulated readings exceeding 1,000,000.
\item Related work and experience have been reported by China Daily News, China Youth Net, Wuhan University News Network and Tencent News.

%相关工作及经历被中国青年网、武汉大学新闻网、腾讯新闻报道
\end{enumerate}

%% Reference
%\newpage
%\bibliographystyle{IEEETran}
%\bibliography{mycite}

% 第二届先进遥感国际研讨会暨2023年武汉遥感周拟于2023年10月13日-15日在武汉召开。

%  4.9

%\section{\faComments\ Conference}
%\begin{itemize}[parsep=0.5ex]
%\item Global Conference on Climate Change Polar Studies, Environmentand Climate Change

%\item Global Smart Cities Summit cum The 3rd International Conference on Urban Informatics (ICUI 2023) 
%\end{itemize}

\end{document}