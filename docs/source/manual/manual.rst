Software and hardware requirements
==================================

GCAM-Europe is distributed as a pre-configured release based on the Global
Change Analysis Model (GCAM). The release includes all files required to run
the reference model and therefore does not require users to compile the model
from source. The repository contains the complete workflow, from data
pre-processing to model execution and output visualisation.

Software requirements
---------------------

The GCAM-Europe release provides a complete working environment. Additional
software is only required for specific tasks within the modelling workflow.

The following software components are used:

- **R**, required to run the data system that prepares the model input data.
- **gcamdata**, the R package responsible for reading the raw input datasets,
  processing them, and generating the XML files used by GCAM.
- **Java Runtime Environment (JRE)**, required to run the GCAM
  ``ModelInterface`` for exploring model outputs and executing database queries.

GCAM itself is implemented in **C++**, although users of the distributed
release do not need to interact with the source code or compile the model.

Further information about the GCAM workflow and software architecture is
available in the official GCAM documentation:

https://jgcri.github.io/gcam-doc/user-guide.html

Hardware requirements
---------------------

The computational requirements of GCAM-Europe depend on the selected scenario
and model configuration. A modern multi-core processor and sufficient memory
are recommended for efficient execution.

.. list-table::
   :header-rows: 1
   :widths: 45 25

   * - Component
     - Minimum requirement
   * - Processor
     - 64-bit multi-core CPU
   * - Memory (RAM)
     - 4 GB
   * - Available disk space
     - At least 9 GB
   * - Operating system
     - 64-bit Windows, Linux, or macOS

Repository structure
====================

The GCAM-Europe repository is organised into a number of directories
corresponding to different stages of the modelling workflow.

::

   CONTRIBUTING.md
   LICENSE.md
   README.md
   Makefile

   exe/
   input/
   output/
   ModelInterface/
   libs/
   cvs/
   util/

The main directories are described below.

``input/``
-----------

The ``input`` directory contains the complete GCAM data system.

This includes:

- the R scripts that configure and execute the data system;
- the initial input datasets;
- the **gcamdata** package configuration; and
- the XML files generated during data processing.

The data system reads the raw input datasets, performs all necessary
pre-processing steps, and generates a complete set of XML files describing the
GCAM-Europe model. These XML files constitute the direct inputs to the GCAM
simulation engine.

``exe/``
--------

The ``exe`` directory contains the executable version of GCAM-Europe.

Model simulations should be launched using ``run_gcam.bat``, which executes
GCAM with the appropriate configuration. The executable itself
(``gcam.exe``) is normally not run directly.

This directory also contains the main configuration file
(``configuration.xml``), which controls the simulation settings, including:

- the simulation time horizon;
- the location of output files;
- the XML input files included in the model;
- and the policy files activated for a given scenario.

Policy files are provided as additional XML files specifying assumptions such
as carbon prices, taxes, subsidies and other policy measures affecting
different regions, markets and simulation periods.

``output/``
-----------

The ``output`` directory stores the results generated after each model run.

By default, simulation outputs are written to this directory, although the
destination can be modified through ``configuration.xml``.

This directory also contains the XML query files used by the GCAM
``ModelInterface`` to retrieve specific information from the output database.

``ModelInterface/``
-------------------

The ``ModelInterface`` directory contains the Java-based graphical interface
used to inspect GCAM output databases.

The software allows users to execute predefined XML queries, explore simulation
results and export selected outputs for further analysis.

``libs/`` and ``cvs/``
----------------------

These directories contain the C++ libraries and supporting configuration files
required internally by GCAM.

Users working with the distributed release normally do not need to modify these
directories.

Workflow overview
=================

The GCAM-Europe modelling workflow consists of three main stages.


1. **Data preparation**

   The data system, implemented in R through the ``gcamdata`` package, reads
   the raw input datasets and generates the XML files required by GCAM.


2. **Model execution**

   The generated XML files are read by the GCAM simulation engine, implemented
   in C++, which executes the selected scenario according to the options
   defined in ``configuration.xml``.


3. **Output analysis**

   Simulation results are stored in the output database and can be explored
   using the Java-based ``ModelInterface`` or exported for further analysis.

   In addition, scenario outputs can be analysed programmatically using external tools:

   - **R-based workflow** using the ``rgcam`` package, which allows direct access
     to GCAM databases for post-processing, scenario comparison, and visualization.

   - **Python-based workflow** using the ``gcamreader`` package, enabling automated
     extraction of results, integration with scientific Python stacks (e.g. pandas,
     numpy, matplotlib), and advanced scenario analysis.

   These tools facilitate reproducible and flexible analysis of GCAM-Europe outputs
   outside the native ModelInterface environment.