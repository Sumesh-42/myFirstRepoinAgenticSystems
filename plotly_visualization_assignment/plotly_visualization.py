import pandas as pd
import plotly.express as px
import numpy as np
# Create a dataset
epochs = np.arange(1, 11)
training_loss = np.random.uniform(low=0.5, high=1.0, size=len(epochs))
# Create a DataFrame
data = pd.DataFrame({'Epoch': epochs, 'Training Loss': training_loss})
# Create a line chart using Plotly Express
fig = px.line(data, x='Epoch', y='Training Loss', title='Training Loss Over Epochs', markers=True)
# Add annotation for where the loss stabilizes
stabilization_epoch = 5  # Example epoch where loss stabilizes
fig.add_annotation(x=stabilization_epoch, y=training_loss[stabilization_epoch-1],
                   text="Loss Stabilizes Here", showarrow=True, arrowhead=1)
# Display the chart
fig.show()
