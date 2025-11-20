import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randn(30,4),
    columns=["London", "New York", "Tokyo", "Dubai"]
)

col1,col2 = st.columns(2)

with col1:
    st.line_chart(data)
with col2:
    st.area_chart(data)


# 2. Give your web app a title
st.title("My First Plot App")

# 3. Prepare some data to plot
# This creates a list of numbers from 0 to 10
x_values = np.linspace(0, 10, 100)
# This creates a wave pattern based on the x values
y_values = np.sin(x_values)

# 4. Create the plot using Matplotlib's object-oriented approach
# We ask for an empty figure 'fig' and an 'ax'es area to draw in
fig, ax = plt.subplots()

# Tell our 'ax'es area to draw a line plot using our data
ax.plot(x_values, y_values)

# Add some labels for clarity
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('A Simple Sine Wave')

# 5. Tell Streamlit to display this specific figure 'fig'
st.pyplot(fig)