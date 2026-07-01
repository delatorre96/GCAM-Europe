Limitations
==========================

Several limitations have been identified in the current implementation of the GCAM-Europe model.
These limitations reflect both structural constraints inherited from the GCAM framework and additional
challenges arising from the regional disaggregation of Europe. The points below summarise key areas
for improvement that can be addressed in future model developments.

a) **Computational complexity**  
   GCAM-Europe increases the spatial resolution of GCAM by explicitly representing individual European
   countries. This additional disaggregation significantly increases computational demand and model run
   time compared to the global GCAM configuration.

   Future improvements could focus on optimisation of data structures, solver efficiency, and potential
   reduction of unnecessary sectoral resolution where appropriate.

b) **Model documentation and transparency**  
   Although GCAM is well documented at the global level, the European disaggregation introduces additional
   layers of complexity that are not yet fully documented in a unified manner.

   Future work will aim to improve documentation of:

   - country-level data structures and harmonisation rules  
   - sectoral mapping between GCAM global regions and European countries  
   - assumptions introduced during downscaling and calibration  

c) **Data harmonisation and regional downscaling**  
   GCAM-Europe relies on the downscaling of global GCAM datasets to European countries. This process
   requires harmonisation of heterogeneous data sources and introduces uncertainty in sectoral and
   country-level allocations.

   In particular, differences in statistical definitions across Eurostat, national inventories, and GCAM
   base datasets may lead to inconsistencies in baseline calibration.

d) **Representation of intra-European heterogeneity**  
   While GCAM-Europe resolves individual countries, intra-country heterogeneity (e.g. regional differences
   within large Member States) is not explicitly represented.

   This may limit the model’s ability to capture sub-national policy effects or regional variation in
   resource availability and technology deployment.

e) **Temporal and technological resolution constraints**  
   As in the original GCAM framework, temporal dynamics are represented in discrete time steps and do not
   fully capture intra-annual variability.

   In addition, certain technologies and transition dynamics may be simplified due to computational
   constraints and data availability at the European level.

f) **Sectoral coupling and simplifications**  
   Although GCAM integrates energy, land, water, and economic systems, some cross-sectoral feedbacks remain
   simplified.

   For example, detailed representations of certain industrial processes or non-CO₂ greenhouse gas pathways
   may not fully capture all mitigation options available in European-specific contexts.

g) **Exogenous demand assumptions**  
   Final energy service demands are largely determined exogenously within GCAM.

   This implies that behavioural changes, structural economic shifts, and policy-induced demand reductions
   are not endogenously modelled but must be introduced through scenario assumptions.

   

References
==========

Ackerman, F., DeCanio, S.J., Howarth, R.B., Sheeran, K., 2009. Limitations of integrated assessment models of climate change. Climatic Change 95, 297–315. https://doi.org/10.1007/s10584-009-9570-x

Aguiar, A., Chepeliev, M., Corong, E., Mensbrugghe, D. van der, 2022. The Global Trade Analysis Project (GTAP) Data Base: Version 11. Journal of Global Economic Analysis 7. https://doi.org/10.21642/JGEA.070201AF

Anderson, K., Jewell, J., 2019. Debating the bedrock of climate-change mitigation scenarios. Nature 573, 348–349. https://doi.org/10.1038/d41586-019-02744-9

Bertram, C., Brutschin, E., Drouet, L., Luderer, G., van Ruijven, B., Aleluia Reis, L., Baptista, L.B., de Boer, H.-S., Cui, R., Daioglou, V., Fosse, F., Fragkiadakis, D., Fricko, O., Fujimori, S., Hultman, N., Iyer, G., Keramidas, K., Krey, V., Kriegler, E., Lamboll, R.D., Mandaroux, R., Rochedo, P., Rogelj, J., Schaeffer, R., Silva, D., Tagomori, I., van Vuuren, D., Vrontisi, Z., Riahi, K., 2024. Feasibility of peak temperature targets in light of institutional constraints. Nat. Clim. Chang. 14, 954–960. https://doi.org/10.1038/s41558-024-02073-4

Binsted, M., Iyer, G., Patel, P., Graham, N.T., Ou, Y., Khan, Z., Kholod, N., Narayan, K., Hejazi, M., Kim, S., Calvin, K., Wise, M., 2022. GCAM-USA v5.3_water_dispatch: integrated modeling of subnational US energy, water, and land systems within a global framework. Geoscientific Model Development 15, 2533–2559. https://doi.org/10.5194/gmd-15-2533-2022

Bistline, J.E.T., Binsted, M., Blanford, G., Boyd, G., Browning, M., Cai, Y., Edmonds, J., Fawcett, A.A., Fuhrman, J., Gao, R., Harris, C., Hoehne, C., Iyer, G., Johnson, J.X., Kaplan, P.O., Loughlin, D., Mahajan, M., Mai, T., McFarland, J.R., McJeon, H., Melaina, M., Mousavi, S.S., Muratori, M., Orvis, R., Prabhu, A., Rossmann, C., Sands, R.D., Sarmiento, L., Showalter, S., Sinha, A., Starke, E., Stewart, E., Vaillancourt, K., Weyant, J., Wood, F., Yuan, M., 2025. Policy implications of net-zero emissions: A multi-model analysis of United States emissions and energy system impacts. Energy and Climate Change 6, 100191. https://doi.org/10.1016/j.egycc.2025.100191

Bond-Lamberty, B., Patel, P., Lurz, J., Kyle, P., kvcalvin, Smith, S., abigailsnyder, Dorheim, K.R., mbins, Link, R., skim301, Narayan, K., nealtg, S, A., enlochner, Feng, L., cwroney, Lynch, C., jhoring, Khan, Z., rhoesly, Zhao, X., Durga, S., orourkepr, JonathanHuster, Haewon, Waite, T., Ou, Y., marideeweber, Iyer, G., 2025. JGCRI/gcam-core: GCAM 8.2. https://doi.org/10.5281/zenodo.15581174

Braunreiter, L., van Beek, L., Hajer, M., van Vuuren, D., 2021. Transformative pathways – Using integrated assessment models more effectively to open up plausible and desirable low-carbon futures. Energy Research & Social Science 80, 102220. https://doi.org/10.1016/j.erss.2021.102220

Brutschin, E., Pianta, S., Tavoni, M., Riahi, K., Bosetti, V., Marangoni, G., Van Ruijven, B.J., 2021. A multidimensional feasibility evaluation of low-carbon scenarios. Environmental Research Letters 16, 064069.

Calvin, K., Bond-Lamberty, B., Clarke, L., Edmonds, J., Eom, J., Hartin, C., Kim, S., Kyle, P., Link, R., Moss, R., 2017. The SSP4: A world of deepening inequality. Global Environmental Change 42, 284–296.

Calvin, K., Patel, P., Clarke, L., Asrar, G., Bond-Lamberty, B., Cui, R.Y., Vittorio, A.D., Dorheim, K., Edmonds, J., Hartin, C., 2019. GCAM v5. 1: representing the linkages between energy, water, land, climate, and economic systems. Geoscientific Model Development 12, 677–698.

Capros, P., Van Regemorter, D., Paroussos, L., Karkatsoulis, P., Fragkiadakis, C., Tsani, S., Charalampidis, I., Revesz, T., Perry, M., Abrell, J., 2013. GEM-E3 model documentation. JRC Scientific and Policy Reports 26034.

Chaturvedi, V., Malyan, A., 2022. Implications of a net-zero target for India’s sectoral energy transitions and climate policy. Oxf Open Clim Chang 2, kgac001. https://doi.org/10.1093/oxfclm/kgac001

Criqui, P., Mima, S., Menanteau, P., Kitous, A., 2015. Mitigation strategies and energy technology learning: An assessment with the POLES model. Technological Forecasting and Social Change 90, 119–136. https://doi.org/10.1016/j.techfore.2014.05.005

Dooley, K., Christiansen, K.L., Lund, J.F., Carton, W., Self, A., 2024. Over-reliance on land for carbon dioxide removal in net-zero climate pledges. Nat Commun 15, 9118. https://doi.org/10.1038/s41467-024-53466-0

Emmerling, J., Andreoni, P., Charalampidis, I., Dasgupta, S., Dennig, F., Feindt, S., Fragkiadakis, D., Fragkos, P., Fujimori, S., Gilli, M., Grottera, C., Guivarch, C., Kornek, U., Kriegler, E., Malerba, D., Marangoni, G., Méjean, A., Nijsse, F., Piontek, F., Simsek, Y., Soergel, B., Taconet, N., Vandyck, T., Young-Brun, M., Zhao, S., Zheng, Y., Tavoni, M., 2024. A multi-model assessment of inequality and climate change. Nat. Clim. Chang. 14, 1254–1260. https://doi.org/10.1038/s41558-024-02151-7

Fisher-Vanden, K., Weyant, J., 2020. The evolution of integrated assessment: Developing the next generation of use-inspired integrated assessment tools. Annual Review of Resource Economics 12, 471–487.

GAGO, D., Nijs, W., RUIZ, C.P., Sgobbi, A., Radu, D., Bolat, P., Thiel, C., PETEVES, E., 2013. The JRC-EU-TIMES model-Assessing the long-term role of the SET Plan Energy technologies.

Gambhir, A., Butnar, I., Li, P.-H., Smith, P., Strachan, N., 2019. A Review of Criticisms of Integrated Assessment Models and Proposed Approaches to Address These, through the Lens of BECCS. Energies 12, 1747. https://doi.org/10.3390/en12091747

Geels, F.W., Berkhout, F., van Vuuren, D.P., 2016. Bridging analytical approaches for low-carbon transitions. Nature Clim Change 6, 576–583. https://doi.org/10.1038/nclimate2980

harrisson,  thomas, 2018. Q&A: How “integrated assessment models” are used to study climate change. Carbon Brief. URL https://www.carbonbrief.org/qa-how-integrated-assessment-models-are-used-to-study-climate-change/ (accessed 6.26.26).

IAMC, 2022. IAMC Documentation Wiki.

IPCC, 2022. Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [P.R. Shukla, J. Skea, R. Slade, A. Al Khourdajie, R. van Diemen, D. McCollum, M. Pathak, S. Some, P. Vyas, R. Fradera, M. Belkacemi, A. Hasija, G. Lisboa, S. Luz, J. Malley, (eds.)].

Jeon, S., Roh, M., Kim, S., 2021. The derivation of sectoral and provincial implications from power sector scenarios using an integrated assessment model at Korean provincial level: GCAM-Korea. Energy Strategy Reviews 38, 100694. https://doi.org/10.1016/j.esr.2021.100694

Kamboj, P., Qiu, Y., Graham, N., Kyle, P., Apeaning, R., Iyer, G., Hejazi, M., 2026. GCAM-KSA: A country-specific integrated assessment model for long-term energy, water, land, and climate analysis of Saudi Arabia. https://doi.org/10.2139/ssrn.6669308

Kazlou, T., Cherp, A., Jewell, J., 2024. Feasible deployment of carbon capture and storage and the requirements of climate targets. Nat. Clim. Chang. 14, 1047–1055. https://doi.org/10.1038/s41558-024-02104-0

Keppo, I., Butnar, I., Bauer, N., Caspani, M., Edelenbosch, O., Emmerling, J., Fragkos, P., Guivarch, C., Harmsen, M., Lefevre, J., 2021. Exploring the possibility space: taking stock of the diverse capabilities and gaps in integrated assessment models. Environmental Research Letters 16, 053006.

Kikstra, J.S., Nicholls, Z.R.J., Smith, C.J., Lewis, J., Lamboll, R.D., Byers, E., Sandstad, M., Meinshausen, M., Gidden, M.J., Rogelj, J., Kriegler, E., Peters, G.P., Fuglestvedt, J.S., Skeie, R.B., Samset, B.H., Wienpahl, L., van Vuuren, D.P., van der Wijst, K.-I., Al Khourdajie, A., Forster, P.M., Reisinger, A., Schaeffer, R., Riahi, K., 2022. The IPCC Sixth Assessment Report WGIII climate assessment of mitigation pathways: from emissions to global temperatures. Geoscientific Model Development 15, 9075–9109. https://doi.org/10.5194/gmd-15-9075-2022

Koasidis, K., Nikas, A., Doukas, H., 2023. Why integrated assessment models alone are insufficient to navigate us through the polycrisis. One Earth 6, 205–209.

Lamb, W.F., Gasser, T., Roman-Cuesta, R.M., Grassi, G., Gidden, M.J., Powis, C.M., Geden, O., Nemet, G., Pratama, Y., Riahi, K., Smith, S.M., Steinhauser, J., Vaughan, N.E., Smith, H.B., Minx, J.C., 2024. The carbon dioxide removal gap. Nat. Clim. Chang. 14, 644–651. https://doi.org/10.1038/s41558-024-01984-6

Low, S., Brutschin, E., Baum, C.M., Sovacool, B.K., 2025. Expert perspectives on incorporating justice considerations into integrated assessment modelling. npj Climate Action 4, 10.

Maryland, C. for G.S. at U. of, University, D. of E.S.S. at T., Sciences, C. of E., University, E. at P., 2025. umd-cgs/gcam-china: gcam-china-v7.1. https://doi.org/10.5281/zenodo.15499108

Oberthür, S., Dupont, C., 2021. The European Union’s international climate leadership: towards a grand climate strategy? Journal of European Public Policy 28, 1095–1114. https://doi.org/10.1080/13501763.2021.1918218

Skea, J., Shukla, P., Al Khourdajie, A., McCollum, D., 2021. Intergovernmental Panel on Climate Change: Transparency and integrated assessment modeling. Wiley Interdisciplinary Reviews: Climate Change 12, e727.

Sognnaes, I., Peters, G.P., 2025. Influence of individual models and studies on quantitative mitigation findings in the IPCC Sixth Assessment Report. Nat Commun 16, 8343. https://doi.org/10.1038/s41467-025-64091-w

van Beek, L., Hajer, M., Pelzer, P., van Vuuren, D., Cassen, C., 2020. Anticipating futures through models: the rise of Integrated Assessment Modelling in the climate science-policy interface since 1970. Global Environmental Change 65, 102191.

van de Ven, D.-J., Mittal, S., Gambhir, A., Lamboll, R.D., Doukas, H., Giarola, S., Hawkes, A., Koasidis, K., Köberle, A.C., McJeon, H., Perdana, S., Peters, G.P., Rogelj, J., Sognnaes, I., Vielle, M., Nikas, A., 2023. A multimodel analysis of post-Glasgow climate targets and feasibility challenges. Nat. Clim. Chang. 13, 570–578. https://doi.org/10.1038/s41558-023-01661-0

van Vuuren, D., O’Neill, B., Tebaldi, C., Chini, L., Friedlingstein, P., Hasegawa, T., Riahi, K., Sanderson, B., Govindasamy, B., Bauer, N., Eyring, V., Fall, C., Frieler, K., Gidden, M., Gohar, L., Jones, A., King, A., Knutti, R., Kriegler, E., Lawrence, P., Lennard, C., Lowe, J., Mathison, C., Mehmood, S., Prado, L., Zhang, Q., Rose, S., Ruane, A., Schleussner, C.-F., Seferian, R., Sillmann, J., Smith, C., Sörensson, A., Panickal, S., Tachiiri, K., Vaughan, N., Vishwanathan, S., Yokohata, T., Ziehn, T., 2025. The Scenario Model Intercomparison Project for CMIP7 (ScenarioMIP-CMIP7) &nbsp; EGUsphere 1–38. https://doi.org/10.5194/egusphere-2024-3765

Weyant, J., 2017. Some contributions of integrated assessment models of global climate change. Review of Environmental Economics and Policy.

Yarlagadda, B., Wild, T., Zhao, X., Clarke, L., Cui, R., Khan, Z., Birnbaum, A., Lamontagne, J., 2023. Trade and Climate Mitigation Interactions Create Agro-Economic Opportunities With Social and Environmental Trade-Offs in Latin America and the Caribbean. Earth’s Future 11, e2022EF003063. https://doi.org/10.1029/2022EF003063

Younis, O., Davies, E.G.R., Chiappori, D.V., Binsted, M., Siddiqui, M.-S., Arbuckle, E.J., Macaluso, N., 2025. Exploring water use pathways under deep decarbonization scenarios in Canada at subnational scales using GCAM-Canada. Journal of Environmental Management 391, 126416. https://doi.org/10.1016/j.jenvman.2025.126416

Zhao, A., O’Keefe, K.T.V., Binsted, M., McJeon, H., Bryant, A., Squire, C., Zhang, M., Smith, S.J., Cui, R., Ou, Y., Iyer, G., Kennedy, S., Hultman, N., 2024. High-ambition climate action in all sectors can achieve a 65% greenhouse gas emissions reduction in the United States by 2035. npj Clim. Action 3, 63. https://doi.org/10.1038/s44168-024-00145-x

