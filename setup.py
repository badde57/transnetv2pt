import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="transnetv2pt",
    version="1.0.0",
    author="badde57", # TODO: Replace with actual author name
    author_email="badde57@protonmail.com", # TODO: Replace with actual author email
    description="PyTorch implementation of TransNet V2", # TODO: Confirm/Update description
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/badde57/transnetv2pt", # TODO: Replace with the upstream GitHub repo URL
    include_package_data=True,
    install_requires=[
        "torch>=1.7",
        "ffmpeg-python>=0.2.0", # Pinned minimum version
        "pillow>=9.0", # Pinned minimum version
        "numpy>=1.18" # Added missing dependency
    ],
    packages=setuptools.find_packages(),
    package_dir={"transnetv2pt": "transnetv2pt"},
    package_data={"transnetv2pt": ["transnetv2-pytorch-weights.pth"]}
)
