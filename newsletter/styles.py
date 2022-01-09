# Colors
BLUE = "#1051ea"
DARK_GREY = "#525252"
LIGHT_GREY = "#f0f0f0"
CSESOC_BLUE = "#3A76F8"
CSESOC_GREY = "#40404C"

# Fonts
HELVETICA = "Helvetica, Arial, sans-serif"
UBUNTU = "Ubuntu, Helvetica, Arial, sans-serif"
UBUNTU_MONO = "'Ubuntu Mono', monospace"

# Classes
SECTION_BACKGROUND = f"""
    background: red;
"""

SECTION_HEADER = f"""
    font-family: {HELVETICA};
    font-weight: bold;
    font-size: 24px;
    text-transform: uppercase;
    text-align: center;
    line-height: 2;
"""
    # width: 100%;
    # background: red;
    # letter-spacing: 10px;

TITLE = f"""
    font-family: {HELVETICA};
    font-size: 18px;
    font-weight: bold;
    margin-block-start: 0;
    margin-block-end: 10px;
"""

DESC = f"""
    font-family: {UBUNTU};
    font-size: 13px;
    line-height: 1.4;
    min-height: 60px;
    color: {DARK_GREY};
"""

CAPTION = f"""
    font-family: {UBUNTU};
    font-size: 12px;
    text-transform: uppercase;
    color: {DARK_GREY};
"""

BUTTON = f"""
    font-family: {UBUNTU};
    background: {BLUE};
    color: white;
    font-size: 13px;
    text-transform: uppercase;
    text-align: center;
    border-radius: 3px;
    margin-top: 20px;
"""

DIVIDER = f"""
    border-top: 1px dashed {LIGHT_GREY};
    width: 100%;
"""
