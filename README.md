# 3D Pressure Sore Tissue Model

I developed this applied research project at Arizona State University under Dr. Vincent Pizziconi to study how localized pressure can deform layered soft tissue. I designed a 60 x 60 x 12 mm multilayer skin phantom, compared three bone-interface geometries, and evaluated mechanical behavior across five pressure levels.

## Work I completed

- Built the epidermis, dermis, and subcutaneous tissue geometry in SolidWorks.
- Created spherical, steep-dome, and triangular bone-interface configurations.
- Defined bonded tissue interfaces, a fixed bone base, and a non-penetrating compression contact.
- Completed 15 simulation cases at 1, 5, 10, 15, and 20 kPa.
- Recorded maximum and average displacement, strain, and von Mises stress.
- Designed a branched sensor channel with one inlet and one outlet for future pressure, shear, and thermal sensing.
- Prepared the fabrication workflow, research poster, and Applied Project Showcase presentation.

## Selected result

For the steep-dome geometry at 20 kPa, I recorded 4.283 mm maximum displacement, 3.167 mm average displacement, 2.869 maximum strain, and 1.211 MPa maximum von Mises stress.

## Repository features

- `src/summarize_results.py` validates a simulation-results table and summarizes peak response by geometry.
- `src/compare_geometries.py` compares geometry sensitivity across matched loading levels.
- `examples/synthetic_results.csv` demonstrates the expected table format without exposing unpublished source files.
- `docs/EXPERIMENT_PLAN.md` records the validation and testing plan.

## Run the analysis

```bash
python -m pip install -r requirements.txt
python src/summarize_results.py examples/synthetic_results.csv
python src/compare_geometries.py examples/synthetic_results.csv
```

## Tools

SolidWorks, finite element analysis, CAD, Formlabs/PreForm, additive manufacturing, mechanical testing, Python, pandas.

## Data and design note

The code is provided with synthetic example data. Original CAD assemblies, proprietary fabrication files, and research records are not included unless cleared for public release.

## Author

Hritika Adhikary - M.S. Biomedical Engineering, Arizona State University.

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
