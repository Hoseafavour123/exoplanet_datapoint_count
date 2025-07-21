# 🪐 Exoplanet Observation Data Counter

[ Live Demo](https://exocounter.onrender.com)

This is a simple and interactive web application that helps you **quickly count the number of observational datapoints** (each representing an image or snapshot) in a `.json` dataset collected from telescopic surveys.

Test it now at: 

## Purpose

In exoplanet transit studies, researchers often work with large datasets containing flux and timing information derived from sequences of stellar images. This tool provides a **drag-and-drop interface** to instantly:

- Count the number of image datapoints.
- Preview the structure of the observation file.
- View the first few records for quick verification.

---

##  Features

- Drag-and-drop `.json` file upload.
- Automatic count of image observation rows.
- Displays field headers (e.g., time, flux, error).
- Preview of the first 5 datapoints.
- Handles malformed or incomplete files gracefully.

---

## Sample JSON Format

The JSON file is expected to be a **list of lists**, where:

- The first list contains field headers (e.g., `["BJD_TDB", "RNFLUX", "ERROR", ...]`).
- Each subsequent list is a single image observation.

```json
[
  ["BJD_TDB", "RNFLUX", "ERROR", "AIRMASS", "AIRMASS CORR"],
  ["2459926.8454252", "1.0284138", "0.0140699", "1.0391256", "1.0100487"],
  ["2459926.84615537", "1.008285", "0.0140687", "1.0379428", "1.0096675"],
  ...
]
