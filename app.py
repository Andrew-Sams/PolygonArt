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
    fig.patch.set facecolor('black')
    ax.set_facecolor('black')

    # Draw the circle