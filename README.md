# Curriculum vitae

This is my curriculum vitae.

## Requirements

 - 2 main targets: latex pdf to be deployed during releases in github registries and whatever tool that takes as input a config file (md or YAML) and returns a static site to be deployed in GHP
- it should have a single source of truth
- that source should be either directly compatible with latex builder (i.e. a tex file) or directly compatible with GHP deployment (i.e. an md or YAML file)
- my only job should be then create a converter from the source of truth (e.g. YAML) to the other deployment (e.g. latex)
- all these deployments should be done automatically through GH workflows 
