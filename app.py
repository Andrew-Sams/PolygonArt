import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Circle
from random import randint, uniform, choice

# Function to generate random polygons
def generate_random_polygon(max_radius, num_sides):
    angles = np.sort(np.random.rand(num_sides) * 2 * np.pi)
    radii = np.random.rand(num_sides) * max_radius
    points = np.array([radii * np.cos(angles), radii * np.sin(angles)]).T
    return points

# Function to create the plot
def create_plot(circle_radius, num_polygons, num_recursive_steps, num_child_polygons, random_seed):
    if random_seed:
        np.random.seed(0)

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Draw the circle
    circle = Circle((0, 0), circle_radius, color='blue', fill=False)
    ax.add_patch(circle)

    for _ in range(num_polygons):
        # Generate parent polygon
        parent_polygon_points = generate_random_polygon(circle_radius, randint(3, 10))
        parent_polygon = Polygon(parent_polygon_points, closed=True, color='white', alpha=uniform(0, 1))
        ax.add_patch(parent_polygon)

        # Generate child polygons recursively
        for _ in range(num_recursive_steps):
            for _ in range(num_child_polygons):
                child_polygon_points = generate_random_polygon(circle_radius / 4, randint(3, 10))  # Adjust as needed
                child_polygon = Polygon(child_polygon_points, closed=True, color='white', alpha=uniform(0, 1))
                ax.add_patch(child_polygon)

    ax.set_xlim(-circle_radius, circle_radius)
    ax.set_ylim(-circle_radius, circle_radius)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    return fig

# Streamlit UI
st.title("Interactive Polygon Plotter")

circle_radius = st.slider("Circle Radius", 1, 10, 5)
num_polygons = st.slider("Number of Polygons", 1, 20, 10)
num_recursive_steps = st.slider("Number of Recursive Steps", 0, 5, 0)
num_child_polygons = st.slider("Number of Child Polygons per Step", 1, 10, 2)
random_seed = st.checkbox("Set Random Seed")

if st.button("Recompute Plot"):
    fig = create_plot(circle_radius, num_polygons, num_recursive_steps, num_child_polygons, random_seed)
    st.pyplot(fig)
