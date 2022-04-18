import pandas as pd
from pathlib import Path
import numpy as np
import os
import panel as pn
pn.extension('plotly')
import plotly.express as px
import hvplot.pandas
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import ipywidgets as widgets
import holoviews as hv
import dash
import dash_core_components as dcc
import dash_html_components as html
hv.extension('bokeh')
from ipywidgets import interact, interactive, fixed, interact_manual, Output, VBox, widgets
from pathlib import Path
from dotenv import load_dotenv
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

load_dotenv()
map_box_api = os.getenv("mapbox")
px.set_mapbox_access_token(map_box_api)

filepath = '../raw_data/SW_high_hits.XLSX'
sw_high_hits = pd.read_excel(filepath)
sw_high_hits['Sampling Qualifier'] = sw_high_hits['Sampling Qualifier'].fillna("")
sw_high_hits = sw_high_hits.dropna(subset=['Lat'])

sw_dioxin = sw_high_hits.loc[sw_high_hits["COC Category"]=="Dioxin/Furan"]
sw_metal = sw_high_hits.loc[sw_high_hits["COC Category"]=="Metal"]
sw_pah = sw_high_hits.loc[sw_high_hits["COC Category"]=="PAH"]
sw_pcb = sw_high_hits.loc[sw_high_hits["COC Category"]=="PCB"]
sw_pesticide = sw_high_hits.loc[sw_high_hits["COC Category"]=="Pesticide"]
sw_dac = sw_high_hits.loc[sw_high_hits["COC Category"]=="Dioxin-Associated Compound"]
sw_svoc = sw_high_hits.loc[sw_high_hits["COC Category"]=="SVOC"]
sw_voc = sw_high_hits.loc[sw_high_hits["COC Category"]=="VOC"]

def coc_density_plot(coc_density_df, coc, radius):
    px.set_mapbox_access_token(map_box_api)
    coc_fig = px.density_mapbox(
        coc_density_df,
        lat="Lat",
        lon="Lon",
        z="ppb (sampling result)",
        zoom=16,
        height=1200,
        width=1300,
        hover_data=["Compound", "Chemical List Group (Dkt. 958)", "Sampling Medium"],
        title=f"Sherwin-Williams Upland Site - {coc} Highest Sampling Results")
    return coc_fig.show()

sw_dioxin_density = coc_density_plot(sw_dioxin, "Dioxins/Furans", 15)
sw_pcb_density = coc_density_plot(sw_pcb, "PCBs", 15)
sw_metal_density = coc_density_plot(sw_metal, "Metals", 15)
sw_pesticide_density = coc_density_plot(sw_pesticide, "Pesticides", 15)
sw_pah_density = coc_density_plot(sw_pah, "PAHs", 15)
sw_voc_density = coc_density_plot(sw_voc, "VOCs", 15)
sw_svoc_density = coc_density_plot(sw_svoc, "SVOCs", 15)
sw_dac_density = coc_density_plot(sw_dac, "Dioxin-Associated Compounds", 15)