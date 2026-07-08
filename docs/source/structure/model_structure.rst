Model Structure
===============

The Global Change Analysis Model (GCAM)
---------------------------------------

The Global Change Analysis Model (GCAM) is an open-source integrated assessment
model (IAM) developed to explore long-term interactions between human and Earth
systems under alternative socioeconomic, technological, and policy assumptions.
Rather than predicting the future, GCAM evaluates *what-if* scenarios,
supporting analyses of energy systems, land use, water resources, emissions,
economic development, and climate change over the period 1990--2100 in
five-year time steps.

GCAM represents the coupled evolution of multiple sectors within a
recursive-dynamic partial-equilibrium framework. Market prices are determined
endogenously through supply-demand equilibrium, allowing interactions and
feedbacks to emerge consistently across energy, agriculture, forestry and land
use (AFOLU), water, the economy, emissions, and the climate system.

The model has been continuously developed for more than three decades by the
Joint Global Change Research Institute (JGCRI) and is maintained as an
open-source community model. Source code, documentation, and input datasets are
publicly available, enabling users to extend the model, develop regional
implementations, and contribute improvements back to the community.

The core GCAM framework consists of several tightly coupled components:

* Energy systems
* Agriculture, Forestry and Land Use (AFOLU)
* Water resources
* Macroeconomic drivers
* Emissions
* Climate

Further information on the global GCAM framework is available in the official
documentation:

https://github.com/JGCRI/gcam-doc


From GCAM to GCAM-Europe
------------------------

GCAM-Europe builds directly upon the GCAM core framework. Rather than
developing a new integrated assessment model from scratch, GCAM-Europe extends
the global model by increasing the spatial, technological, and behavioural
resolution of Europe while preserving the global consistency of GCAM.

The development of GCAM-Europe is based on two complementary principles:

* **Regional disaggregation**, replacing aggregated European regions with
  explicit country-level representation.

* **Regional refinement**, incorporating European datasets and introducing
  structural enhancements tailored to European technologies, markets, and
  policy analyses.

Because GCAM-Europe preserves the underlying architecture of GCAM, the standard
workflow, XML configuration, calibration procedure, and model execution remain
unchanged. Users familiar with GCAM can therefore work with GCAM-Europe using
the same modelling workflow while benefiting from a substantially more detailed
representation of Europe.


Main structural extensions
--------------------------

GCAM-Europe extends the core GCAM framework through several structural
enhancements designed to improve the representation of European energy systems,
markets, technologies, households, and socioeconomic conditions.

Regional representation
^^^^^^^^^^^^^^^^^^^^^^^

GCAM-Europe replaces the five aggregated European regions of the global model
with explicit country-level representation.

The model includes all 27 European Union Member States together with additional
European countries such as the United Kingdom and Switzerland. For land-use and
water systems, the spatial resolution is further increased through the
definition of 119 land regions based on the intersection of geopolitical
boundaries and major river basins.

This regionalization enables detailed country-level analyses while preserving
the global interactions represented by the original GCAM framework.

.. figure:: _static/Regional disaggregation in GCAM-Europe.png
   :width: 85%
   :align: center

   Regional representation implemented in GCAM-Europe.


Regional data integration
^^^^^^^^^^^^^^^^^^^^^^^^^

GCAM-Europe replaces many default global datasets with specialized European
data sources wherever available.

Energy statistics are primarily obtained from Eurostat, transportation data are
derived from the JRC-IDEES database, electricity infrastructure is harmonized
with ENTSO-E planning scenarios, and demographic projections follow the
European Commission Ageing Report. Population and macroeconomic drivers are
also consistent with the latest Shared Socioeconomic Pathways (SSPs). When
European data are unavailable, the model falls back to the standard datasets
used by GCAM, ensuring consistency with the global framework.


Energy system
^^^^^^^^^^^^^

The energy system incorporates several structural refinements specifically
designed for European analyses.

**Electricity markets**

Electricity is represented through interconnected grid regions that closely
follow the wholesale electricity regions defined by the European Commission.
Within each grid region, electricity markets are further divided into four
representative load segments (base, intermediate, sub-peak, and peak) derived
from the openTEPES electricity model. This structure enables a more realistic
representation of renewable integration, electricity storage, and
cross-border transmission.

.. figure:: _static/Electricity grid regions GCAM-Europe.png
   :width: 85%
   :align: center

   Electricity grid regions represented in GCAM-Europe.

**Variable renewable electricity**

Wind and solar technologies incorporate technology-specific value adjustments
derived from the Regional Energy Deployment System (ReEDS) model. These
adjustments account for the declining market value of intermittent generation
at increasing penetration levels, providing a more realistic representation of
variable renewable electricity deployment.

**Transportation**

The transportation sector is calibrated using the JRC-IDEES database,
providing detailed historical information on energy consumption, technology
deployment, transport activity, and emissions across all major transport modes
for European countries.

**Industrial sectors**

Industrial processes incorporate updated datasets for cement production,
energy intensities, and process emissions, providing a more accurate
representation of one of the most important industrial sources of greenhouse
gas emissions.


Buildings and households
^^^^^^^^^^^^^^^^^^^^^^^^

GCAM-Europe substantially expands the representation of residential energy
demand and household behaviour.

Residential demand is disaggregated into additional end-use categories aligned
with Eurostat statistics, including cooking, domestic hot water, and household
appliances, complementing the standard heating and cooling demands represented
in the global model.

The technology portfolio explicitly represents multiple heat pump
configurations together with solar thermal technologies. Future technology
adoption is represented through country-specific technology preference
trajectories, allowing behavioural aspects of technology diffusion to be
represented alongside conventional cost-based decision making.

Households are stratified into income deciles, enabling the model to capture
heterogeneous residential energy demand, technology adoption, and distributional
effects. Household energy consumption is further informed by survey-based data
derived from the DIAMOND household database, improving the representation of
within-country socioeconomic heterogeneity.


Food system
^^^^^^^^^^^

Food demand is represented across household income deciles, allowing the model
to capture heterogeneous consumption patterns and distributional impacts across
different socioeconomic groups rather than relying on a single representative
consumer.


Commodity trade
^^^^^^^^^^^^^^^

GCAM-Europe extends the standard GCAM Armington trade structure by introducing
a dedicated representation of the European Economic Area (EEA).

While trade between Europe and the rest of the world follows the standard GCAM
trade formulation, intra-European trade is represented through an additional
nested Armington structure with substantially reduced trade barriers. This
allows the model to reproduce the integrated European internal market while
supporting analyses of policies such as the Carbon Border Adjustment Mechanism
(CBAM).

.. figure:: _static/Commodity trade structure GCAM-Europe.png
   :width: 85%
   :align: center

   Trade structure implemented in GCAM-Europe.