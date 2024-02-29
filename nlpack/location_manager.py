import os

class LocationManager:
    r_dir = str #plain text
    m_dir = str #modified text

    directories = ["../data/r_dir",
                   "../data/m_dir"]

    [os.makedirs(directory) for directory in directories if not os.path.exists(directory)]
