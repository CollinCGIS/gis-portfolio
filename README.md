# Environmental GIS Portfolio

A portfolio site covering five environmental GIS projects, with an interactive demo of the
method behind each one, the analysis code, and a set of browser-based GIS utilities.

**Live site:** _add your URL here once it is deployed_

## Projects

| Project | Question | Methods |
|---|---|---|
| Urban Heat Island | Which neighborhoods run hottest, and how much follows pavement? | Raster analysis, zonal statistics, regression |
| Watershed Water Quality | Is nutrient pollution rising or falling, and is the change real? | Time series, Mann-Kendall test, data cleaning |
| Wildfire Risk | Where do slope, aspect and fuel combine into the highest risk? | Weighted overlay, terrain analysis, validation |
| Coastal Erosion | Which parts of the coast are exposed as water rises? | DEM analysis, scenario modeling, change detection |
| Air Quality and Equity | Who lives where the air is worst? | Spatial interpolation, spatial joins, bivariate mapping |

All five are built on public data from USGS, NOAA, EPA, the US Census Bureau, NASA Landsat,
LANDFIRE, MTBS and NLCD. Each project page lists its sources with download links.

## What is in this repository

```
index.html        the complete site, one self-contained file -- this is what gets served
artifact.html     the same page without the <html>/<head> wrapper (for publishing inside Claude)
build.py          rebuilds both files from the parts below
src/              page markup, styles and scripts
code/             the analysis snippets shown on the Code page
.nojekyll         tells GitHub Pages to serve the files as-is
```

### Analysis code

`code/` holds the snippets rendered on the site's Code page. The site reads them from these
files at build time, so what a visitor sees is the same text that lives here.

| File | What it does | Verified |
|---|---|---|
| `landsat_st.py` | Landsat Collection 2 surface temperature, DN to °F | conversion tested |
| `zonal_tracts.py` | Mean temperature per census tract | syntax only |
| `impervious_fit.py` | Impervious surface against temperature | tested |
| `clean_wqp.py` | Tidy a Water Quality Portal download | tested |
| `station_trends.py` | Mann-Kendall trend and Sen slope per station | tested |
| `overlay_fire.py` | Slope, aspect, weighted risk, burn capture | tested |
| `pyqgis_clip.py` | Clip a raster to a study area in QGIS | syntax only |
| `slr_inundation.py` | Ocean-connected inundation and totals | tested |
| `sample_buildings.py` | DEM elevation at building footprints | syntax only |
| `idw.py` | Inverse distance weighting | tested |
| `acs_join.py` | Join ACS income to block groups | join logic tested |
| `exposure_by_income.py` | Exposure by income tercile | tested |
| `monitors_per_bg.sql` | Monitors per block group (PostGIS) | not run |

"Tested" means the function was executed against synthetic data with its output checked.
The snippets marked "syntax only" read files from disk and were parsed but not run.

### Browser tools

The GIS Tools page runs entirely client-side -- nothing is uploaded. It includes a
coordinate and UTM converter, distance and bearing, spectral indices, Landsat scaling,
map scale, slope units, a GeoJSON inspector and a CRS reference table. The coordinate
and distance math was checked against [pyproj](https://pyproj4.github.io/pyproj/):
UTM agreed to within a micrometre across fourteen test points spanning both hemispheres.

## Running it locally

No build step is needed to view the site -- open `index.html` in a browser.

To rebuild after editing anything in `src/` or `code/`:

```bash
python3 build.py
```

To serve it the way a host would:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Adding your finished maps

Edit `src/maps-data.js` and add one entry per project, then run `python3 build.py`:

```js
window.MAPS_DATA = {
  heat: {
    src: "maps/heat-philadelphia.png",
    alt: "Land surface temperature by census tract, Philadelphia",
    caption: "Landsat 9, 14 August 2025. EPSG:5070."
  }
};
```

Put the image files in a `maps/` folder next to `index.html`. Project ids are
`heat`, `water`, `fire`, `coast` and `air`. Any project without an entry shows a
"map in progress" placeholder.

## Filling in the resume

Edit `src/resume-data.js`. Text in `[square brackets]` renders highlighted as a
placeholder. Once every bracket is replaced, set `placeholder: false` to remove the
template notice, then rebuild.

## Notes on the demos

The interactive demos generate synthetic data in the browser. They show how each method
behaves and what its output looks like; they are not measurements of any real place, and
the site says so on every demo. The finished maps use the real public datasets cited on
each project.

## Built with

Plain HTML, CSS and JavaScript with no framework and no build dependencies beyond Python's
standard library. Fonts come from Google Fonts; everything else is self-contained.
