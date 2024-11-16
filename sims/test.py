import mujoco
from mujoco import viewer

# Path to your MuJoCo XML model file
model_path = "/home/kadi/Desktop/Thesis/sims/mujoco_menagerie/universal_robots_ur5e/ur5e.xml"

# Load the model and create the data structure
try:
    model = mujoco.MjModel.from_xml_path(model_path)
    data = mujoco.MjData(model)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Launch the interactive viewer
print("Launching the simulation. Close the viewer window to exit.")
try:
    viewer.launch(model, data)
    for i in range(data.ncon):
        contact = data.contact[i]
        print(f"Contact {i}: geom1={contact.geom1}, geom2={contact.geom2}")
        
except Exception as e:
    print(f"Error running viewer: {e}")

