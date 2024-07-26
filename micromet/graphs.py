import plotly.graph_objects as go

import pandas as pd

def energy_sankey(df, date_text="2024-06-19 12:00"):
    select_date = pd.to_datetime(date_text)
    swi = df.loc[select_date, "SW_IN"]
    lwi = df.loc[select_date, "LW_IN"]
    swo = df.loc[select_date, "SW_OUT"]
    lwo = df.loc[select_date, "LW_OUT"]
    nr = df.loc[select_date, "NETRAD"]
    shf = df.loc[select_date, "G"]
    le = df.loc[select_date, "LE"]
    h = df.loc[select_date, "H"]

    # Define the energy balance terms and their indices
    labels = [
        "Incoming Shortwave Radiation",
        "Incoming Longwave Radiation",
        "Total Incoming Radiation",
        "Outgoing Shortwave Radiation",
        "Outgoing Longwave Radiation",
        "Net Radiation",
        "Ground Heat Flux",
        "Sensible Heat",
        "Latent Heat",
        "Residual"
    ]

    print(h)
    rem = nr - (shf + h + le)

    ebr = (h + le) / (nr - shf)

    # Define the source and target nodes and the corresponding values for the energy flow
    source = [0, 1, 2, 2, 2, 5, 5, 5, 5]  # Indices of the source nodes
    target = [2, 2, 5, 3, 4, 6, 7, 8, 9]  # Indices of the target nodes

    # Define the source and target nodes and the corresponding values for the energy flow
    # source = [0, 1, 2, 2, 2, 5, 5, 5, 5]  # Indices of the source nodes
    # target = [2, 2, 5, 3, 4, 6, 7, 8, 9]  # Indices of the target nodes
    values = [lwi, swi, nr, swo, lwo, shf, h, le, rem]  # Values of the energy flow

    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
        ),
        link=dict(
            source=source,
            target=target,
            value=values,
        )
    )])

    # Update layout and title
    fig.update_layout(title_text=f"Energy Balance {ebr:0.2f} on {select_date:%Y-%m-%d}", font_size=10)

    # Show the figure
    # fig.show()
    return fig