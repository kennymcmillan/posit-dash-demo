import os
from datetime import datetime

import dash
from dash import Input, Output, dcc, html

app = dash.Dash(__name__, title="Posit Dash Demo")
server = app.server  # WSGI entrypoint required by Posit Connect

app.layout = html.Div(
    style={"fontFamily": "system-ui, sans-serif", "maxWidth": "640px", "margin": "2rem auto"},
    children=[
        html.H1("Posit Connect — Dash Deployment Check"),
        html.P("If you can see this on Posit Connect, the deploy works."),
        html.Div(
            [
                html.Label("Your name:"),
                dcc.Input(id="name-input", value="Kenny", type="text", style={"marginLeft": "0.5rem"}),
            ]
        ),
        html.Hr(),
        html.Div(id="greeting"),
        html.Pre(id="env-info", style={"background": "#f4f4f4", "padding": "0.75rem", "borderRadius": "4px"}),
    ],
)


@app.callback(Output("greeting", "children"), Input("name-input", "value"))
def greet(name):
    return f"Hello, {name or 'stranger'} — rendered at {datetime.now().isoformat(timespec='seconds')}"


@app.callback(Output("env-info", "children"), Input("name-input", "value"))
def env_info(_):
    keys = ["CONNECT_SERVER", "CONNECT_CONTENT_GUID", "SPORTS_API_URL"]
    lines = [f"{k} = {os.environ.get(k, '<unset>')}" for k in keys]
    return "\n".join(lines)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
