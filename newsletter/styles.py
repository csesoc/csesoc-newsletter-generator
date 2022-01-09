# Colors
BLUE = "#1051ea"
LIGHT_BLUE = "#3c54ec"
DARK_GREY = "#525252"
LIGHT_GREY = "#f0f0f0"
CSESOC_BLUE = "#3A76F8"
CSESOC_GREY = "#40404C"

# Fonts
HELVETICA = "Helvetica, Arial, sans-serif"
UBUNTU = "Ubuntu, Helvetica, Arial, sans-serif"
UBUNTU_MONO = "'Ubuntu Mono', monospace"

# Classes
SECTION_HEADER = f"""
    font-family: {HELVETICA};
    font-weight: bold;
    font-size: 24px;
    text-transform: uppercase;
    text-align: center;
    line-height: 2;
    border-bottom: 5px solid {BLUE};
    margin-block-start: 0;
    margin-block-end: 0;
"""

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
    border-top: 3px dashed {LIGHT_GREY};
    width: 100%;
"""

SOCIALS = f"""
    font-family: {UBUNTU};
    font-size: 13px;
    text-align: center;
    color: {DARK_GREY};
    background: {LIGHT_GREY};
    width: 100%
    line-height: 3;
"""
