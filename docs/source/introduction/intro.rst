General Introduction
====================

The **GCAM-Europe** model is an expansion of the Global Change Analysis Model (GCAM), a widely used
Integrated Assessment Model (IAM) for global scenario analysis (Calvin et al., 2019). GCAM is a
technology-rich, bottom-up model that represents interactions between the economy, energy system,
land use, water resources, and the climate system.

The model is designed to explore long-term transition pathways under different climate and policy
scenarios, including carbon pricing, emissions trading systems, regulatory instruments, and accelerated
technology deployment. It links socio-economic drivers such as population and labor productivity growth
to energy demand, land-use change, and water use, which are represented through a wide range of
technology options for energy supply, transformation, and end-use services, as well as agricultural
and forestry production systems.

A complete description of the global GCAM framework is available in the official documentation:
https://github.com/JGCRI/gcam-core.com


Geographical resolution in GCAM-Europe
--------------------------------------

GCAM divides the global economy into 32 regions, with Europe originally represented through several
aggregated regional groupings (EU-12, EU-15, Eastern Europe, non-EU Europe, and EFTA).

GCAM-Europe significantly refines this representation by disaggregating the European continent into
39 individual countries, each represented as a separate model region. This increased spatial resolution
allows for a more detailed assessment of national-level climate and energy policy impacts, while
maintaining consistency with the global GCAM structure.

In addition, the model preserves the rest of the world as defined in the original GCAM regional
classification, enabling the analysis of international spillovers such as carbon leakage and trade
effects across a representative set of global regions.


Model characteristics and extensions
------------------------------------

GCAM-Europe extends the standard GCAM framework by introducing Europe-specific data sources and
additional sectoral detail. Whenever available, European datasets (e.g., Eurostat energy statistics)
are used to replace default global assumptions. In cases where country-level data are incomplete,
the model reverts to standard GCAM input datasets (e.g., IEA statistics) to ensure completeness and
consistency.

Key model extensions include:

- Enhanced representation of residential energy demand, including new end-use categories such as
  hot water, cooking, and household appliances
- Introduction of emerging technologies such as heat pumps
- Increased granularity in consumer segmentation in the residential sector, based on country-level
  data availability
- Improved representation of the European Single Market for selected sectors, allowing for trade
  between European countries

The model also represents an interconnected electricity system structured into grid regions and
load segments, enabling a more detailed representation of electricity flows, storage options, and
temporal variability in supply and demand.


Model dynamics and outputs
--------------------------

GCAM-Europe operates over the period 1990–2100 in five-year time steps. The model simulates the
evolution of energy systems, land use, water use, and economic activity under exogenous assumptions
regarding population, economic growth, technological change, and policy constraints.

Model outputs include projections of:

- Energy supply and demand
- Land-use and agricultural activity
- Greenhouse gas emissions (16 gases), aerosols, and short-lived climate forcers
- Radiative forcing and climate-related indicators

These outputs can be used to evaluate the implications of climate mitigation policies and transition
pathways at both European and global scales.