# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    # Function to ensure that the value is within the range [0, 255]
    def clamp(x):
        return max(0, min(x, 255))
    
    # Convert each decimal value to its hexadecimal representation
    return '{:02X}{:02X}{:02X}'.format(clamp(r), clamp(g), clamp(b))