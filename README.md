# 3D Pressure Sore Tissue Model

A portfolio-ready, reproducible framework for documenting a multilayer pressure-sore tissue phantom developed at Arizona State University.

## Project scope

- 60 × 60 × 12 mm multilayer tissue model
- Epidermis, dermis, subcutaneous tissue, and bone interface
- Spherical, steep-dome, and triangular loading geometries
- Static loading cases at 1, 5, 10, 15, and 20 kPa
- Stress, strain, and displacement summaries
- Embedded sensor-channel design and SLA fabrication workflow

## Repository status

This public repository contains documentation and reusable analysis utilities. Original CAD/FEA files and raw experimental artifacts will be added only after confirming ownership and sharing permissions. The sample data are synthetic.

## Structure

- `src/`: result-validation and summary tools
- `examples/`: synthetic result table
- `docs/`: experiment and fabrication notes
- `data/`, `outputs/`: ignored local working folders

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/summarize_results.py examples/synthetic_results.csv
```

## Selected reported result

For the steep-dome geometry at 20 kPa: maximum displacement 4.283 mm and average displacement 3.167 mm. Treat this as a documented project result, not a benchmark.

## Ethics and reuse

This is an engineering research portfolio, not a validated clinical device or diagnostic system.

## License

MIT for code and original documentation. Third-party assets retain their original terms.
