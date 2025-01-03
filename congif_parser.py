from loguru import logger
import configparser

# Initialize ConfigParser and read the configuration file
config = configparser.ConfigParser()
config_file_path = "/Users/sarveshjere/Desktop/Python Tutoriala/config_file.ini"

if not config.read(config_file_path):
    logger.error(f"Could not read the configuration file at {config_file_path}")
elif "raw_materials" not in config:
    logger.error("The section 'raw_materials' is missing in the configuration file.")
else:
    brick_cost = int(config["raw_materials"]["brick_cost"])  # Convert to integer
    logger.info(f"Brick cost per unit: {brick_cost}")

    # Function to calculate the total number of bricks
    def total_number_Bricks(length, breadth, height):
        no_of_bricks_in_length = length * height
        total_bricks_in_length = no_of_bricks_in_length * 2

        no_of_bricks_in_breadth = breadth * height
        total_bricks_in_breadth = no_of_bricks_in_breadth * 2

        total_number_Bricks = total_bricks_in_length + total_bricks_in_breadth
        return total_number_Bricks

    # Function to calculate the total cost of bricks
    def cost_of_bricks(config):
        brick_cost = int(config["raw_materials"]["brick_cost"])
        total_number_Bricks1 = total_number_Bricks(15, 15, 10)
        final_cost = brick_cost * total_number_Bricks1
        return final_cost

    # Call the function and log the result
    result = cost_of_bricks(config)
    logger.info(f"Total cost to make the room is {result}")
