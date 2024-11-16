import mujoco
from mujoco import viewer

# Loading a specific model description as an imported module.
from robot_descriptions import panda_mj_description
model = mujoco.MjModel.from_xml_path(panda_mj_description.MJCF_PATH)

# Directly loading an instance of MjModel.
# from robot_descriptions.loaders.mujoco import load_robot_description
# model = load_robot_description("panda_mj_description")

# # Loading a variant of the model, e.g. panda without a gripper.
# model = load_robot_description("panda_mj_description", variant="panda_nohand")

data = mujoco.MjData(model)

# Create the viewer
try:
    with viewer.launch(model, data) as sim_viewer:
        print("Viewer launched. Press ESC to exit.")
        
        # Simulation loop
        while sim_viewer.is_running():
            # Step the simulation
            mujoco.mj_step(model, data)
            
            # Update the viewer
            sim_viewer.sync()
except Exception as e:
    print(f"Error running viewer: {e}")